def separate_names_birthdates(filename):
    """
    Reads names and birthdates from a text file and prints them in separate sections.

    Args:
        filename (str): The name of the text file containing the data.
    """
    try:
        # Attempt to open the specified file in read mode.
        with open(filename, 'r') as file:
            # Read all lines from the file into a list.
            lines = file.readlines()

            # Initialize empty lists to store names and birthdates.
            names = []
            birthdates = []
            
            # Iterate over each line in the file.
            for line in lines:
                # Strip any leading/trailing whitespace and split the line from the right into up to 4 parts.
                # This ensures the last three parts are treated as the birthdate.
                parts = line.strip().rsplit(' ', 3)
                
                # Check if the line was correctly split into exactly 4 parts (name + birthdate).
                if len(parts) == 4:
                    # Join all parts except the last three to form the name.
                    name = ' '.join(parts[:-3])
                    # Join the last three parts to form the birthdate.
                    birthdate = ' '.join(parts[-3:])
                    # Append the name to the names list.
                    names.append(name)
                    # Append the birthdate to the birthdates list.
                    birthdates.append(birthdate)
                else:
                    # Print a message for lines that do not match the expected format.
                    print(f"Skipping line due to incorrect format: {line.strip()}")

            # Print the "Name" section header.
            print("Name")
            # Iterate over each name in the names list and print it.
            for name in names:
                print(name)

            # Print a newline character followed by the "Birthdate" section header.
            print("\nBirthdate")
            # Iterate over each birthdate in the birthdates list and print it.
            for birthdate in birthdates:
                print(birthdate)

    # Handle the case where the specified file is not found.
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

# Example usage: specify the path to the file and call the function.
# Dear examiner this is the only way python could read the file on my computer by inputing the entire path
filename = "C:\\Users\\cathy\\OneDrive\\Desktop\\C7 LECTURES\\6 - File l0 operations\\DOB.txt"
separate_names_birthdates(filename)
