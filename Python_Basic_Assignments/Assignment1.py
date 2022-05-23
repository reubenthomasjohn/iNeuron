# Q1. Write a Python program to print "Hello Python"
print('Hello Python')

# Q2.
def operate(a, b):
    print("{a} + {b} = {c:.2f}".format(a = a, b = b, c = float(a)+float(b)))
    print("{a} / {b} = {c:.2f}".format(a = a, b = b, c = float(a)/float(b)))

operate(2.5, 2.89)

# Q3.
def area_triangle(base = 10, height = 10):
    print("Area of triangle: ", 0.5 * base * height)
area_triangle(10, 15)

# Q4. 
def swap(x=1, y=2):
    # create a temporary variable and swap the values
    x, y = y, x

    print('The value of x after swapping: {}'.format(x))
    print('The value of y after swapping: {}'.format(y))
swap()

# Q5. 
def gen_random(bounds = (0, 10)):
    import random
    
    return (random.randint(bounds[0], bounds[1]))

print("Random No: ", gen_random((1, 100)))

