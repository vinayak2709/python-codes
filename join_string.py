numList = ['1', '2', '3','4']
element_seperator = ''
# print(seperator.join(numList))
r=element_seperator.join(numList)
print(r)
numTuple = ('1', '2', '3', '4')
print(element_seperator.join(numTuple))

s1 = 'abc'
s2 = '123'

""" Each character of s2 is concatenated to the front of s1"""
print('s1.join(s2):', s1.join(s2))

""" Each character of s1 is concatenated to the front of s2"""
print('s2.join(s1):', s2.join(s1))