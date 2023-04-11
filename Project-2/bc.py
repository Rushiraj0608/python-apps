with open("input.txt") as file:
    lines = [line.rstrip() for line in file]

exp = {}
def assignmentFunction(line):
    line = line.replace(" ","")
    expression = line.split("=")
    # print(line)
    # print(expression[0], " = " , expression[1])
    exp[expression[0]] = expression[1]
    # print()
for line in lines:
    # print(line)
    if("=" in line):
        assignmentFunction(line)

# print(exp)
    # print()

# print(type(exp))

variable = [exp.keys()] 
print((variable))
for keys in exp:
    for var in variable :
        for v in var:
            if(v in exp[keys]):
                # print(exp[keys],"hvfdjv")
                exp[keys] = exp[keys].replace(v,exp[v])
        


for keys in exp:
    print(exp[keys],"exp[key]") 
    exp[keys] = eval(exp[keys])   

print(exp)