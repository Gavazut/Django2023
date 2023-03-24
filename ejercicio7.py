from typing import Self


class Cuenta():
        titular= ""
        cantidad= 0


        def __init__(self, titular, cantidad):
            self.__titular= titular
            self.__cantidad= cantidad


        def mostrarDatos(self): 
            print(f"Bienvenido Sr. {self.__titular}, su saldo al día de hoy es {self.__cantidad}")
            return 
        
        @property
        def ingresarMonto(self, ingreso):
             if ingreso < (-1):
                  pass
             else:
                  cantidad= cantidad + ingreso

        @ingresarMonto.setter
        def saldoActual(self, cantidad_nueva):
             while cantidad_nueva > 0:
                  self.cantidad = cantidad_nueva
        
        @property
        def retirarMonto(self, retiro):
            while self.__cantidad > (-1000):
                cantidad= cantidad - retiro

        @retirarMonto.setter
        def debito(self, retiro_nuevo):
            if retiro_nuevo > self.cantidad and retiro_nuevo < (-1000):
                  self.cantidad= self.cantidad - retiro_nuevo
            elif retiro_nuevo > self.cantidad and retiro_nuevo >(-1000):
                    print("Saldo insuficiente")
            elif retiro_nuevo < self.cantidad:
                 self.cantidad= self.cantidad - retiro_nuevo
            else:
                 pass
                  



cadena="Hola"
capadepenapa= cadena

for i, c in enumerate(cadena):
     if c in "aeiou":
          capadepenapa[i]= c + "p" + c
     else:
          capadepenapa[i] = c
