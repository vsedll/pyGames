import random

def fib():
    a, b = 0 , 1
    while True:
        yield a
        a, b = b, a + b

def cities():
    arr = ['asd','sd','gsr','rtb']
    iter(arr)

gen = fib()
for i in range(1,10):
    #print(next(gen))
    pass

def Rand_gen():
    while True:
        yield random.randint(0,9)

def range_gen(start, end, step = 1):
    while start < end:
        yield start
        start += step
        
def map_gen(func, l):
    i = 0
    while i < len(l):
        if func(l[i]):
            yield l[i]
        i += 1

#gen = range_gen(1,11)
for i in range(1,10):
   # print(next(gen))
   pass

gen = map_gen(lambda x: x < 2, [1, 2, 3, 4, 5])
for i in range(1,10):
    print(next(gen))
