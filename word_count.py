import sys

if len(sys.argv) != 2:
    print("(El comando necesita un argumento) python archivo.py 'lorem_ipsum.txt'")
    sys.exit(1)


archivo = sys.argv[1]

#leer el archivo

with open(archivo, "r", encoding = "utf-8") as f:
    texto = f.read()

total_letras = texto
total_palabras = texto.split()

distintos = set(total_letras)
palabras_distintas = set(total_palabras)

print(f"El número de caracteres distintos es: {len(distintos)}")
print(f"El número de palabras distinas es : {len(palabras_distintas)}")