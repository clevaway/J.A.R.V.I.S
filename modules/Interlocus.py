import os
from dotenv import load_dotenv
import speech_recognition as sr
import pyttsx3

import sounddevice as sd
from kokoro_onnx import Kokoro
import asyncio
import time
import queue
import numpy as np
import sounddevice as sd
import webrtcvad
import logging
import pywhispercpp.constants as constants
from pywhispercpp.model import Model

load_dotenv(override=True)

KOKORO_VOICE = os.getenv('KOKORO_VOICE')


class Interlocus:
    def __init__(self):
        self.kokoro = Kokoro("kokoro-v0_19.onnx", "voices-v1.0.bin")
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.input_device = None  # Added: use default input device

    async def speak(self, text):
        print(f"JARVIS: {text}")
        
        stream = self.kokoro.create_stream(
            text,
            voice=KOKORO_VOICE,
            speed=1.0,
            lang="en-us",
        )

        count = 0
        async for samples, sample_rate in stream:
            count += 1
            print(f"Speaking ({count})...")
            sd.play(samples, sample_rate)
            sd.wait()

    #  available models are: ['base', 'base-q5_1', 'base.en', 'base.en-q5_1', 'large-v1', 'large-v2', 'large-v2-q5_0', 'large-v3', 'large-v3-q5_0', 'large-v3-turbo', 'large-v3-turbo-q5_0', 'medium', 'medium-q5_0', 'medium.en', 'medium.en-q5_0', 'small', 'small-q5_1', 'small.en', 'small.en-q5_1', 'tiny', 'tiny-q5_1', 'tiny.en', 'tiny.en-q5_1', 'tiny.en-q8_0']
    # whisper_init_from_file_with_params_no_state: loading model from '/Users/username/Library/Application Support/pywhispercpp/models/ggml-base.bin'
    def listen(self):

        # Set parameters from pywhispercpp constants and desired configuration
        sample_rate = constants.WHISPER_SAMPLE_RATE  # same as whisper.cpp
        channels = 1
        block_duration = 30  # block duration in milliseconds
        block_size = int(sample_rate * block_duration / 1000)

        # Create a queue to accumulate audio blocks
        q = queue.Queue()
        # Initialize VAD (voice activity detector)
        vad = webrtcvad.Vad()
        # Silence and queue thresholds (in number of blocks)
        silence_threshold = 16
        q_threshold = 16
        silence_counter = 0

        # Initialize the Whisper model (using a tiny English model as an example)
        model = Model("small.en",
                      print_realtime=False,
                      print_progress=False,
                      print_timestamps=False,
                      single_segment=True,
                      no_context=True)

        # This variable will accumulate all transcribed text
        transcription = ""
        # Flag to indicate that transcription has completed
        done = False

        def _audio_callback(indata, frames, time_info, status):
            nonlocal silence_counter
            if status:
                logging.warning(f"Audio warning: {status}")
            # Ensure we have the expected number of frames
            assert frames == block_size
            # Normalize audio from [-1,1] to [0,1]
            audio_data = np.fromiter(map(lambda x: (x + 1) / 2, indata.flatten()), dtype=np.float16)
            # Convert normalized audio to bytes
            audio_bytes = audio_data.tobytes()
            # Use VAD to detect if speech is present
            if vad.is_speech(audio_bytes, sample_rate):
                q.put(indata.copy())
                silence_counter = 0
            else:
                if silence_counter >= silence_threshold:
                    if q.qsize() > q_threshold:
                        _transcribe_speech()
                        silence_counter = 0
                else:
                    silence_counter += 1

        def _transcribe_speech():
            nonlocal transcription, done
            logging.info("Speech detected ...")
            audio_data = np.array([])
            # Concatenate all queued audio blocks
            while not q.empty():
                audio_data = np.append(audio_data, q.get())
            # Append zeros to workaround small audio packets
            audio_data = np.concatenate([audio_data, np.zeros((int(sample_rate) + 10))])
            # Run inference; update transcription via the callback
            def callback(seg):
                nonlocal transcription
                transcription += seg.text + " "
                print(f"YOU: {seg.text}")
            model.transcribe(audio_data, new_segment_callback=callback)
            done = True

        print("SYSTEM: Listening... (will stop after one transcription)")
        with sd.InputStream(device=self.input_device,  # use self.input_device if set, else default
                            channels=channels,
                            samplerate=sample_rate,
                            blocksize=block_size,
                            callback=_audio_callback):
            try:
                # Listen until speech is transcribed
                while not done:
                    time.sleep(0.1)
            except KeyboardInterrupt:
                print("SYSTEM: Stopped listening by KeyboardInterrupt.")
        return transcription.strip()