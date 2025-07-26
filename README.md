# Jarvis

The J.A.R.V.I.S Large Language Model, 100% offline

We have use custom jarvis dataset and various other open datasets on the internet of jarvis's dialog with stark to fine-tune on top of Llama2 7b

## Content

- Dataset [here](https://huggingface.co/datasets/fotiecodes/jarvis-llama2-dataset) | dataset is being created progresively
- Model: [here](https://huggingface.co/fotiecodes/Llama-2-7b-chat-jarvis) | Updated every week or so

Jarvis is bing built with privacy in mind, everything runs locally. This fine-tuned model is better at responding like jarvis and producing response in the best jarvis tone possible.

## Star History

<a href="https://www.star-history.com/#clevaway/J.A.R.V.I.S&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=clevaway/J.A.R.V.I.S&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=clevaway/J.A.R.V.I.S&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=clevaway/J.A.R.V.I.S&type=Date" />
 </picture>
</a>

## Current features

- [x] Jarvis can tell you the current date and time just ask:) `Try: What time is it?  what is the date of today?`
- [x] Open your default browser and search for something `Try: hey jarvis, help me search for the best african dish out there`
- [x] play youtube video by title `Try: hey jarvis, play Girls like you by Maroon 5 on youtube`
- [x] You can ask jarvis what it sees(uses the webcam, only works in the project not the chat, you have to run the while project. NB: it uses llava(100% offline), so you have to download and install it with ollama command "`ollama run llava`" )  `Try:"what is this?"  "what are you looking at?", "tell me what you see", "describe this" or even "describe what you see"`
- [ ] Search on wikipedia
- [ ] Send emails from contacts

### Usage

#### Installation

I. You will need Ollama to download and install the model for use locally.

1. Download and install ollama [here](https://ollama.com/)
2. Run the command:

  ```bash
ollama run fotiecodes/jarvis
  ```

  This will install the model [jarvis](https://ollama.com/fotiecodes/jarvis) model locally.
3. From here you can already chat with jarvis from the command line by running the same command `ollama run fotiecodes/jarvis` or `ollama run fotiecodes/jarvis:latest` to run the lastest stable release.

II. After installing the model locally and started the ollama sever and can confirm it is working properly, clone this repositry and run the main.py file

### 🚨 Important

Please check the `.env.example` file and add the neccessary env variables before running.

That's it, you can start talking to Jarvis✨

### Setup local dev

Please go to [CONTRIBUTOR.md](CONTRIBUTOR.md) for more info.

To-Do:

- [x] Prepare instruct dataset(WIP)
- [x] Fine-tune llama2-7b for a costum model `Llama-2-7b-chat-jarvis"`(WIP)
- [ ] Build a proper voice clone of jarvis(In progress): currently having difficulties finding clean voice samples of jarvis on the internet, so working with what i have, i guess won't be perfect.
- [ ] Use Whisper for voice to text input(if anyone has anything better, please suggest as this is the best i found out there.)
- [ ] Deploy the voice model as an API for everyone to be able to use it locally(We can deploy on my vps i don't know, if the specs will even let us though, we'll see)

<!-- ## Converting model from hf to gguf file
Command:
```bash
python llama.cpp/convert.py jarvis-hf \
  --outfile jarvis-7b-v0.1.gguf \
  --outtype q8_0
``` -->

## Installing TTS for local processing

for offline tts we use Kokoro, an amazing low latency tts
Note: on Linux you need to run this as well: `apt-get install portaudio19-dev`
In the root directory of the project, run the following command

```bash
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/kokoro-v0_19.onnx
wget https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files/voices.json
```

Note: the voice name is already set in the .env file(the actual jarvis voice will be coming soon) this one is closest we have at the moment to jarvis's voice.

## Why Jarvis?

Well, simple. I have always wanted to have my very own Jarvis, now i'm not talking about a siri clone or google home assitant clone. I am talking about my very own Jarvis, talks like jarvis, response like jarvis, feels like jarvis in the most accurate way possible.

## Acknowledgments

Special thanks to:

- [ollama]([ollama](https://github.com/ollama/ollama)) for the amazing project
- [ggerganov](https://github.com/ggerganov) the genius behind [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [kokoro-onnx](https://github.com/thewh1teagle/kokoro-onnx) the tts that powers jarvis for offline inferencing
- Every contributor to this repo:)

### Supporters ✨
<https://github.com/thewh1teagle/kokoro-onnx/projects[>]

- We're looking for Sponsors!

### License 📜

This project is licensed under the [MIT License](LICENSE) - see the LICENSE file for details. 📄

### Support 💬

If you have any questions, suggestions, or need assistance, please open an issue:)

**Disclaimer**:
Jarvis can make mistakes. Consider checking important information.

###### * This project was inspired by "J.A.R.V.I.S" from the Marvel movie series
