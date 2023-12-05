class Peca:
    vertice = 0, 0
    multi = 0

    @property
    def x(self):
        return self.vertice[0]

    @property
    def y(self):
        return self.vertice[1]

    @property
    def w(self):
        return self.vertice[2]

    @property
    def h(self):
        return self.vertice[3]

    def __repr__(self) -> str:
        return f'<{self.vertice}>'

    def __eq__(self, __value: object) -> bool:
        a = self.multi
        b = __value.multi
        return a == b

    def __gt__(self, __value) -> bool:
        return self.multi > __value.multi

    def __lt__(self, __value) -> bool:
        return self.multi < __value.multi
