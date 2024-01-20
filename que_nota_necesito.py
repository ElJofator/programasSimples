#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.
s1 = input("Ingrese nota certamen 1: ")
s2 = input("Ingrese nota certamen 2: ")
s3 = input("Ingrese nota laboratorio: ")
if(s1.isnumeric() and s2.isnumeric() and s3.isnumeric()):
    c1 = int(s1)
    c2 = int(s2)
    nl = int(s3)
    nf = 60 #Nota necesaria para aprobar
    #nc = (nf - 0.3nl)/0.7
    #(c1+c2+c3)/3 = (nf - 0.3nl)/0.7
    #c3 = 30nf/7 - 9nl/7 - c1 - c2
    c3 = (30*nf - 9*nl)/7 - c1 - c2
    entero = int(c3)
    if(entero < c3):
        entero += 1
    print(f"Necesita nota {entero} en el certamen 3")