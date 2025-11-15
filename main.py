
# 1
words = ["Cat", "Dog", "Rabbit", "Fish"]
lengths = [len(w) for w in words]
a = iter(lengths)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
try:
    print(next(a))
except:
    print("В списку закінчились слова")