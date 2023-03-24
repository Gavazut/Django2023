cadena="Hola"
capadepenapa= cadena

for i, c in enumerate(cadena):
    if c in "aeiou":
        capadepenapa[i]= c + "p" + c
    else:
          capadepenapa[i] = c #

