
print("Hi, this is my first python script")

a = ['Mary', 'had', 'a', 'little', 'lamb']
print(len(a))
for i in range(len(a)):
    print(i + 1, a[i])


def fib(n):  # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


# Now call the function we just defined:
fib(2000)



