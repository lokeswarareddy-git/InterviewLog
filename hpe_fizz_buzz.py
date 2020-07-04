#Write a Python program which iterates the integers from 1 to 50. 
# For multiples of three print "Fizz" instead of the number and 
# for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".

for num in range(1,51):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        continue
    elif num %3 == 0:
        print("Fizz")
        continue
    elif num % 5 == 0:
        print("Buzz")
        continue
    else:
        print(num)