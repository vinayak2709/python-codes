# Enter your code here. Read input from STDIN. Print output to STDOUT
#import array

inputs = int(input())
s = [["d"]]
i = 0
while (i < inputs):
    s.insert(i, str(input()))
    i += 1
#s.remove("d")
si = 0  # stringIterations
ci = 0  # characterIterations
l = [1]
l.remove(1)
for i in range(0, inputs):
    l.insert(i, len(s[i]))
while (si < inputs):
    while (ci < l[si]):
        if (ci % 2 == 0):
            print(s[si][ci], end="")
        ci += 1
    print(end=" ")
    ci = 0
    # if l[si]%2==1:
    while (ci < (l[si])):
        if (ci % 2 == 1):
            print(s[si][ci], end="")
        ci += 1

    print("")

    # print("\n")
    ci = 0
    si += 1

