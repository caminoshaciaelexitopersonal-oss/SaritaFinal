# Thread Lifecycle Report (Phase 78.4)

## 1. UnifiedExecutionGraph
* **Thread Name:** `GraphEventProcessor`
* **Purpose:** Process events from the `_event_queue` and maintain the graph state/ledger.
* **Management:** Uses `_running` flag and a `None` sentinel in the queue.
* **Shutdown:** `shutdown()` method joins the thread cleanly.

## 2. SovereignScheduler
* **Thread Name:** `SchedulerDispatch`
* **Purpose:** Poll the `UnifiedExecutionGraph` for authorized tasks and execute them.
* **Management:** Uses `is_running` flag.
* **Shutdown:** `shutdown()` method stops the loop and joins the thread.

## 3. RuntimeReplayEngine
* **Context:** Creates a temporary `UnifiedExecutionGraph` instance.
* **Risk:** If `replayed_graph` is not shut down, its `GraphEventProcessor` thread will linger.
* **Fix Required:** Replay Engine should call `replayed_graph.shutdown()` after reconstruction is finished or the caller should manage it.

## 4. Other Threads
* **io_uring threads:** Managed by the OS/Kernel via `io_uring` syscalls.
* **eBPF telemetry:** Async tracepipe streaming (to be audited).
