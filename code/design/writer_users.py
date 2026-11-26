class FakeWriter(Writer):
    def __init__(self):
        self.written = []

    def write(self, results):
        self.written.append(results)

class Experiment:
    def __init__(self, writer: Writer):
        self.writer: Writer = writer

    def run(self, data):
        self.writer.write(analyse(data))
