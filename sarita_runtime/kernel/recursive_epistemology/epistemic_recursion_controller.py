class EpistemicRecursionController:
    def __init__(self, max_depth=10):
        self.max_depth = max_depth

    def control_recursion(self, current_depth):
        return current_depth < self.max_depth
