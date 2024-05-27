def gcd(a,b):
    if b == 0:
        return a
    else:
        print(f"Recursion: {a,b}")
        return gcd(b, a % b)
    
if __name__ == '__main__':
    (a,b) = map(int, input("List the pair of vals to find the GCD: ").split())
    print(gcd(a,b))