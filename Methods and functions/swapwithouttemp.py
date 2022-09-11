def swap(a,b):
    a,b = b,a
    return a,b

a=3
b=5
print(f"before swapping a={a} b={b}")
a,b=swap(a,b)
print(f"after swapping a={a} b={b}")

