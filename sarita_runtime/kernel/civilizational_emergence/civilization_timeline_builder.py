class CivilizationTimelineBuilder:
    def __init__(self):
        self.timeline = []

    def add_milestone(self, event):
        self.timeline.append(event)

    def get_timeline(self):
        return self.timeline
