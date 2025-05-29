import sys

if len(sys.argv) != 5:
    print("python conversiones.py 'Sol Peruano' 'Pesos Argentino' 'Dolares Americano' 'Pesos Chilenos' ")
    sys.exit(1)


conversiones = {
    "Soles_Peruanos" : (float(sys.argv[1]) * float(sys.argv[-1])),
    "Pesos_Argentino" : (float(sys.argv[2]) * float(sys.argv[-1])),
    "Dolares_Americanos" : (float(sys.argv[3]) * float(sys.argv[-1]))
}

for k, v in conversiones.items():

    print(f"{sys.argv[-1]} pesos chilenos equivalen a:")
    print(k, v)
    