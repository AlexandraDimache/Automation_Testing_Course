# Operatori de asignare

x = 3 # Asignare = stocarea unei valori la o adresa de memorie
print(x)
x = x + 3 # Crestem valoarea lui x cu 3
print(x)
x += 3  # Forma mai scurta de la linia 5, X-ul devine 6
print(x)

# Operatori aritmetici

print(10%3) # restul impartirii din 10/3

print(2**3) # ridicare la puterea a 3

# Operatori de comparare

x = 5
y = 3

print(x==y) # operator de comparatie ==
            # operator de atribuire =

print(x!=y) # verifica daca valorile variabilelor sunt diferite, opus de ==

print(x<y)
print(x<=y)
print(x>y)
print(x>=y)

# Operatori logici sunt : and, or, not
# Intotdeauna operatorul and are prioritate in fata operatorului or

print( x<2 and x<y) # ambele conditii trebuie sa fie true pentru a avea toata conditia evaluata

print(x>2 and x<y)
print(x>2 and x<2 or y>2)
print(x>2 or x<y and y>2)
print(x>2 and (x<y or y>2))
'''
pasaport = input('Introduceti validarea pasaportului: Da/ Nu')
parintii = input('Are ambii parinti? Da/ Nu')
permisiune = input('Are persiunea acestora? Da/Nu')
if pasaport == 'Da' and parintii == 'Da' or permisiune == 'Da':
    print('Permite calatoria')
else:
    print('Nu permite calatoria')
'''
NOTA_TRECERE = 5
NOTA_TRECERE_PURTARE = 7
nota_examen = int(input('Introdu nota la examen: '))
nota_purtare = int(input('Introdu nota la purtare: '))

if nota_examen >= NOTA_TRECERE and nota_purtare >= NOTA_TRECERE_PURTARE :
    print('Felicitari, ai trecut! ')
    if nota_examen == 10 and nota_purtare == 10:
        print('Felicitari, esti premiant!')
else:
    print('Nu ai trecut clasa :(')

