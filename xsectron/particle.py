class Particle:
    @property
    def charge(self):
        return self._charge

    @charge.setter
    def charge(self, value):
        self._charge = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = value

    @property
    def spin(self):
        return self._spin

    @spin.setter
    def spin(self, value):
        self._spin = value

    @property
    def isospin(self):
        return self._isospin

    @isospin.setter
    def isospin(self, value):
        self._isospin = value
