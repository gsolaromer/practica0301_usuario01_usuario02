import datetime

start_time = datetime.datetime.now()

def fib_r(n):
    if n < 2:
        return n
    return fib_r(n-1) + fib_r(n-2)

for x in range(40):
    print(fib_r(x))

end_time = datetime.datetime.now()

print(f"El tiempo de ejecución es: {end_time - start_time}")