import json

"""TRY EXCEPT BLOCK EXAMPLE"""
try:
    file = open('new_families.txt', 'r')

    for f in file:
        json_in = f.replace("'", '"')
        new_f = json.loads(json_in)

    print("This try-block worked!")

except IOError as e:
    print("IO error in the try block, please fix this!")
    print(e)

except EOFError as e:
    print("EOF error in the try block, please fix this!")
    print(e)
else:
    print("No, excpetions :) ... continue with program")

finally:
    print("This runs no matter what.")
