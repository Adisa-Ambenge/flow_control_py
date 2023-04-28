def even_numbers():
   x=0
   while x<50:
       x+=1
       if x%2!=0:
         continue
       print(x)
       
# Question 2
def check_is_prime(num):
    if num < 2:  # 0 and 1 are not considered prime numbers
        print("Not prime")
        return
    
    for i in range(2, int(num/2)+1):
        if num % i == 0:
            print("Not prime")
            return
    
    print("Prime")
    
# Question 3

def list_Of_Integers(nums):
    sum = 0
    for num in nums:
        if num%2 ==0:
            sum+=num
    print(sum)
    
# Question 4

def numbers_divisble_by_two(num1,num2):
    add = 0
    for num in range(num1,num2+1):
        if num%3 ==0:
            add+=num
    print(add)
        
        
