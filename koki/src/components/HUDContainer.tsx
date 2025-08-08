import React, { useState } from "react";
import JarvisHUD, { HUDMode } from "./JarvisHUD";
import { MicVAD } from "./MicVAD";
import DraggableArea from "./DraggableArea";
import { Mic, MicOff } from "lucide-react";

export function HUDContainer() {
  const [micOn, setMicOn] = useState(true);
  const [mode, setMode] = useState<HUDMode>("idle");
  const [volume, setVolume] = useState(0);

  return (
    <div className="min-h-screen w-full bg-[#051824] flex flex-col items-center justify-center p-6">
      <DraggableArea />

      <JarvisHUD mode={mode} volume={micOn ? volume : 0} />

      {/* Headless VAD below the HUD. Turns mic data into HUD state. */}
      <MicVAD
        enabled={micOn}
        onUpdate={({ volume, mode }) => {
          setVolume(volume);
          // Smooth thinking -> listening after a short delay would be handled here if desired
          setMode(mode);
        }}
      />
    
      {/* Controls under the HUD */}
     <div className="space-y-2">
       <div className="mt-6 flex items-center gap-4">
        <button
          onClick={() => setMicOn(v => !v)}
          className={`px-4 py-2 rounded-xl text-sm font-medium shadow-md transition active:scale-95 border flex items-center gap-2 ${
            micOn
              ? "bg-cyan-600/20 border-cyan-400/40 text-cyan-100 hover:bg-cyan-600/30"
              : "bg-slate-700/40 border-slate-500/40 text-slate-200 hover:bg-slate-700/60"
          }`}
          aria-pressed={micOn}
        >
          {micOn ? <Mic size={16} /> : <MicOff size={16} />}
          {micOn ? "Mute" : "Unmute"}
        </button>

        {/* Manual mode overrides for testing */}
        {/* <div className="flex gap-2">
          {(["idle","listening","speaking","thinking"] as HUDMode[]).map(m => (
            <button key={m} onClick={() => setMode(m)} className={`px-3 py-1 rounded border text-xs uppercase tracking-wide ${mode===m?"border-cyan-400 text-cyan-100":"border-slate-500 text-slate-300"}`}>{m}</button>
          ))}
        </div> */}

      </div>
      <div className="text-sm text-cyan-100/80 font-mono ml-2 text-center">vol: {volume.toFixed(2)}</div>
     </div>
    </div>
  );
}