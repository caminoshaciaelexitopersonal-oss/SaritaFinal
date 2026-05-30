import logging

class DeterministicSubmissionQueue:
    """
    Manages deterministic submission of IO requests to the ring.
    """
    def __init__(self, engine):
        self.engine = engine

    async def submit_ordered_bundle(self, bundle: list):
        logging.info(f"SQ Authority: Submitting ordered bundle of {len(bundle)} requests.")
        for req in bundle:
            await self.engine.submit_io_request(req['op'], req['fd'], req['buf'])
        return True
