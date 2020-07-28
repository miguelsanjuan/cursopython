texto = "Repaso de python"
year = 2020
numero = 35

#imprimir
print(f"{texto} - {str(year)} - {str(numero)}")
print(texto + " - " + str(year) + " - " + str(numero))

#entrada de datos
sitioweb = input("¿Cual es tu pagina web?: ")
print("El sitio se llama: " + sitioweb)

#condiciones
"""
altura = int(input("¿Cual es tu altura?: "))
if altura >= 180:
    print("Eres alto")
else:
    print("Eres bajo")
"""
#funcion
var_altura = int(input("¿Cual es tu altura?: "))

def mostrarAltura(altura):
    resultado = ""
    
    if altura >= 180:
        resultado = "Eres alto"
    else:
        resultado = "Eres bajo"

    return resultado

print(mostrarAltura(var_altura))
mostrarAltura(var_altura)
mostrarAltura(var_altura)
print(type(year))

chicas = "nunca te voy dejar de recordar cuando te mirabaim"

print(chicas)

print("Sofia \n todavia te quiero")