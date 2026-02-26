# TERATORS(CUSTOM)
# Create
# a
# custom
# iterator
# that
# prints
# numbers
# from
#
# 1
# to
# 5.

nums=[1,2,3,4,5]

it=iter(nums)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))



# Write
# an
# iterator
#
#
# class that returns next even number.
#


class EvenIterator:
    def init(self):
        self.num=0

    def iter(self): #returns iterator object like 0 here
        return self

    def next(self):    #returns next value next even num
        self.num=self.num+2
        return self.num

e=EvenIterator()

print(next(e))
print(next(e))
print(next(e))

#
# Explain and demonstrate
# the
# use
# of
# iter() and next().


class EvenIterator:
    def init(self):
        self.num=0

    def iter(self): #returns iterator object like 0 here
        return self

    def next(self):    #returns next value next even num
        self.num=self.num+2
        return self.num

e=EvenIterator()

print(next(e))
print(next(e))
print(next(e))


# 🔹 GENERATORS
# Write
# a
# generator
# to
# generate
# numbers
# from
#
# 1
# to
# N.


def numbers(n):
    i=1
    while i<=n:
        yield i
        i=i+1

# for x in numbers(5):
#     print(x)

gen=numbers(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))




# Create
# a
# generator
# to
# generate
# even
# numbers
# only.

def numbers(n):
    i=2
    while i <= n:
        yield i
        i = i + 2


gen = numbers(10)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


# Write
# a
# generator
# to
# read
# a
# file
# line
# by
# line.


def read_file(filename):
    file=open(filename,"r")
    for line in line:
        yield line


# Create
# a
# generator
# for Fibonacci series.


def fibonacci(n):
    a=0
    b=1
    count=0

    while count<n:
        yield a
        c=a+b
        a=b
        b=c
        count=count+1


gen=fibonacci(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



#     Write
#     a
#     generator
#     that
#     simulates
#     retry
#     attempts(max
#     3
#     tries).

def retry_attempts():
    attempt=1
    while attempt<=3:
        yield attempt
        attempt=attempt+1

gen=retry_attempts()

print(next(gen))
print(next(gen))
print(next(gen))