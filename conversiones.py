import sys

#Introducir valores:

# Sol peruano = 0.0046
# Peso Argentino = 0.093
# Dolar americano = 0.0013


if len(sys.argv) != 5:
    print("python conversiones.py 'Sol Peruano' 'Pesos Argentino' 'Dolares Americano' 'Pesos Chilenos' ")
    sys.exit(1)


conversiones = {
    "Soles Peruanos" : (float(sys.argv[1]) * float(sys.argv[-1])),
    "Pesos Argentino" : (float(sys.argv[2]) * float(sys.argv[-1])),
    "Dolares Americanos" : (float(sys.argv[3]) * float(sys.argv[-1]))
}

print(f"Los {sys.argv[-1]} pesos chilenos equivalen a:")

for k, v in conversiones.items():

    print(k, v)
    