class MultiParadigmManager:
    def __init__(self):
        self.paradigms = {}

    def add_paradigm(self, paradigm):
        self.paradigms[paradigm["id"]] = paradigm

    def get_all(self):
        return self.paradigms
