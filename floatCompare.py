import math

list=[81.617424, 78.445992, 77.065201, 77.001472,83.408829, 76.654587, 75.273796, 75.210068, 74.76918, 74.705002, 73.28672, 73.269371, 72.977776, 72.913605, 72.102379, 72.038635, 71.793732, 71.495316, 71.477959]


j=0
while(j<len(list)):

    print(type(list[j]))
    j+=1


i=0
maxx=max(list)
print(maxx)
while(list[i]!=maxx):
    i+=1
print(i)




i=0
c=0
while(i<len(list)):
    if(list[i])>list[i-1]:
        c=i
    i+=1
print(list[c],c)



