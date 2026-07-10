class PeerReviewEngine:
    """
    Simulates rigorous double-blind peer-review comments and scoring.
    """
    def __init__(self):
        self.reviews = []

    def submit_review(self, paper_title: str, reviewer_id: str, scores: dict, comments: str):
        self.reviews.append({
            "paper": paper_title,
            "reviewer": reviewer_id,
            "scores": scores,
            "comments": comments,
            "decision": "ACCEPT" if sum(scores.values()) / len(scores) >= 0.85 else "REVISE"
        })
