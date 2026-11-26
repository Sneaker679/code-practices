from abc import ABC, abstractmethod


class Force(ABC):  # the contract
    @abstractmethod
    def force(self, body): ...


class Gravity(Force):  # fulfils it
    def force(self, body):
        return -9.81 * body.mass
