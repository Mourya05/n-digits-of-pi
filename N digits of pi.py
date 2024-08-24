from mpmath import mp

def digits(n):
    
    mp.dps = n + 1
    pi_str = str(mp.pi)
    
    #+2 to include 3.
    print(pi_str[:n + 2])

n = int(input("Enter the number of digits: "))
digits(n)