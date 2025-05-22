def number():
    try:
        n=input("type a number:")
        n=float(n)
        print(n)
    except(ValueError):
        print("Invalid input.")

number()
