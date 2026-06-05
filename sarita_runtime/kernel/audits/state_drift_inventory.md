# State Drift Inventory (Phase 78.1)

This document tracks identified state variables that are prone to drifting during replay or restart scenarios.

## 1. Material Runqueue
* **Variable:** `UnifiedExecutionGraph.material_runqueue`
* **Source of Drift:** Replay populates this queue. If the replayed system attempts to "execute" these tasks, they might be popped and removed, while the original system might have kept them until completion.
* **Resolution:** Replay mode should distinguish between rehydrating the queue and authorizing new work.

## 2. Completed Tasks Set
* **Variable:** `UnifiedExecutionGraph.completed_tasks`
* **Source of Drift:** If an `EXECUTION_COMPLETE` event is missing from the ledger, the replayed state will think a task is still running.

## 3. Global Pressure Score
* **Variable:** `UnifiedExecutionGraph.global_pressure`
* **Source of Drift:** Floating point precision and the timing of `PRESSURE_UPDATE` events relative to other decisions.

## 4. Resource Ownership Map
* **Variable:** `UnifiedExecutionGraph.ownership`
* **Source of Drift:** Non-atomic updates or out-of-order events if the single writer queue is bypassed (though bypassed is currently prohibited).

## 5. Active Epoch
* **Variable:** `UnifiedExecutionGraph.active_epoch`
* **Source of Drift:** Manual epoch advances vs. automated triggers.
