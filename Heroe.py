class Heroe:
    # declaro la funcion especial constructor , que se encarga de inicilizar mis atributos
    def __init__(self):
        #defino los atributos de mi clase, los atrbutos igual a variables
        self.nombre=None
        self.edad=None
        self.porderPatada=None
        self.poderPuño=None
        pass
    def saludar(self):
        print('soy un heroe')