"use client";

import { motion } from "framer-motion";
import { AlertCircle, ShieldAlert, X } from "lucide-react";
import { useState } from "react";

export default function SecurityAlert() {
  const [isVisible, setIsVisible] = useState(true);

  if (!isVisible) return null;

  return (
    <motion.div
      initial={{ x: "100%", opacity: 0 }}
      animate={{ x: 0, opacity: 1 }}
      exit={{ x: "100%", opacity: 0 }}
      transition={{ type: "spring", stiffness: 100, damping: 15 }}
      className="absolute top-6 right-6 z-50 w-96"
    >
      <div className="relative flex flex-col p-4 bg-alert-crimson/10 border border-alert-crimson backdrop-blur-md shadow-neon-crimson rounded-sm overflow-hidden">
        {/* Animated Background Pulse */}
        <div className="absolute inset-0 bg-alert-crimson/5 animate-pulse-glow pointer-events-none" />

        {/* Scanline effect on the alert */}
        <div className="absolute inset-0 overflow-hidden pointer-events-none">
          <div className="w-full h-1 bg-alert-crimson/30 animate-scanline" style={{ animationDuration: '3s' }} />
        </div>

        <div className="relative z-10 flex items-start justify-between">
          <div className="flex items-center gap-3 text-alert-crimson">
            <motion.div
              animate={{ opacity: [1, 0.4, 1] }}
              transition={{ duration: 1, repeat: Infinity }}
            >
              <ShieldAlert size={24} />
            </motion.div>
            <h3 className="font-mono font-bold tracking-widest uppercase text-lg">Priority Alert</h3>
          </div>
          <button
            onClick={() => setIsVisible(false)}
            className="text-alert-crimson/70 hover:text-alert-crimson transition-colors"
          >
            <X size={20} />
          </button>
        </div>

        <div className="relative z-10 mt-3 text-sm font-mono text-gray-300">
          <p className="mb-1 text-alert-crimson">&gt; ANOMALY DETECTED IN SECTOR 7G</p>
          <p className="opacity-80">Unauthorized access attempt flagged. IP traced to unknown proxy network. Counter-measures deploying...</p>
        </div>

        <div className="relative z-10 mt-4 flex gap-2">
          <button className="flex-1 py-1.5 text-xs font-mono border border-alert-crimson/50 text-alert-crimson hover:bg-alert-crimson/20 transition-colors uppercase tracking-wider">
            View Details
          </button>
          <button className="flex-1 py-1.5 text-xs font-mono bg-alert-crimson/20 border border-alert-crimson text-alert-crimson hover:bg-alert-crimson hover:text-void transition-colors uppercase tracking-wider shadow-[0_0_10px_rgba(255,42,42,0.5)]">
            Initiate Lockdown
          </button>
        </div>
      </div>
    </motion.div>
  );
}