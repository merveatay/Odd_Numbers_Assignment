#Finds odd numbers between 2 number(including themself) taken from user
num1 = int(input('Enter first number:')) #first number taken from user named as num1 and converted to int to conduct mathematical operations
num2 = int(input('Enter second number:')) #second number taken from user named as num2 and converted to int to conduct mathematical operations
if num1 > num2: #to create an ascending range of numbers (class range)
    for i in range(num2,num1+1): #for loop iterating numbers between num2 and num1(range function does not include last value, to include num1 itself, increment last value by 1)
        if i%2 != 0: #checks if number indicated by i is odd, using modulus operator(%)
            print(i) #print number(i) as if statement is true and number is odd
elif num1 < num2: #to create an ascending range of numbers (class range)
    for i in range(num1, num2+1): #for loop iterating numbers between num1 and num2(range function does not include last value, to include num2 itself, increment last value by 1)
        if i%2 != 0: #checks if number indicated by i is odd, using modulus operator(%)
            print(i) #print number(i) as if statement is true and number is odd
else: #if, previous if or elif statements cannot be satisfied it means numbers are equal and cannot perfom desired ouput
    print("Enter numbers that are different from each other.") #inform user that given numbers are the same

