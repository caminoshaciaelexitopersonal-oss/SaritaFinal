class BlockingEngine:
    """
    Groups experimental units into homogeneous blocks (e.g. by OS, hardware, memory limits) to control for nuisance variables.
    """
    def __init__(self):
        pass

    def assign_blocks(self, units: list, block_key_func) -> dict:
        blocks = {}
        for unit in units:
            key = block_key_func(unit)
            if key not in blocks:
                blocks[key] = []
            blocks[key].append(unit)
        return blocks
