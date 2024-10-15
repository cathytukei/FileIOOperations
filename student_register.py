# student_register.py

def register_students():
    # Ask the user how many students are registering
    num_students = int(input("How many students are registering? "))

    # Open the file reg_form.txt in write mode
    with open('reg_form.txt', 'w') as file:
        # Loop for the number of students
        for i in range(num_students):
            # Ask for the next student ID number
            student_id = input(f"Enter the ID number for student {i + 1}: ")
            # Write the ID number to the file with a dotted line
            file.write(f"{student_id}\n{'-' * 40}\n")

    print("Registration complete. The IDs have been saved to reg_form.txt.")

# Call the function to register students
if __name__ == "__main__":
    register_students()
