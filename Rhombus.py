pocetRadku = input("Kolik krát kolik chceš mít kosočtverec hvězd chceš?")

n = int(pocetRadku)

prvniRadek = list("*")

for i in range(n):
    print((n-i-1)*" " + (2*i+1)*"*" )

for i in range(n-1):
    print((i+1)*" " + (2*n-2*i-3) * "*")
