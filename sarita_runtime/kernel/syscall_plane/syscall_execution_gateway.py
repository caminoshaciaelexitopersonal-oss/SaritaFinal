import logging
import ctypes
import os

class SyscallExecutionGateway:
    """
    Sovereign syscall gateway.
    Material enforcement with real syscall numbers and lineage recording.
    """
    def __init__(self, ledger):
        self.ledger = ledger
        self.libc = ctypes.CDLL('libc.so.6', use_errno=True)

    def material_syscall(self, syscall_nr: int, *args):
        """
        Executes a material syscall and records physical proof in the ledger.
        """
        logging.info(f"Syscall Gateway: MATERIALIZING Syscall {syscall_nr}")

        # Physical execution
        res = self.libc.syscall(syscall_nr, *args)

        # Immediate lineage registration (non-ceremonial)
        self.ledger.append_material_proof(
            task_id=f"SYS-{syscall_nr}-{os.getpid()}",
            epoch=0, # Current epoch should be passed
            evidence={"result": res, "args": [str(a) for a in args]},
            verdict="MATERIAL_EXECUTION_CERTIFIED"
        )

        return res
