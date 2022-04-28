kaas_duur = 'emmenthaler'
kaas_nietduur = 'leerdammer'
steenja = 'pammigiano regiano'
steennee = 'goudse kaas'
korstja = 'camembert'
korstnee = 'mozzarella'
korst2ja = 'bleu de rochbaron'
korst2nee = "foume d'ambert"








geel = input ('is de kaas geel?')
if geel == ("ja"):
     gaten = input ('zitten er gaten in?')
     if gaten ==  ("ja"):
              duur = input ('is de kaas belachelijk duur?')
              if duur == ("ja"):
                      print (kaas_duur)

              else:
                      print (kaas_nietduur)
