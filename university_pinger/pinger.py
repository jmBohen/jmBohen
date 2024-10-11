import os
import sys

def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename>")
        sys.exit(1)
    else:
        room = sys.argv[1]

    for i in range(20):
        ip = f"{room}{i}.iem.pw.edu.pl";
        response = os.system(f"ping {ip}")
        if response == 0:
            print(f"{ip} is up")
        else:
            print(f"{ip} is down")

main()