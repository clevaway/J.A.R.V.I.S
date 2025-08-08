/* eslint-disable react-hooks/exhaustive-deps */

// ==============================
// MicVAD.tsx (separate component)
// ==============================
import { useEffect, useRef, useState } from "react";
import type { HUDMode } from "./JarvisHUD";

export interface MicVADProps {
  enabled: boolean;
  onUpdate: (data: { volume: number; mode: HUDMode }) => void;
}

export function MicVAD({ enabled, onUpdate }: MicVADProps) {
  // Removed unused volume state
  const [speaking, setSpeaking] = useState(false);
  const [listening, setListening] = useState(false);
  const lastVoiceTsRef = useRef<number>(0);

  const analyserRef = useRef<AnalyserNode | null>(null);
  const streamRef = useRef<MediaStream | null>(null);
  const rafRef = useRef<number | null>(null);

  useEffect(() => {
    let ctx: AudioContext | null = null;
    let source: MediaStreamAudioSourceNode | null = null;

    async function start() {
      try {
        if (!enabled) return;
        const stream = await navigator.mediaDevices.getUserMedia({ audio: { noiseSuppression: true, echoCancellation: true }, video: false });
        streamRef.current = stream;
        ctx = new (window.AudioContext || (window as any).webkitAudioContext)();
        source = ctx.createMediaStreamSource(stream);
        const analyser = ctx.createAnalyser();
        analyser.fftSize = 1024;
        analyser.smoothingTimeConstant = 0.85;
        source.connect(analyser);
        analyserRef.current = analyser;
        loop();
      } catch (e) {
        console.warn("Mic permission/error:", e);
        onUpdate({ volume: 0, mode: "idle" });
      }
    }

    function stop() {
      if (rafRef.current) cancelAnimationFrame(rafRef.current);
      analyserRef.current = null;
      if (streamRef.current) {
        streamRef.current.getTracks().forEach(t => t.stop());
        streamRef.current = null;
      }
      if (ctx) ctx.close();
      // setVolume(0); // Removed unused volume state
      setSpeaking(false);
      setListening(false);
      onUpdate({ volume: 0, mode: "idle" });
    }

    function loop() {
      const analyser = analyserRef.current;
      if (!analyser) return;
      const data = new Uint8Array(analyser.fftSize);
      analyser.getByteTimeDomainData(data);
      let sum = 0;
      for (let i = 0; i < data.length; i++) {
        const v = (data[i] - 128) / 128;
        sum += v * v;
      }
      const rms = Math.sqrt(sum / data.length);
      const level = Math.min(1, Math.pow(rms * 2.2, 1.2));
      // setVolume(level); // Removed unused volume state

      const now = performance.now();
      const SPEAK_THRESHOLD = 0.12;
      const QUIET_THRESHOLD = 0.06;
      const MIN_SPEAK_TIME = 120;

      const isLoud = level > SPEAK_THRESHOLD;
      const isQuiet = level < QUIET_THRESHOLD;

      if (isLoud) {
        setListening(true);
        if (!speaking && (lastVoiceTsRef.current === 0 || now - lastVoiceTsRef.current > MIN_SPEAK_TIME)) {
          setSpeaking(true);
        }
        lastVoiceTsRef.current = now;
      } else if (isQuiet) {
        setSpeaking(false);
      }

      let mode: HUDMode = "idle";
      const idleNow = lastVoiceTsRef.current && now - lastVoiceTsRef.current > 10000; // 10s
      if (!enabled) mode = "idle";
      else if (speaking) mode = "speaking";
      else if (!speaking && listening && !idleNow) mode = "thinking"; // transient, parent can smooth
      else if (listening && idleNow === false) mode = "listening";
      else mode = "idle";

      onUpdate({ volume: level, mode });

      rafRef.current = requestAnimationFrame(loop);
    }

    if (enabled) start();
    else stop();

    return () => stop();
  }, [enabled]);

  return null; // headless component
}