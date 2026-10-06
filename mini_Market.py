import random

market_Name = input("Market adını gir: ")

product1 = input("1. ürünün adını gir: ")
price1 = float(input("ücreti gir: "))
amount1 = int(input("adeti gir "))

product2 = input("2. ürünün adını gir: ")
price2 = float(input("ücreti gir: "))
amount2 = int(input("adeti gir "))

product3 = input("3. ürünün adını gir: ")
price3 = float(input("ücreti gir: "))
amount3 = int(input("adeti gir "))

total1 = price1*amount1
total2 = price2*amount2
total3 = price3*amount3

total_Price = total1+total2+total3

money = float(input("Müşetrinin verdiği ücreti gir: "))

change = money - total_Price

receipt_number = random.randint(1000,9999)

print("\n=========================")
print(market_Name)
print("Fiş No: ",receipt_number)
print("=========================")

print(product1, "-", amount1, "Adet",total1, "TL")
print(product2, "-", amount2, "Adet",total2, "TL")
print(product3, "-", amount3, "Adet",total3, "TL")

print("GENEL TOPLAM:", total_Price, "TL")
print("ALINAN PARA:", money, "TL")
print("PARA ÜSTÜ: ", change, "TL")

print("=========================")
print("TEŞEKKÜR EDERİZ")





