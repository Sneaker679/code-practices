class Body:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

    def momentum(self):
        return self.mass * self.velocity

body = Body(1, 5)
momentum = body.momentum()
