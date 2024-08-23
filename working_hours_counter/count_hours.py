import sys
import re

def main():
    
    check_args()
    hours = 0
    wage = float(sys.argv[2])
    with open(sys.argv[1], "r") as file:
        for line in file:
            if line == "\n": continue
            hours += count_hours(line)

    hours = round(hours,2)
    print("Sum of hours: ", hours)
    print("Salary: ", f"{hours} * {wage} =", round(hours * wage,2), "zł")

def count_hours(line):
    matches = re.search(r"^\d*\D*(\d{1,2}):(\d{2})\D*-\D*(\d{1,2}):(\d{2})$", line)
    times = list()
    for _ in range(4):
        times.append(float(matches.group(_+1)))
    hour1, minutes1, hour2, minutes2 = times
    time1 = hour1 + minutes1/60
    time2 = hour2 + minutes2/60
    delta = time2 - time1 
    print(line.strip("\n"), f"   Number of hours: {round(delta,2)}")
    return delta


def check_args():
    if len(sys.argv) != 3:
        sys.exit("\nPass a correct number of args\n")
    


if __name__ == "__main__":
    main()