

def arithmetic_arranger(problems, solve=False):

    # Check for number of problems in the string.
    if len(problems) > 5:
        return "Error: Too many problems."

    first=""
    second=""
    lines=""
    sumx=""
    string=""
    for problem in problems:
        equation=problem.split()
        if len(equation[0])>4 or len(equation[2])>4:
            return "Error: Numbers cannot be more than four digits."
        if equation[1]=="*" or equation[1]=="/":
            return "Error: Operator must be '+' or '-'."
        if not equation[0].isdigit() or not equation[2].isdigit():
            return "Error: Numbers must only contain digits."
        #here you sum
        sum=""
        if equation[1]=="+":
            sum=str(int(equation[0])+int(equation[2]))
        if equation[1]=="-":
            sum=str(int(equation[0])-int(equation[2]))
        length=max(len(equation[0]),len(equation[2]))+2
        top=str(equation[0]).rjust(length)
        bottom=equation[1] + str(equation[2]).rjust(length-1)
        line=""
        res=str(sum).rjust(length)
        for s in range(length):
            line+="-"
        if problem!=problems[-1]:
            first += top + "    "
            second += bottom + "    "
            lines += line + "    "
            sumx += res + "    "
        else:
            first+=top
            second+=bottom
            lines+=line
            sumx+=res
    if solve is True:
        string=first+"\n"+second+"\n"+lines+"\n"+sumx
    else:
        string=first+"\n"+second+"\n"+lines
    return string
print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')
