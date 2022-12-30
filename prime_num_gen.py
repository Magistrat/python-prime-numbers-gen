def primes():
    count = 1
    while True:
        count += 1
        n = count
        while n >= 1:
            n = n - 1
            if n <= 1:
                yield count
                break
            if count % n == 0:
                break

def main():
    gen = primes()
    for i in range(10
        print(next(gen))


if __name__ == '__main__':
    main()
