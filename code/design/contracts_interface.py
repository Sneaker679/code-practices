class Force(ABC):
    @abstractmethod
    def force(self, body): ...


class ConservativeForce(Force):
    @abstractmethod
    def potential(self, body): ...
