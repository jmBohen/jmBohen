import os
import sys

def print_lib(lib):
    if len(lib) == 0:
        print("No IPs to print")
        return
        
    print("\n\nIPs up:\n")
    for key in lib:
        if lib[key] == "up":
            print(f"{key}")


def main():
    
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <room> <first no.> <last no.>")
        sys.exit(1)

    room = sys.argv[1]
    result = dict()
    first, last = int(sys.argv[2]), int(sys.argv[3])
    for i in range(first, last+1):
        print(f"Pinging {room}{i:02}.iem.pw.edu.pl: ", end="", flush=True)
        ip = f"{room}{i:02}.iem.pw.edu.pl"
        response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
        result[ip] = "up" if response == 0 else "down"
        print(result[ip])

    print_lib(result)
main()