# def a(x):
#     return x ** 2    
a = lambda x : x ** 2

# def b(x, y):
#     return x, y : x ** 2  + y ** 2
b = lambda x, y : x ** 2  + y ** 2

# def c(*args):
#     return sum(args)/len(args)
c = lambda *args : sum(args)/len(args)

# def d(s):
#     return "".join(set(s))
d = lambda s: "".join(set(s))

print(a(100))
print(b(5, 20))
print(c(-2, 10, 9, 7))
print(d("Reza"))