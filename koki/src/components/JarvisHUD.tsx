import React from "react";
import { motion } from "framer-motion";

export type HUDMode = "idle" | "listening" | "speaking" | "thinking";

export interface JarvisHUDProps {
  mode: HUDMode;
  /** 0..1 volume. Used for center pulse scale. Optional. */
  volume?: number;
  /** SVG artboard size. Default 520. */
  size?: number;
  /** Center label. Default "J.A.R.V.I.S" */
  label?: string;
  /** Pause all animations */
  paused?: boolean;
}

export default function JarvisHUD({ mode, volume = 0, size = 520, label = "J.A.R.V.I.S", paused = false }: JarvisHUDProps) {
  const stroke = "#19E3FF";
  const dim = "#0AAFD1";

  const speeds = {
    speaking: 8,
    thinking: 12,
    listening: 18,
    idle: 26,
  } as const;

  const outerSpeed = speeds[mode];
  const counterSpeed = outerSpeed + 4;
  const pulseScale = 1 + Math.min(0.25, Math.max(0, Math.min(1, volume)) * 0.6);

  return (
    <div className="relative aspect-square w-[min(60vw,520px)] select-none" style={{cursor:"default"}}>
      {/* Soft outer glow */}
      <div
        className="absolute inset-0 rounded-full blur-3xl opacity-30"
        style={{
          background:
            "radial-gradient(50% 50% at 50% 50%, rgba(25,227,255,0.35) 0%, rgba(5,24,36,0) 70%)",
        }}
      />

      <svg viewBox={`0 0 ${size} ${size}`} className="relative z-10">
        <defs>
          <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="2" result="coloredBlur" />
            <feMerge>
              <feMergeNode in="coloredBlur" />
              <feMergeNode in="SourceGraphic" />
            </feMerge>
          </filter>
          <radialGradient id="centerGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stopColor="#0BC2E6" stopOpacity="0.35" />
            <stop offset="60%" stopColor="#0BC2E6" stopOpacity="0.08" />
            <stop offset="100%" stopColor="#0BC2E6" stopOpacity="0" />
          </radialGradient>
        </defs>

        {/* Background faint disc */}
        <circle cx={260} cy={260} r={240} fill="url(#centerGrad)" />

        {/* Static base ring */}
        <circle cx={260} cy={260} r={210} fill="none" stroke={dim} strokeOpacity="0.25" strokeWidth="2" />

        {/* Rotating segmented ring (outer) */}
        <motion.g
          style={{ originX: 0.5, originY: 0.5 }}
          animate={paused ? { rotate: 0 } : { rotate: 360 }}
          transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: outerSpeed, ease: "linear" }}
          filter="url(#glow)"
        >
          <circle cx={260} cy={260} r={230} fill="none" stroke={stroke} strokeWidth="3" strokeDasharray="6 18" strokeLinecap="round" opacity={mode === "idle" ? 0.35 : 0.6} />
          <circle cx={260} cy={260} r={222} fill="none" stroke={stroke} strokeWidth="4" strokeDasharray="2 10" opacity={mode === "idle" ? 0.2 : 0.35} />
        </motion.g>

        {/* Counter-rotating thin markers */}
        <motion.g
          style={{ originX: 0.5, originY: 0.5 }}
          animate={paused ? { rotate: 0 } : { rotate: -360 }}
          transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: counterSpeed, ease: "linear" }}
          filter="url(#glow)"
        >
          <circle cx={260} cy={260} r={195} fill="none" stroke={stroke} strokeWidth="2" strokeDasharray="1 12" opacity={mode === "idle" ? 0.45 : 0.7} />
        </motion.g>

        {/* Inner rotating arcs */}
        <motion.g
          style={{ originX: 0.5, originY: 0.5 }}
          animate={paused ? { rotate: 0 } : { rotate: 360 }}
          transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: Math.max(6, outerSpeed - 6), ease: "linear" }}
          filter="url(#glow)"
        >
          {Array.from({ length: 12 }).map((_, i) => (
            <Arc key={i} cx={260} cy={260} r={165} start={i * 30 + 4} sweep={16} stroke={stroke} width={5} opacity={mode === "thinking" ? 0.5 : 0.9} />
          ))}
        </motion.g>

        {/* Fine inner dial */}
        <motion.g style={{ originX: 0.5, originY: 0.5 }} animate={paused ? { rotate: 0 } : { rotate: -360 }} transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: outerSpeed + 6, ease: "linear" }}>
          <circle cx={260} cy={260} r={140} fill="none" stroke={dim} strokeWidth="2" strokeDasharray="2 8" opacity={0.6} />
        </motion.g>

        {/* Pulsing center ring */}
        <motion.circle cx={260} cy={260} r={110} fill="none" stroke={stroke} strokeWidth="3" filter="url(#glow)" animate={paused ? undefined : { opacity: [0.25, mode === "speaking" ? 1 : 0.8, 0.25] }} transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: 2.0, ease: "easeInOut" }} />

        {/* Center core – scales with volume */}
        <motion.circle cx={260} cy={260} r={70} fill={mode === "idle" ? "#0BC2E6" : mode === "thinking" ? "#64E8FF" : "#12D9FF"} style={{ originX: 0.5, originY: 0.5 }} animate={paused ? { scale: 1 } : { scale: 1 * pulseScale }} transition={paused ? { type: "spring", stiffness: 100, damping: 20, duration: 0 } : { type: "spring", stiffness: 100, damping: 20 }} opacity={0.18} />

        {/* Micro text ring */}
        <g opacity={0.7}>
          {Array.from({ length: 28 }).map((_, i) => (
            <SmallTick key={i} cx={260} cy={260} r={250} angle={i * (360 / 28)} />
          ))}
        </g>

        {/* Label */}
        <motion.text x={260} y={268} textAnchor="middle" fontFamily="ui-sans-serif, system-ui, -apple-system" fontSize="28" letterSpacing="6" fill="#CFF8FF" style={{ filter: "url(#glow)" }} animate={paused ? undefined : { opacity: [0.9, 0.65, 0.9] }} transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: 3, ease: "easeInOut" }}>{label}</motion.text>

        {/* Inner small readout dots */}
        <motion.g style={{ originX: 0.5, originY: 0.5 }} animate={paused ? { rotate: 0 } : { rotate: -360 }} transition={paused ? { repeat: 0, duration: 0 } : { repeat: Infinity, duration: counterSpeed + 6, ease: "linear" }}>
          {Array.from({ length: 32 }).map((_, i) => (
            <circle key={i} cx={260 + Math.cos((Math.PI / 16) * i) * 95} cy={260 + Math.sin((Math.PI / 16) * i) * 95} r={2.2} fill={stroke} opacity={mode === "speaking" ? 1 : 0.8} />
          ))}
        </motion.g>
      </svg>
    </div>
  );
}

