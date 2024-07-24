start = int(input('Масса нефти для перегонки:'))
cerocin = 0.3
masut = 0.53
cerosin_neft = start*cerocin
masut_neft = start * masut
neft = start - (cerosin_neft + masut_neft)
print(neft) # по условию задачи необходимо вывести керосин и мазут