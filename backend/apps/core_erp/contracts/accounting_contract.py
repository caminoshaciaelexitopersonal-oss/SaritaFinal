from abc import ABC, abstractmethod

class AccountingContract(ABC):
    """
    Contrato formal para servicios de contabilidad.
    """

    @abstractmethod
    def create_journal_entry(self, date, description, reference="", **kwargs):
        pass

    @abstractmethod
    def add_transaction(self, entry, account, debit=0, credit=0, description=""):
        pass

    @abstractmethod
    def post_entry(self, entry):
        pass
