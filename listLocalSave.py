import cv2
import numpy as np
from types import SimpleNamespace


Dict = {'name': "Vinayak" ,'surname': "Majgaonkar",'empId':1}


a=SimpleNamespace(**Dict)
p=a.name
q=a.surname
r=a.empId

print("Local_name = " ,p)
print("Local_surname = ",q)
print("Local_empId = ",r)

s="Local_"
s1=a.__str__()
s2=s+s1
print(s2)

s1= (a)
print(s1)

for key,val in Dict.items():
        exec(key + '=val')
        print("Local_"+key,val)

