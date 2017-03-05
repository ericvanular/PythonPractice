# Enter your code here. Read input from STDIN. Print output to STDOUT
import fileinput

for idx, line in enumerate(fileinput.input()):
    if idx == 0:
        input_string = line.strip()
    
def reduce_string(input_string):
    if input_string == "":
        return [False, ""]
    output_string = ""
    num_adjacent_chars = 1
    for idx, char in enumerate(input_string):
        if idx != 0:
            if char == input_string[idx - 1]:
                num_adjacent_chars += 1
            else:
                if num_adjacent_chars % 2 != 0:# if odd
                    output_string += input_string[idx - 1]
                num_adjacent_chars = 1
                
    if num_adjacent_chars % 2 != 0:
        output_string += input_string[-1]
    
    if output_string == input_string:
        return [False, output_string]
    
    return [True, output_string]

def get_non_reducible_string(input_string):
    was_reduced, non_reducible_string = reduce_string(input_string)
    while was_reduced:
        was_reduced, non_reducible_string = reduce_string(non_reducible_string)
    if non_reducible_string == "":
        return "Empty String"
    return non_reducible_string
        
    
    
  
print get_non_reducible_string(input_string)
         
                
            
   