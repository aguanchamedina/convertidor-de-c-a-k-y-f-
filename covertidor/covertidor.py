from tkinter import mainloop

print("-----------------------------------")
print("------------CONVERTIDOR------------")
print("-----------------------------------")

#INPUT
X = int(input("Digite la cantidad de °C a convertir: "))

#PROCESS
grados_kelvin = X + 273.15
grados_Fahrenheit = ( X * 9/5) + 32 

#OUTPUT
print("---------RESULTADO-----------")
print("La cantidad de °C a su equivalente °k es: " + str(grados_kelvin))
print("La cantidad de °C a su equivalente °F es: " + str(grados_Fahrenheit))
print("Gracias por usar el convertidor :) ")

mainloop