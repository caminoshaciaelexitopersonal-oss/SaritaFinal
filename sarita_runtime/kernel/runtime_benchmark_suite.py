import time

class RuntimeBenchmarkSuite:
    def measure_throughput(self, domain, total_ops, elapsed_time):
        tps = total_ops / elapsed_time
        print(f"Benchmark: {domain} Throughput = {tps:.2f} TPS")
        return tps

    def measure_rehydration_time(self, node_id, start_time):
        duration = time.time() - start_time
        print(f"Benchmark: Node {node_id} rehydrated in {duration:.2f}s")
        return duration

if __name__ == "__main__":
    suite = RuntimeBenchmarkSuite()
    suite.measure_throughput("FINANCE", 10000, 15.5)
