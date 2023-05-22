# Citim o gramatică și un număr n
with open('grammar.txt') as f:
    N = f.readline().split()  # neterminale
    T = f.readline().split()  # terminale
    P = int(f.readline())  # numărul de producții
    S = f.readline().strip()  # simbolul de start

    D = {}  # construim un dicționar pentru a stoca producțiile
    for i in range(P):
        productie = f.readline().strip()
        neterminal, derivari = productie.split(' -> ')
        derivari = derivari.split(' | ')

        if neterminal in D:
            D[neterminal].extend(derivari)
        else:
            D[neterminal] = derivari

# Păstrăm valorile subproblemelor rezolvate într-un dicționar în dicționar
R = {x: {} for x in N}

# Generăm cuvintele de lungime 0
for x in N:
    if '^' in D[x]:
        R[x][0] = ['']

# Citește n
n = int(input("n?"))

# Generăm cuvintele de lungime 1 până la n
for l in range(1, n + 1):
    for x in N:
        for prod in D[x]:
            terminale = True #verificam daca avem doar terminale in productie
            if prod[len(prod) - 1] in N: #verificam daca ultimul simbol e terminal
                terminale = False
            if prod == '^':
                prod = ''

            if terminale and len(prod) == l:
                if l in R[x]:
                    R[x][l].append(prod)
                else:
                    R[x][l] = [prod]
            elif not terminale:
                sim_term = prod[:-1]
                simbol_urm = prod[-1]
                lungime_ramasa = l - (len(prod) - 1)

                if lungime_ramasa in R[simbol_urm]:
                    if l not in R[x]:
                        R[x][l] = []
                    for cuv in R[simbol_urm][lungime_ramasa]:
                        R[x][l].append(sim_term + cuv)

# Afisam cuvintele generate de simbolul de start
if n not in R[S]:
    print("Nu exista cuvinte de lungime n")
else:
    if n != 0:
        print("Putem genera urmatoarele cuvinte de lungime", n)
        for cuv in R[S][n]:
            if cuv == '':
                print('^')
            else:
                print(cuv)
    else:
        print("Putem genera cuvantul vid: \n^")
