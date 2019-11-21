arr=['a','t','f','h','b','c','k','e','n','j','l','g']

print(arr)
def sorting(arr1):
    i=0
    j=0
    k=0
    temp = []
    temp = arr1
    temp_list_1=[]

    while (k < len(arr1)):
        i=0
        while(i<len(arr1)):

            if i<len(arr1)-1:
                temp_list_1 = list(arr1)
                if temp_list_1[i]>temp_list_1[i+1]:
                    swap=temp_list_1[i]
                    temp_list_1[i]=temp_list_1[i+1]
                    temp_list_1[i + 1]=swap

                    arr1 = ''.join(temp_list_1)
            else:
                temp_list_1 = list(arr1)
                if temp_list_1[i] > temp_list_1[i - 1]:
                    swap = temp_list_1[i]
                    temp_list_1[i] = temp_list_1[i - 1]
                    temp_list_1[i - 1] = swap

                    arr1 = ''.join(temp_list_1)

            i+=1
        k+=1


    return arr1
char_array=sorting(arr)
char_array_list=list(char_array)
print(char_array_list)
print(char_array)
