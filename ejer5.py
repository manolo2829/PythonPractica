c=int(input("cantidad para invertir:  "))
inte=int(input("interes anual:  "))
years=int(input("cantidad de años que va a invertir:  "))
for i in range(years):
    c*=1+inte/100
    print(f"ganacias tras {i} años:  {round(c,2)}")
