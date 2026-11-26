class Experiment:
    def __init__(self, writer):
        self.writer = writer

    def run(self, data):
        results = analyse(data)
        self.writer.write(results)

Experiment(CsvWriter("out.csv"))
Experiment(ConsoleWriter())
Experiment(FakeWriter())  # in tests
