with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

def assignmentFunction(line):
    line = line.replace(" ","")
    print(line)
    print()
for line in lines:
    # print(line)
    if("=" in line):
        assignmentFunction(line)
    print()