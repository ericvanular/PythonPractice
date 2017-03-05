#string parser

def f(string):
    data = []
    line_data = ""
    in_quotes = False
    parsed_output = []

    for char in string:
        if char == '"':
            in_quotes = not in_quotes
        if char == ',' and in_quotes == False:
            data.append(line_data.replace(" ", ""))
            line_data = ""
        else:
            line_data += char

    data.append(line_data.replace(" ", ""))
    #print data

    for line in data:
        if line[0] == '"' and line[-1] == '"':
            parsed_output.append(line[1:-1])
        else:
            parsed_output.append(int(line))


    return parsed_output

print f('1,"Que", "Kay"')
