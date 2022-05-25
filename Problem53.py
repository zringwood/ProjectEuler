#How many, not necessarily distinct, values of nCr for 1<=n<=100,
#are greater than one-million?

total = 0
#Generate the first 100 levels of pascals triangle
last = [1]
for count in range(100):
    level = [1]
    for i in range(len(last)-1):
        level.append(last[i] + last[i+1])
        if (last[i] + last[i+1]) > 1e6 :
            total+=1
    level.append(1)
    last = level
print(total)
