def upper(b):
    b = a.split()
    count = 0
    for i in b:
        for j in i:
            if j==j.upper():
                count=count+1
    print(f'the upper letters are {count}')

def lower(b):
    b = a.split()
    count1 = 0
    for i in b:
        for j in i:
            if j!=j.upper():
                count1=count1+1
    print(f'the lower letters are {count1}')
a=input('enter the sentence')
upper(a)
lower(a)


