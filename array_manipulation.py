import numpy as np

column1=[]
column2=[]
indexess = 0
i=0
keyss=0
valuess=0
column1.append(keyss)
column2.append(valuess)
j=0
count_index=0
while j<5:
    indexess=0
    i=0
    while(i<5):
        keyss+=1
        valuess+=1
        # print(keyss,valuess)
        column1.append(keyss)
        column2.append(valuess)

        column1[indexess]= keyss+6
        column2[indexess]= valuess+6
        if len(column1) > indexess + 1:
            # for h in range(0,i):
            #     del column1[indexess]
            del column1[-1]

        indexess+=1

        i+=1
    j+=1

# del column2[indexess + 1]
print(column2)
print(column1)

# print(column1)
# print(column2)
# del column1[2]
# print(column1)
# print(column2)