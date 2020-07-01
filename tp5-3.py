texto = input("ingrese un texto.. ")
x = texto.center(20,"*")
r = texto.rjust(20,"-")
l = texto.ljust(20,"#")

print(x)
print(r)
print(l)