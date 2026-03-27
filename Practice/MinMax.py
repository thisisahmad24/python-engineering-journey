# Minimum and Maximum in a List without using built-in functions
List = [23,1,3,45,67,89,12,34]
min = List[0]
max = List[0]
for i in List:
    if i< min:
        min = i
    if i> max:
        max = i
print("Minimum Number in the List is: ", min)
print("Maximum Number in the List is: ", max)

