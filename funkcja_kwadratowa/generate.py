#generate quadratic formula
import sys
import random

def generate():
    a = random.randint(-5, 5)
    while a == 0:
        a = random.randint(-5, 5)
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    
    b = -(x + y)
    c = x * y
    b *= a
    c *= a

    a = f"{a}x^2" if a != 1 else "x^2"
    if b == 0:
        b = ""
    elif b == 1:
        b = "x"
    else:
        b = f"+ {b}x" if b > 0 else f"- {-b}x"
    
    if c == 0:
        c = ""
    else:
        c = f"+ {c}" if c > 0 else f"- {-c}"

    sign = random.choice(["=", "<", ">", "≤", "≥"])
    print(f"{a} {b} {c} {sign} 0")

def main():
    how_many = int(sys.argv[1])
    for i in range(how_many):
        generate()

main()