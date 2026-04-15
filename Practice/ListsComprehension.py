num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Squares using list comprehension
squares = [n*n for n in num]
print(squares)

#Even numbers using list comprehension
even = [n for n in num if n%2==0]
print(even)

#Odd numbers using list comprehension
odd = [n for n in num if n%2!=0]
print(odd)

