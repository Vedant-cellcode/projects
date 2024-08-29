
def prime(num):
    count = 0
    for i in range(2,num+1):
        prime=True
        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime==True:
            count += 1
    print(count)
prime(100)