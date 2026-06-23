from sarita_runtime.kernel.scientific_autonomy.recursive_convergence_engine import RecursiveConvergenceEngine

def run_demo():
    engine = RecursiveConvergenceEngine()
    # Trajectory of an audit metric converging to 0.95
    trajectory = [0.8, 0.9, 0.94, 0.949, 0.9499, 0.95, 0.95]

    print(f"Evaluating recursive convergence for trajectory: {trajectory}")
    eval = engine.evaluate_convergence(trajectory)

    print(f"Converged: {eval['converged']}")
    print(f"Oscillating: {eval['oscillating']}")
    print(f"Equilibrium: {eval['equilibrium_point']:.4f}")
    print(f"Certified: {eval['certified']}")

if __name__ == "__main__":
    run_demo()
