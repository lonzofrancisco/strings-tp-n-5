string = input("Ingrese un texto..  ")



lenght = (len(string))
print("texto ingresado: " + string)

print("La cadena tiene "+ str(lenght) + " caracteres!") 

print("su texto en mayus: "+ string.upper())
mayus = string.capitalize()

if string.find("la") > -1:
    print("existe 'la' en tu texto")
print(string.capitalize())