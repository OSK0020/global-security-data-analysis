"use client";

import { motion } from "framer-motion";
import { Activity, Globe, Lock, Cpu, Database, Eye } from "lucide-react";
import ThreatLevelChart from "@/components/ThreatLevelChart";
import SecurityAlert from "@/components/SecurityAlert";

export default function Home() {
  const containerVariants = {
    hidden: { opacity: 0 },
    show: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 20 },
    show: { opacity: 1, y: 0, transition: { type: "spring" as const, stiffness: 50 } },
  };

  return (
    <div className="w-full max-w-[1600px] mx-auto h-[calc(100vh-4rem)] flex flex-col relative">
      <SecurityAlert />

      {/* Header */}
      <header className="flex items-center justify-between border-b border-tactical-cyan/20 pb-4 mb-6">
        <div className="flex items-center gap-4">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ duration: 20, repeat: Infinity, ease: "linear" }}
            className="text-tactical-cyan"
          >
            <Globe size={32} strokeWidth={1} />
          </motion.div>
          <div>
            <h1 className="text-2xl font-bold tracking-[0.2em] text-tactical-cyan uppercase">Global Intelligence Node</h1>
            <p className="text-xs font-mono text-tactical-cyan/60 tracking-widest">SYS_STATUS: OPTIMAL | ENCRYPTION: 256-BIT SECURE</p>
          </div>
        </div>
        <div className="flex items-center gap-6 font-mono text-sm hidden md:flex">
          <div className="flex items-center gap-2 text-tactical-cyan/80">
            <Cpu size={16} />
            <span>CPU: 42%</span>
          </div>
          <div className="flex items-center gap-2 text-tactical-cyan/80">
            <Database size={16} />
            <span>MEM: 68%</span>
          </div>
          <div className="flex items-center gap-2 text-alert-crimson">
            <span className="w-2 h-2 rounded-full bg-alert-crimson animate-pulse-glow" />
            <span>LIVE</span>
          </div>
        </div>
      </header>

      {/* Main Grid */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="show"
        className="flex-1 grid grid-cols-1 md:grid-cols-4 grid-rows-6 gap-6 h-full min-h-[600px]"
      >
        {/* Main Threat Chart - Spans 3 cols, 4 rows */}
        <motion.div
          variants={itemVariants}
          className="col-span-1 md:col-span-3 row-span-4 relative border border-tactical-cyan/30 bg-tactical-cyan/5 backdrop-blur-sm p-4 flex flex-col"
        >
          {/* Corner accents */}
          <div className="absolute top-0 left-0 w-3 h-3 border-t-2 border-l-2 border-tactical-cyan" />
          <div className="absolute top-0 right-0 w-3 h-3 border-t-2 border-r-2 border-tactical-cyan" />
          <div className="absolute bottom-0 left-0 w-3 h-3 border-b-2 border-l-2 border-tactical-cyan" />
          <div className="absolute bottom-0 right-0 w-3 h-3 border-b-2 border-r-2 border-tactical-cyan" />

          <div className="flex items-center justify-between mb-4">
            <h2 className="font-mono text-tactical-cyan uppercase tracking-wider text-sm flex items-center gap-2">
              <Activity size={16} /> Live Threat Telemetry
            </h2>
            <span className="font-mono text-xs text-tactical-cyan/50">UPDATING...</span>
          </div>
          
          <div className="flex-1 w-full relative">
            <ThreatLevelChart />
          </div>
        </motion.div>

        {/* Status Panel - 1 col, 2 rows */}
        <motion.div
          variants={itemVariants}
          className="col-span-1 row-span-2 border border-tactical-cyan/20 bg-black/40 p-4 flex flex-col justify-between"
        >
          <h2 className="font-mono text-tactical-cyan/70 uppercase tracking-wider text-xs border-b border-tactical-cyan/20 pb-2 mb-4">System Integrity</h2>
          
          <div className="space-y-4">
            <div>
              <div className="flex justify-between font-mono text-xs text-gray-400 mb-1">
                <span>Firewall</span>
                <span className="text-tactical-cyan">ACTIVE</span>
              </div>
              <div className="h-1 w-full bg-gray-900 rounded-full overflow-hidden">
                <div className="h-full bg-tactical-cyan w-full shadow-neon-cyan" />
              </div>
            </div>
            
            <div>
              <div className="flex justify-between font-mono text-xs text-gray-400 mb-1">
                <span>Intrusion Detection</span>
                <span className="text-encrypted-amber">ELEVATED</span>
              </div>
              <div className="h-1 w-full bg-gray-900 rounded-full overflow-hidden">
                <div className="h-full bg-encrypted-amber w-[75%] shadow-neon-amber" />
              </div>
            </div>

            <div>
              <div className="flex justify-between font-mono text-xs text-gray-400 mb-1">
                <span>Sector 7 Shield</span>
                <span className="text-alert-crimson animate-pulse">COMPROMISED</span>
              </div>
              <div className="h-1 w-full bg-gray-900 rounded-full overflow-hidden">
                <div className="h-full bg-alert-crimson w-[30%] shadow-neon-crimson" />
              </div>
            </div>
          </div>
        </motion.div>

        {/* Recent Events Log - 1 col, 4 rows */}
        <motion.div
          variants={itemVariants}
          className="col-span-1 row-span-4 border border-tactical-cyan/20 bg-black/40 p-4 overflow-hidden flex flex-col"
        >
          <h2 className="font-mono text-tactical-cyan/70 uppercase tracking-wider text-xs border-b border-tactical-cyan/20 pb-2 mb-4 flex items-center gap-2">
            <Eye size={14} /> Security Logs
          </h2>
          <div className="flex-1 overflow-y-auto space-y-3 pr-2 [&::-webkit-scrollbar-thumb]:bg-tactical-cyan/50 hover:[&::-webkit-scrollbar-thumb]:bg-tactical-cyan">
            {[
              { time: "14:02:45", type: "CRITICAL", msg: "Unauthorized access in DB_NODE_04", color: "text-alert-crimson" },
              { time: "14:01:12", type: "WARN", msg: "Multiple failed auth attempts from IP 192.168.1.104", color: "text-encrypted-amber" },
              { time: "13:58:30", type: "INFO", msg: "Automated scan completed. No threats found.", color: "text-tactical-cyan" },
              { time: "13:50:05", type: "INFO", msg: "System backup initiated to secure storage.", color: "text-tactical-cyan" },
              { time: "13:45:22", type: "WARN", msg: "High traffic spike detected on API Gateway.", color: "text-encrypted-amber" },
              { time: "13:30:00", type: "INFO", msg: "Shift handover log recorded.", color: "text-gray-400" },
              { time: "13:15:10", type: "INFO", msg: "Node 7 connection established.", color: "text-tactical-cyan" },
            ].map((log, i) => (
              <div key={i} className="font-mono text-xs">
                <div className="flex justify-between opacity-50 mb-0.5">
                  <span>[{log.time}]</span>
                  <span>[{log.type}]</span>
                </div>
                <div className={`${log.color} break-words leading-relaxed`}>
                  &gt; {log.msg}
                </div>
              </div>
            ))}
          </div>
        </motion.div>

        {/* Data Stream / Terminal - 3 cols, 2 rows */}
        <motion.div
          variants={itemVariants}
          className="col-span-1 md:col-span-3 row-span-2 border border-tactical-cyan/20 bg-black/60 p-4 relative overflow-hidden group hidden md:block"
        >
          <div className="absolute inset-0 bg-tactical-cyan/5 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none" />
          
          <div className="flex items-center gap-2 mb-2 font-mono text-tactical-cyan/70 text-xs">
            <Lock size={14} />
            <span>ENCRYPTED DATA STREAM</span>
          </div>

          <div className="font-mono text-xs text-tactical-cyan/50 leading-relaxed overflow-hidden h-full">
            {/* Simulated hex dump / terminal output */}
            <p className="animate-pulse">0x0000 48 65 6C 6C 6F 20 57 6F 72 6C 64 21 0A 00 00 00  Hello World!....</p>
            <p className="opacity-80">0x0010 53 79 73 74 65 6D 20 49 6E 69 74 69 61 6C 69 7A  System Initializ</p>
            <p className="opacity-60">0x0020 65 64 2E 2E 2E 0A 4C 6F 61 64 69 6E 67 20 6D 6F  ed....Loading mo</p>
            <p className="opacity-40">0x0030 64 75 6C 65 73 3A 20 4F 4B 0A 43 68 65 63 6B 69  dules: OK.Checki</p>
            <p className="opacity-20">0x0040 6E 67 20 6E 65 74 77 6F 72 6B 20 6E 6F 64 65 73  ng network nodes</p>
            <p className="text-tactical-cyan animate-pulse mt-2">&gt; Awaiting command input_</p>
          </div>
        </motion.div>
      </motion.div>
    </div>
  );
}