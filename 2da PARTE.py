nombre=input("Por favor, ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))
while edad<18:
    print("Perdone, pero ustede tiene que tener o ser mayor de 18 años. Gracias por su visita")
    edad=int(input("Ingrese su edad: "))
print("Continuemos")

peso=float(input("Ingrese peso (kg): "))
talla=float(input("Ingrese talla (m): "))

def indiceMasaCorporal(peso,talla):
    IMC=peso/(talla**2)
    return IMC
