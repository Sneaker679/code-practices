class Body:                                  # the blueprint
    def __init__(self, mass, velocity):      # runs when an object is created
        self.mass = mass                     # attributes: the object's data
        self.velocity = velocity

    def kinetic_energy(self):                # method: behaviour from data
        return 0.5 * self.mass * self.velocity**2

electron = Body(9.11e-31, 2.0e6)             # objects: instances of the class
proton = Body(1.67e-27, 2.0e6)
print(electron.kinetic_energy())             # 1.822e-18 (J)
