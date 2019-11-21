# Below is Python code to sort the Big integers
# in ascending order
def SortingBigIntegers(arr, n):


    # Direct sorting using lamda operator
    # and length comparison
    arr.sort(key=lambda x: (len(x), x))
    return arr

    # Driver code of above implementation
arr = ["54", "724523015759812365462",
       "870112101220845", "8723"]
n = len(arr)

sorted_array=SortingBigIntegers(arr, n)

# Print the final sorted list using
# join method
print(" ".join(arr))
print(sorted_array)

#now we can convert it into integer
print(2+int(sorted_array[0]))
