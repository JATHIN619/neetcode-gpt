class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        if iterations == 0:
            return init  # untouched, preserves int type -> round() would too, but no need to call it
        x = init * (1 - 2 * learning_rate) ** iterations
        return round(x, 5)