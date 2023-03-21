from ejercicio7 import Cuenta



class CuentaNueva(Cuenta):
       

       def __init__(self, titular, cantidad = 0, bonificacion= 0):
            super().__init__(titular, cantidad)
            self.bonificacion= bonificacion
        
       @property
       def bonificacion (self, bonificacion):
             return self.__bonificacion

       @bonificacion.setter
       def bonificacion(self,bonificacion):
             self.__bonificacion= bonificacion


       def titularValido(self):
        return self.titular.edad < 25 and self.titular.esMayordeEdad()
        

       def retirar(self, retiro_nuevo):
        if self.titular.edad and self.titular.esMayordeEdad() < 25:
             self.cantidad = self.cantidad - retiro_nuevo
        else:
             print("Titular no es mayor de edad.")

        def mostrar(self):
             print(f"Cuenta Jóven, Titular: {super().titular}, Saldo: {super().cantidad }, Bonificacion: {self.__bonificacion}"        )
