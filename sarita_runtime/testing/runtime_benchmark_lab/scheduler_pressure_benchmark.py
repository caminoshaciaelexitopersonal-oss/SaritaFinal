import asyncio
import logging
import time

class SchedulerPressureBenchmark:
    """
    Benchmarks scheduler jitter under heavy system load.
    """
    async def run_benchmark(self, duration_sec: int = 10):
        logging.info(f"Benchmark: Starting Scheduler Pressure test for {duration_sec}s")
        start_time = time.time()
        latencies = []

        while time.time() - start_time < duration_sec:
            t0 = time.perf_counter_ns()
            await asyncio.sleep(0.001) # Yield to scheduler
            t1 = time.perf_counter_ns()
            latencies.append((t1 - t0) / 1_000_000.0)

        avg_lat = sum(latencies) / len(latencies)
        max_lat = max(latencies)
        logging.info(f"Benchmark: Scheduler Jitter Results - Avg: {avg_lat:.4f}ms, Max: {max_lat:.4f}ms")
        return {"avg": avg_lat, "max": max_lat}

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(SchedulerPressureBenchmark().run_benchmark(5))
