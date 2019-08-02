import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex


while line != "exit":
    # TODO Find matches
    line_txt = line
    match = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{7}|[0-9]{10}", line)
    match2 = re.findall("[(0-9)]{5}-[0-9]{3}-[0-9]{4}|[(0-9)]{5}[0-9]{3}-[0-9]{4}|[(0-9)]{5}[0-9]{3}[0-9]{4}", line)
    # print(match)
    
    # TODO If no match found, print that no number was found
    if not match and not match2:
       print(f"No match found in {line}")
   
    
    # TODO Else, break number up into area code, prefix, and suffic
    elif match or match2:
        if match:
            result = re.sub("[^\d]", "", match.pop())
            print('no paren: ',result)
            print('no paren result type: ',type(result))
            area_code = ""
            prefix = ""
            suffix = ""
            print(type(match))
            for x in range(len(result)):
                while result.index(x) <= 4:
                    area_code += x
                    print(area_code)
            # print(f"Found match '{match.pop()}' in {line}.")
        elif match2:
            result = re.sub("[^\d]", "", match2.pop())
            print('with paren: ',result)
            # print(f"Found match '{match2.pop()}' in {line}.")
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")