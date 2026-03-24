"use client";

import React, { useMemo } from 'react';
import { AreaClosed, LinePath } from '@visx/shape';
import { curveMonotoneX } from '@visx/curve';
import { scaleTime, scaleLinear } from '@visx/scale';
import { LinearGradient } from '@visx/gradient';
import { ParentSize } from '@visx/responsive';

// Mock data generation
const generateData = (pts: number) => {
  const now = Date.now();
  return Array.from({ length: pts }).map((_, i) => ({
    date: new Date(now - (pts - i) * 60000), // per minute
    value: 30 + Math.random() * 40 + Math.sin(i / 5) * 20,
  }));
};

type DataPoint = {
  date: Date;
  value: number;
};

const getDate = (d: DataPoint) => d.date.valueOf();
const getValue = (d: DataPoint) => d.value;

export default function ThreatLevelChart() {
  const data = useMemo(() => generateData(60), []);

  return (
    <div className="w-full h-full min-h-[200px] relative">
      <ParentSize>
        {({ width, height }) => {
          if (width < 10 || height < 10) return null;

          const margin = { top: 10, right: 0, bottom: 0, left: 0 };
          const innerWidth = width - margin.left - margin.right;
          const innerHeight = height - margin.top - margin.bottom;

          const xScale = scaleTime({
            range: [0, innerWidth],
            domain: [Math.min(...data.map(getDate)), Math.max(...data.map(getDate))],
          });

          const yScale = scaleLinear({
            range: [innerHeight, 0],
            domain: [0, Math.max(...data.map(getValue)) + 20],
            nice: true,
          });

          return (
            <svg width={width} height={height}>
              <LinearGradient id="area-gradient" from="#00f0ff" to="#00f0ff" fromOpacity={0.4} toOpacity={0.0} />
              
              <AreaClosed<DataPoint>
                data={data}
                x={d => xScale(getDate(d)) ?? 0}
                y={d => yScale(getValue(d)) ?? 0}
                yScale={yScale}
                strokeWidth={1}
                stroke="url(#area-gradient)"
                fill="url(#area-gradient)"
                curve={curveMonotoneX}
              />
              
              <LinePath<DataPoint>
                data={data}
                x={d => xScale(getDate(d)) ?? 0}
                y={d => yScale(getValue(d)) ?? 0}
                stroke="#00f0ff"
                strokeWidth={2}
                curve={curveMonotoneX}
                style={{
                  filter: 'drop-shadow(0 0 4px rgba(0, 240, 255, 0.8))',
                }}
              />
              
              {/* Optional Grid Lines */}
              {Array.from({ length: 4 }).map((_, i) => (
                <line
                  key={i}
                  x1={0}
                  x2={width}
                  y1={innerHeight * (i / 4)}
                  y2={innerHeight * (i / 4)}
                  stroke="rgba(255,255,255,0.05)"
                  strokeDasharray="4,4"
                />
              ))}
            </svg>
          );
        }}
      </ParentSize>
    </div>
  );
}