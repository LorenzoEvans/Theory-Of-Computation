import re # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# TODO Define your regex


while line != "exit":
    # TODO Find matches
    match = re.findall("[0-9]{3}-[0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{7}|[0-9]{10}", line)
    match2 = re.findall("[(0-9)]{5}-[0-9]{3}-[0-9]{4}|[(0-9)]{5}[0-9]{3}-[0-9]{4}|[(0-9)]{5}[0-9]{3}[0-9]{4}", line)

    # TODO If no match found, print that no number was found
    # TODO Else, break number up into area code, prefix, and suffic
    if match or match2:
        if match:
            result = re.sub("[^\d]", " ", match.pop())
            result = re.split("\s", result)
            area_code, prefix, suffix = result[0], result[1], result[2]
            print(f"Area Code: {area_code}, Prefix: {prefix}, Suffix: {suffix}")
        elif match2:
            result = re.sub("[^\d]", " ", match2.pop())
            result = re.split("\s", result)
            area_code, prefix, suffix = result[1], result[3], result[4]
            print(f"Area Code: {area_code}, Prefix: {prefix}, Suffix: {suffix}")
        else:
            print(f"No match found in {line}")


    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    
    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")