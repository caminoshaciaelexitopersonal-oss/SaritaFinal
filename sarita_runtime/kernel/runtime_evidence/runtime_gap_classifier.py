import logging

class GapClassifier:
    def classify_gaps(self, checklist):
        report = {}
        for item, status in checklist.items():
            if status:
                report[item] = "REAL"
            else:
                report[item] = "NOT_IMPLEMENTED"
        return report
