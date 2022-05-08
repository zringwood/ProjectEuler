##By replacing the 1st digit of the 2-digit number *3, it turns out that six
##of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
##
##By replacing the 3rd and 4th digits of 56**3 with the same digit,
##this 5-digit number is the first example having seven primes among the
##ten generated numbers, yielding the family:
##56003, 56113, 56333, 56443, 56663, 56773, and 56993.
##Consequently 56003, being the first member of this family, is the
##smallest prime with this property.
##
##Find the smallest prime which, by replacing part of the number
##(not necessarily adjacent digits) with the same digit, is part of an
##eight prime value family.
import re
#First million primes, stored in a txt file
file = open("primes.txt","r")
primes = file.read().split("\n")
#Slightly cheeky way to do things but there's no need
#for cumbersome algorithms when we can just binary search.
def isPrime(number) :
    return primes.count("{}".format(number)) == 1

#We know that it needs to have 3 replaceable digits so we get rid of ones without three
for prime in primes :
    for num in "0123456789" :
        if prime.count(num) == 3 :
            #Potential for a prime family
            count = 0
            for num0 in "0123456789" :
                if isPrime(prime.replace(num,num0)):
                   count +=1
            if(count == 8):
                print(prime)
                break;

    
