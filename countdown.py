import time
def countdown(n):
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        print('*' * n)
        time.sleep(1)
        countdown(n-1)

a=int(input("Enter the limit"))
countdown(a)