class Experiment:
    def __init__(self):
        self.writer = CsvWriter("out.csv")

    def run(self, data):
        results = analyse(data)
        self.writer.write(results)
