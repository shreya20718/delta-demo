try:
    file = open("sample.txt", "r")
    lines = file.readlines()
    
    if len(lines) >= 2:
        print("Line 1:", lines[0].strip())
        print("Line 2:", lines[1].strip())
    elif len(lines) == 1:
        print("Line 1:", lines[0].strip())
        print("Line 2: <No second line>")
    else:
        print("The file is empty.")
        
except FileNotFoundError:
    print("Error: The file 'sample.txt' was  not found.")

finally:
    print("Execution completed, whether an error occurred or not.")
    try:
        file.close()
    except NameError:
        pass
