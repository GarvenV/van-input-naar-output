#Er wordt u een aantal relevante vragen gesteld...
#gelieve die naar eer en geweten in te vullen


input ("wat is je naam?")
dressuur = int(input("hoeveel jaal praktijkervaring heeft u met dieren-dressuur?"))
if dressuur>=4:
    jaar = input ("bent u in bezit van een mbo-4 ondernemen? ja/nee")
else:
    input ("helaas u voldoet niet aan de strenge eissen")    

if jaar == "ja":
    vrachtwagen = input ("in bezit van een geldig vrachtwagen rijbewijs? ja/nee")
    hoed = input("in bezit van een hoge hoed? ja/nee")   

else:
    print ("helaas u voldoet miet aan de strenge eissen.")
if hoed == "ja":
    snor=input ("is man en heeft snor breder dan 10cm of is vrouw en draagt rood krulhaar langer dan 20cm ja/nee")       
else: 
    print("helaas u voldoet niet aan de strenge eissen")
if snor == "ja":
    beschrijving=input ("geef een beschrijving")
    lengte=input("bent u langer dan 1 meter 50 (1.50) ja/nee")
if lengte == "ja":
    gewicht=int(input ("wat s uw lichaamsgewicht?"))
if gewicht <=90:
    print ("helaas u voldoet niet aan de strenge eissen")     
else:
    certificaat=input("heeft certificaat overleven met gevaarlijk personeel ja/nee")
    if certificaat == "ja":
        certificaat= "persoon heeft EHBO"

input ("waarom zijn de appel rood? press enter")
input ("dat is een neppe sollicitatie. grapje press enter")
input (" sorry dat ik u pest press enter")
input ("oke we gaan we door press enter")
input ("uw sollicitatie is met succes beeindigt stuur uw cv om aangenomen te worden")

