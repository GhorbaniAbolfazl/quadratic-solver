print("This program can calculate the solutions of the quadratic equation for you.")
print("Please enter the requested values based on ax^2 + bx + c.")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

if a != 0:
    delta = b**2 - 4*a*c

    if delta < 0:
        print("No real answer was found.")
    elif delta == 0:
        x = (-b) / (2*a)
        print(f"1 real answer found, x = {x}")
    else:
        sqrt_delta = delta**0.5
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        print(f"2 real answers found, x = {x1} , {x2}")

else:
    # Linear case: bx + c = 0
    if b != 0:
        x = (-c) / b
        print("Since a = 0, this is not a quadratic equation.")
        print(f"But I can still give the linear answer: x = {x}")
    else:
        # b == 0
        if c == 0:
            print("This equation has infinite solutions.")
        else:
            print("No answer was found.")
