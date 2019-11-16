phone_book={}
names=[]
data=[]
numbers=[]
entry_strings=[]
name_check=[]
no_of_entries=int(input())
i=0;j=0;k=0
while i<no_of_entries:
    a=input()
    entry_strings.append(a)
    data.append(entry_strings[i].split(" "))
    names.append(data[i][0])
    numbers.append(data[i][1])
    phone_book[names[i]] = numbers[i]

    i+=1

while j<len(data):
    name_check.append(input())
    if phone_book.get(name_check[j])==None:
        print("Not found")
    else:
        print(name_check[j]+"="+phone_book.get(name_check[j]))
    j+=1