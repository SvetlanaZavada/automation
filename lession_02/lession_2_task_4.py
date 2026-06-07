def fizz_buzz(n):
    for a in range(1, n+1):
        if a % 3 == 0 and a % 5 == 0:
            print(f"{a} - FrizzBuzz")
        elif a % 3 == 0:
            print(f"{a} - Fizz")
        elif a % 5 == 0:
            print(f"{a} - Buzz")
        else:
            print(a)


fizz_buzz(17)
