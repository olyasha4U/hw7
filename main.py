
# 1
# words = ["Cat", "Dog", "Rabbit", "Fish"]
# lengths = [len(w) for w in words]
# a = iter(lengths)
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# try:
#     print(next(a))
# except:
#     print("В списку закінчились слова")
# 2
# class Number:
#     def __init__(self):
#         self.a=2
#     def __iter__(self):
#         self.a=2
#         print(self.a)
#         return self
#     def __next__(self):
#         self.a *=2
#         return self.a
# n=iter(Number())
# for i in range (10):
#     print(next(n))

# 3

# def gen(number):
#     c=number
#     while True:
#         c *=3
#         yield c
# g=gen(1)
# for i in range(10):
#     print(next(g))
4
from random import randint
alfavit=["a", "b","c","d", "e","f","g","h","i","j","k","l","m","n"]
number=randint(0,13)
def gen(num):
    print(alfavit[num])
    while True:
        num +=1
        yield alfavit[num]

g=gen(number)
try:
    for num in range(13):
        print(next(g))
except:
    print("Кінець списку")

