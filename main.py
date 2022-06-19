#for loop

#count up until user-input number
print("\n-For loop count from zero to user-input stop point")
number = int(input("How many times you would like to count: "))
print('\nHere is the counting up to ' + str(number))
for i in range(number):
    print(str(i+1))                               # start count from 1 instead of 0


print("\n-For loop with start and stop point")
strt = int(input("Input a number to start the count: "))
fnsh = int(input("input a number to stop the count: "))

for i in range(strt,fnsh+1):                    # plus one to include the stop point
    print(i)

print("\n-For loop with start,stop point, and step")
st = int(input("input a number to start the count: "))
fn = int(input("input a number to stop the count: "))
step = int(input("input a number of how you would the number to be counted: "))
for i in range(st,fn,step):                                # if step 2 and start at 1 and finish at 10 the ouput 1 3 5 7 9
    print(i)

print("\nOutput/display character in word/s one by one")
word = input("\ninput word/s to be displayed one by one: ")
for i in word:
    print(i)

