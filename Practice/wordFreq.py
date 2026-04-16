text = input("Enter a string: ")
#lower Case
text = text.lower()
# frequency count
words = text.split()
word_freq ={}
for word in words:
    if word in word_freq:
        word_freq[word] +=1
    else:
        word_freq[word] = 1
print(word_freq)
