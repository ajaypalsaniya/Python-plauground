#Return fibbonachi series for entered number

n = int(input("enter you number for fibbonachi :"))
def fibo(n):
    if n==1:
        return 1
    else:
        return n+fibo(n-1)
print(fibo(n))