// helpers
function polarToCartesian(cx: number, cy: number, r: number, angleDeg: number) {
  const a = ((angleDeg - 90) * Math.PI) / 180.0;
  return { x: cx + r * Math.cos(a), y: cy + r * Math.sin(a) };
}

function arcD(cx: number, cy: number, r: number, start: number, sweep: number) {
  const startPt = polarToCartesian(cx, cy, r, start);
  const endPt = polarToCartesian(cx, cy, r, start + sweep);
  const largeArcFlag = sweep <= 180 ? 0 : 1;
  return `M ${startPt.x} ${startPt.y} A ${r} ${r} 0 ${largeArcFlag} 1 ${endPt.x} ${endPt.y}`;
}

function Arc({ cx, cy, r, start, sweep, stroke, width = 4, opacity = 1 }: { cx: number; cy: number; r: number; start: number; sweep: number; stroke: string; width?: number; opacity?: number; }) {
  return <path d={arcD(cx, cy, r, start, sweep)} fill="none" stroke={stroke} strokeWidth={width} strokeLinecap="round" opacity={opacity} />;
}

function SmallTick({ cx, cy, r, angle }: { cx: number; cy: number; r: number; angle: number; }) {
  const inner = r - 8;
  const p1 = polarToCartesian(cx, cy, inner, angle);
  const p2 = polarToCartesian(cx, cy, r, angle);
  return <line x1={p1.x} y1={p1.y} x2={p2.x} y2={p2.y} stroke="#0BC2E6" strokeWidth="2" opacity="0.35" />;
}