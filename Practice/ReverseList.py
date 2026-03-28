# Reverse List (No reverse())
list = [1,2,3,4,5]
reversedList = []
reversedList.append(list[4])
reversedList.append(list[3])
reversedList.append(list[2])
reversedList.append(list[1])
reversedList.append(list[0])
print(reversedList)

list2 = [6,7,8,9,10]
reverseList = [None] * len(list2)
reverseList[0] = list2[4]
reverseList[1] = list2[3]
reverseList[2] = list2[2]
reverseList[3] = list2[1]
reverseList[4] = list2[0]
print(reverseList)
