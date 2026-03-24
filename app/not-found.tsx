"use client";

import { motion } from "framer-motion";
import Link from "next/link";
import { AlertTriangle } from "lucide-react";

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] w-full selection:bg-alert-crimson/30 selection:text-alert-crimson">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
        className="relative flex flex-col items-center max-w-2xl text-center p-12 border border-alert-crimson/30 bg-alert-crimson/5 backdrop-blur-md shadow-neon-crimson rounded-sm"
      >
        <div className="absolute top-0 left-0 w-2 h-2 border-t-2 border-l-2 border-alert-crimson" />
        <div className="absolute top-0 right-0 w-2 h-2 border-t-2 border-r-2 border-alert-crimson" />
        <div className="absolute bottom-0 left-0 w-2 h-2 border-b-2 border-l-2 border-alert-crimson" />
        <div className="absolute bottom-0 right-0 w-2 h-2 border-b-2 border-r-2 border-alert-crimson" />

        <motion.div
          animate={{ opacity: [1, 0.5, 1, 0, 1] }}
          transition={{ duration: 0.4, repeat: Infinity, repeatType: "mirror" }}
          className="mb-6 text-alert-crimson"
        >
          <AlertTriangle size={64} strokeWidth={1.5} />
        </motion.div>

        <motion.h1
          className="text-5xl font-bold tracking-widest text-alert-crimson mb-4 uppercase animate-glitch"
        >
          404: Signal Lost
        </motion.h1>

        <p className="text-gray-400 font-mono mb-8 max-w-lg leading-relaxed">
          &gt; ERROR_CODE: NO_NODE_FOUND
          <br />
          &gt; WARNING: Requested coordinates exist outside monitored sectors. Return to command center to prevent tracking loss.
        </p>

        <Link href="/">
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="px-8 py-3 bg-transparent border border-tactical-cyan text-tactical-cyan font-mono uppercase tracking-widest hover:bg-tactical-cyan/10 hover:shadow-neon-cyan transition-all duration-300 relative group overflow-hidden"
          >
            <span className="relative z-10">Re-establish Connection</span>
            <div className="absolute inset-0 bg-tactical-cyan/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300 ease-out" />
          </motion.button>
        </Link>
      </motion.div>
    </div>
  );
}