
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

3
class Number_1:
    def __init__(self):
        self.b=3
    def __iter__(self):
        self.b=3
        print(self.b)
        return self
    def __next__(self):
        self.b *=3
        return self.b
n1=iter(Number_1())
for i in range(10):
    print(next(n1))