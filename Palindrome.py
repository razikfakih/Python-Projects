s = 'catdadbowlradarcarlevelbadriverrotor'

temp = ''

print("Palindrome strings:")

for i in s:
    temp = temp + i
    #print(temp)

    if(len(temp)>=3):
        l = len(temp)
        x = 0
        t = ''
        for j in range(0,l):
            if(temp[j] == temp[l-1-j]):
                x+=1
                #print("x=%d"%x)
                t = t + temp[j]
                #print("t=" + t)
        if(x == l):
            print(t)
            t = ''
            x = 0
        else:
            t = ''
            x = 0

        if(l>3):
            for k in range(1,l-2):
                n=0
                for m in range(k,l):
                    if(temp[m] == temp[l-1-n]):
                        x += 1
                        t = t + temp[m]
                    n = n + 1
                if(x == l-k):
                    print(t)
                    t = ''
                    x = 0
                    n = 0

                else:
                    t = ''
                    x = 0
                    n = 0