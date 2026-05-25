import logging
import asyncio
import subprocess
import os

class RuntimePerfEventCollector:
    """
    Collects hardware and software performance events.
    Material implementation using the 'perf' command-line tool.
    """
    def __init__(self):
        pass

    async def collect_cpu_events(self, pid: int, duration_sec: int = 1):
        logging.info(f"Perf Collector: Collecting CPU events for PID {pid} for {duration_sec}s")

        try:
            cmd = [
                "perf", "stat", "-e", "cache-misses,cycles,instructions,context-switches",
                "-p", str(pid), "sleep", str(duration_sec)
            ]

            process = await asyncio.create_subprocess_exec(
                *cmd,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await process.communicate()

            metrics = self._parse_perf_output(stderr.decode())
            return metrics
        except Exception as e:
            logging.error(f"Perf Collector: Failed to collect events: {e}")
            return {"error": str(e)}

    def _parse_perf_output(self, output: str):
        metrics = {}
        for line in output.splitlines():
            if "cache-misses" in line:
                metrics["cache_misses"] = line.split()[0].replace(",", "")
            if "cycles" in line:
                metrics["cycles"] = line.split()[0].replace(",", "")
            if "instructions" in line:
                metrics["instructions"] = line.split()[0].replace(",", "")
            if "context-switches" in line:
                metrics["context_switches"] = line.split()[0].replace(",", "")
        return metrics
