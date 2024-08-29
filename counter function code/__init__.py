dict={}
sentence='i i am vedant vedant am'
sent=sentence.split()
counter=1
lst=list(sent)
for i in lst:
    if i in dict:
        dict[i]=counter+1
    else:
        dict[i]=counter

print(dict)
