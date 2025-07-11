N = int(input("ingrese le numero de intervalos: "))

intervalos= []

for _ in range(N):
    entrada = input("Ingresa el inicio y el fin del intervalo: ")
    li, ri = map(int, entrada.split())
    intervalos.append((li, ri))
intervalos.sort()

total = 0
inicio , fin = intervalos[0]

#quedamos medios



