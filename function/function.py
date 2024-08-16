# Function definition
def calc_sum(a,b): # parameters
    return a + b
sum = calc_sum(1,2) #function call; arguments
print(sum)
# Another simple function
def print_this():
    print("Hello World")
print_this()

def avrg(a ,b ,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return sum
avrg(1,2,3)