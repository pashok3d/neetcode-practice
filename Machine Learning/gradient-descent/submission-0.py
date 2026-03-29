class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x = init
        for i in range(iterations):
            grad = 2*x
            x = x + learning_rate * -1 * grad
        return round(x, 5)