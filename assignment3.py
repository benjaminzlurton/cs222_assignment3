students = {}  # The dictionary of student IDs as the keys and their list of properties as the values

for student_txt in open("students.txt").read().splitlines(): # Open the file, turn it into a string, and then split the string into a list of strings each of which is a line
    student = student_txt.split(",")  # Split the string into a list of strings by comma
    students[student[0]] = student[1:]  # Save the first element of the list as the key and the entire rest of the list as it's value into the students dictionary

while True:
    print("Choose an option\n"
          "1) Search by last name\n"
          "2) Search by major\n"
          "3) Quit")
    selection = input()

    if selection == "1":
        print("Enter a last name to search:")
        query = input()
        num_results = 0 #
        for student_id, details in students.items(): # Iterate over each item in the list
            if details[0].lower() == query.lower(): # If the student's last name and the search query matches...
                print(f"{student_id}, {details}")   # ...print it
                num_results += 1                    # and increment the result count by 1
        if num_results == 0:                        # If there aren't any results, inform the user
            print("No matching results found.")
        print()

    elif selection == "2":
        print("Enter a major to search:")
        query = input()
        num_results = 0
        for student_id, details in students.items():  # Iterate over each item in the list
            if details[2].lower() == query.lower():  # If the student's major and the search query matches...
                print(f"{student_id}, {details}")    # ...print it
                num_results += 1                     # and increment the result count by 1
        if num_results == 0:                         # If there aren't any results, inform the user
            print("No matching results found.")
        print()

    elif selection == "3":
        print("Goodbye!")
        exit()
