class Body:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

body = Body(1, 5)
momentum = body.mass * body.velocity
