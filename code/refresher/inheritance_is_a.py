class Body:                                  # the blueprint
    def __init__(self, mass, velocity):      # runs when an object is created
        self.mass = mass                     # attributes: the object's data
        self.velocity = velocity

    def kinetic_energy(self):                # method: behaviour from data
        return 0.5 * self.mass * self.velocity**2

class ChargedBody(Body):                     # a ChargedBody IS A Body
    def __init__(self, mass, velocity, charge):
        super().__init__(mass, velocity)     # reuse the parent's setup
        self.charge = charge                 # add what is new

    def force(self, field):                  # new behaviour
        return self.charge * field

electron = ChargedBody(9.11e-31, 2.0e6, -1.6e-19)
electron.kinetic_energy()                    # inherited from Body
