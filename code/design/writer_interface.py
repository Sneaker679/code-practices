class Writer(ABC):
    @abstractmethod
    def write(self, results): ...

class CsvWriter(Writer):
    def __init__(self, path):
        self.path = path

    def write(self, results):
        np.savetxt(self.path, results)

class ConsoleWriter(Writer):
    def write(self, results):
        print(results)
