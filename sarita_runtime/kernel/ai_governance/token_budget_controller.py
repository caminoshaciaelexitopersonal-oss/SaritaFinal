import logging

class TokenBudgetController:
    def __init__(self, limit):
        self.limit = limit
        self.consumed = 0

    def check_budget(self, amount):
        if self.consumed + amount > self.limit:
            return False
        self.consumed += amount
        return True
