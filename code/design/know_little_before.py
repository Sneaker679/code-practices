class System:
    def drag_force(self, body):
        rho = self.planet.air.density
        v = body.velocity
        return -0.5 * rho * v**2
