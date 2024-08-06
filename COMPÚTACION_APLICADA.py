montoT = float(input("Ingresa el monto T invertido (Q): "))
interesT = float(input("Ingresa el interés T ganado anualmente (Q)): "))
interesB = float(input("Ingresa el interés anual de la cuenta Banrural): "))
interesBI = float(input("Ingresa el interés anual de la cuenta de Banco Industrial): "))

interesB /= 100
interesBI /= 100

a1, b1, c1 = 1, 1, montoT
a2, b2, c2 = interesB, interesBI, interesT
a1_prime, b1_prime, c1_prime = a1 * interesB, b1 * interesB, c1 * interesB
a3, b3, c3 = a2 - a1_prime, b2 - b1_prime, c2 - c1_prime
y = c3 / b3
x = c1 - y

print(f'La inversion en la cuenta Banrural es de: Q{x:.2f}')
print(f'La inversion en la cuenta del BI es de: Q{y:.2f}')