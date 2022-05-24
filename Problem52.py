#It can be seen that the number, 125874, and its double,
#251748, contain exactly the same digits, but in a different order.
#Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
#contain the same digits.

#Trying a basic iterative solution
i=0
while True:
    i+=1
    if not sorted("{}".format(i))==sorted("{}".format(i*2)):
        continue
    if not sorted("{}".format(i))==sorted("{}".format(i*3)):
        continue
    if not sorted("{}".format(i))==sorted("{}".format(i*4)):
        continue
    if not sorted("{}".format(i))==sorted("{}".format(i*5)):
        continue
    if not sorted("{}".format(i))==sorted("{}".format(i*6)):
        continue
    print(i)
    break

