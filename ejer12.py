frase=str(input("ingrese una frase:  "))
l=str(input("ingrese una letra"))
cn= 0
for i in frase:
    if i == l:
        cn+=1
print(f"la {l} aparece {cn} veces en la palabra {frase}")