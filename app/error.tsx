"use client";

import { useEffect } from "react";
import { motion } from "framer-motion";
import { ServerCrash } from "lucide-react";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    // Log the error to an error reporting service
    console.error(error);
  }, [error]);

  return (
    <div className="flex flex-col items-center justify-center min-h-[80vh] w-full selection:bg-encrypted-amber/30 selection:text-encrypted-amber">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative flex flex-col items-start w-full max-w-3xl p-8 border border-encrypted-amber/40 bg-[#1a1400]/40 backdrop-blur-md shadow-neon-amber rounded-sm overflow-hidden"
      >
        <div className="absolute top-0 left-0 w-full h-1 bg-encrypted-amber animate-pulse-glow" />

        <div className="flex items-center gap-4 mb-6 text-encrypted-amber">
          <ServerCrash size={48} strokeWidth={1.5} />
          <div>
            <h2 className="text-2xl font-bold tracking-widest uppercase">System Critical Failure</h2>
            <p className="text-sm font-mono opacity-80">INTEGRITY COMPROMISED</p>
          </div>
        </div>

        <div className="w-full bg-black/60 border border-gray-800 p-4 mb-8 font-mono text-xs text-gray-400 overflow-x-auto">
          <p className="text-alert-crimson mb-2">&gt; ERROR_DUMP_START</p>
          <p className="whitespace-pre-wrap break-all opacity-80">{error.message || "Unknown fatal exception caught in Main Thread."}</p>
          {error.digest && <p className="mt-2 text-tactical-cyan">Digest: {error.digest}</p>}
          <p className="text-alert-crimson mt-2">&gt; ERROR_DUMP_END</p>
        </div>

        <div className="flex gap-4 w-full justify-end">
          <motion.button
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            onClick={() => reset()}
            className="px-6 py-2 bg-encrypted-amber/10 border border-encrypted-amber text-encrypted-amber font-mono uppercase tracking-wider hover:bg-encrypted-amber/20 hover:shadow-neon-amber transition-all duration-300"
          >
            Attempt Override & Restart
          </motion.button>
        </div>
      </motion.div>
    </div>
  );
}