#Basic - Print all integers from 0 to 150.
#Multiples of Five - Print all the multiples of 5 from 5 to 1,000
#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.
#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)


for i in range(1, 150):
    print(i)



print(list(range(5,1000,5)))



for number in range(0, 100):
    if number %5 == 0: 
        print("coding")
    if number %10 == 0:
        print("coding dojo")
    print(number)



sum = 0
for i in range(1, 500000, 2):
    sum = sum + i
print(sum)



        #START, STOP, STEP



for i in range(2018, 1, -4):
    print(i)




for i in range(10, 1000000, 5):
    print(i)