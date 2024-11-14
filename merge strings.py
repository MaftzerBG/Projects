word1 = 'abc'
word2 = 'pqr'
merge = ''
l1, l2 = len(word1), len(word2)
if len(word1) == len(word2):
    for i in range(min(l1, l2)):
        merge += word1[i]
        merge += word2[i]
    merge += word1[l2:] if l1>l2 else word2[l1:]
    print(merge)




