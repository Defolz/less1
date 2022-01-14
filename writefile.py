l = list()
date = list()
names = list()
f = open('Perepis.txt', 'r')
number = 0
for i in f:
    l= i.split(".")
    l[2] = int(l[2])
    if l[2] < 1978:        
        number +=1
        l = i.split()
        print(l[0])
        
f.close()
print(number)         
print()
print()
print("######")        
print()
print()
f = open('Perepis.txt', 'r')
for i in f:
    l = i.split(".")
    l[2] = int(l[2])
    year = l[2]
    #print(l[2])
    if (l[2] < 1980) and (l[2] > 1960):
        l = i.split()
        print(l[0],l[1],l[2],year)
  
        
