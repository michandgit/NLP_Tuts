#write a program for word analysis

def word_analysis(sentence) :
    l = sentence.split()
    op={}
    for i in range(len(l)):
        x = l[i]
        ct=0
        for j in l:
            if j==x:
                ct+=1
        op[x]=ct
    return op

def word_analysis1(sentence):
    l = sentence.split()
    op={}
    for i in l:
        if i not in op:
            op[i] = l.count(i)
    return op

sentence = "This is my college and it is not so my type"
d = word_analysis1(sentence)
print(d)
# for i in d:
#     print(i , " = "  , d[i])