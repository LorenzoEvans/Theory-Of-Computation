import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex


while line != "exit":
    # TODO Find matches
    line_txt = line
    match = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{7}|[0-9]{10}", line)
    match2 = re.findall("[(0-9)]{3}-[0-9]{3}-[0-9]{4}", line)
    # print(match)
    
    # TODO If no match found, print that no number was found
    if not match and not match2:
       print(f"No match found in {line}")
   
    
    # TODO Else, break number up into area code, prefix, and suffic
    elif match or match2:
        if match:
            print(f"Found match '{match.pop()}' in {line}.")
        elif match2:
            print(f"Found match '{match.pop()}' in {line}.")
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")