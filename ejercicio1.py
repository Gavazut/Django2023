

def mcd():
    potencia= 1
    dividendo_str= input("Inserte el primer número: ")
    dividendo = int(dividendo_str)
    divisor_str= input("Inserte el segundo número: ")
    divisor= int(divisor_str)
    try:
         dividendo//divisor
    except ZeroDivisionError:
         print("Disculpe, no se puede dividir entre cero")
         
    if dividendo == divisor:
         print("El Máximo común divisor es: ", divisor)
    elif dividendo//divisor >0:
        cociente= dividendo//divisor
        potencia +=1
        cociente= cociente//divisor
        print("El máximo común divisor es: ", cociente**potencia)
    elif  dividendo// divisor < 1:
          print("El máximo común divisor es decimal")
    else: 
         print("Por favor ingrese dos números válidos")

resultado= mcd()

