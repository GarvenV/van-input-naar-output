# pizza calculator
# small 5 euro
# medium 8 euro
# large 13 euro
print('_____________________________________')
print('pizza small           5$')
print('pizza medium          8$')
print('pizza large           13$')
print('_____________________________________')

pizzasmall=int(input("hoeveel pizza small wil je"))
pizzamedium=int(input("hoeveel pizza medium wil je"))
pizzalarge=int(input("hoeveel pizza large wil je"))
prijsSmall= (pizzasmall * 5)  
prijsMedium= (pizzamedium * 8)
prijsLarge= (pizzalarge * 13) 

print ("de prijs van uw pizza is dan" + str(prijsSmall + prijsMedium + prijsLarge) + "euro")