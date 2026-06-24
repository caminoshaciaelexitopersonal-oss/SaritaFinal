class EpochCreator:
    def __init__(self):
        self.epochs = []

    def declare_epoch(self, name, start_step, characteristic):
        epoch = {
            "name": name,
            "start_step": start_step,
            "characteristic": characteristic
        }
        self.epochs.append(epoch)
        return epoch

    def get_current_epoch(self, current_step):
        for epoch in reversed(self.epochs):
            if current_step >= epoch["start_step"]:
                return epoch
        return None
