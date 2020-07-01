#       “La letra '..' aparece .. veces en la cadena '...'”

string = input("ingrese una cadena de texto:  ")

char = input("ingrese el caracter a buscar:  ")
n= 0
for x in string:
    if x == char:
        n=n+1

print("La letra '"+char+"' aparece " + str(n) + " veces en la cadena: --> "+string)