import datetime

start_time = datetime.datetime.now()

def fibonacci(n):
    a=0
    b=1

    for k in range(n):
        c=a+b
        a=b
        b=c

    return b

for x in range(40):
        print (fibonacci(x))

end_time = datetime.datetime.now()

print(f"El tiempo de ejecución es: {end_time - start_time}")