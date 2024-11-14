word1 = input("first word: ")
word2 = input("second word: ")
wordcomb = []
if len(word1) == len(word2):
    for i in range(len(word1)):
        wordcomb.append(word1[i])
        wordcomb.append(word2[i])
elif len(word1) > len(word2):
    for i in range(len(word1)):
        if i > len(word2)-1:
            wordcomb.append(word1[i])
        else:
            wordcomb.append(word1[i])
            wordcomb.append(word2[i])
elif len(word1) < len(word2):
    i = 0
    for i in range(len(word2)):
        if i > len(word1)-1:
            wordcomb.append(word2[i])
        else:
            wordcomb.append(word1[i])
            wordcomb.append(word2[i])
       
print(''.join(wordcomb))