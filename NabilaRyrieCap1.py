from tabulate import tabulate
import time

# Main database
pData = [
    {"Reg No.": "P0001", "Name": "Elang Adhyaksa", "Age": 24, "Diagnosis": "ADHD", "Hospital Status": "Admitted"},
    {"Reg No.": "P0002", "Name": "Nadia Budianto", "Age": 17, "Diagnosis": "Anxiety", "Hospital Status": "Consultation"},
    {"Reg No.": "P1230", "Name": "Brian Mamangkey", "Age": 50, "Diagnosis": "Tourette Syndrome", "Hospital Status": "Critical"},
    {"Reg No.": "P0069", "Name": "Sabrina Putribening", "Age": 25, "Diagnosis": "K-Pop Addiction", "Hospital Status": "Emergency"}
]

# Function to display data
def showData(): 
    print("Current Patient Data")
    print(tabulate(pData, headers="keys", tablefmt="simple"))

# Some extra function I'm playing around with
def ifContinue():
    while True:
        print("Would you like to continue?")
        ifCon = str(input("Y/N: ")).capitalize()
        if ifCon == 'Y':
            return True
        elif ifCon == 'N':
            print("Thank you for visiting our database!")
            return False
        else:
            print("Please input the correct format.")

# add def hospital status
def hospitalStatus():
    print("\n")
    print("Select Hospital Status:")
    print("a. Consultation")
    print("b. Admitted")
    print("c. Discharged")
    print("d. Emergency")
    print("e. Surgery")
    print("f. Recovery")
    print("g. Outpatient")
    print("h. Critical")
    print("i. Transferred")
    print("j. Awaiting Diagnosis")
    print("\n")


# Main Loop and Menu
loop = True
while loop:
    print('''Welcome to Purwadhika Hospital Database!\n''')
    print('''Select Menu:
        1. Current Patient Data
        2. Add a new Patient
        3. Remove Patient
        4. Modify Patient Data
        5. Look for Specific Patient Data
        6. Exit Program\n''')

    menu = (input("Enter a number from the menu: "))
           
    try:
        menu = int(menu)

        # MENU TO SHOW DATA
        if menu == 1:
            while True:
                showData()
                loop = ifContinue()
                break

        # MENU TO ADD DATA
        elif menu == 2:
            while True:
                try:
                    reg_number_str = input("Enter new patient registration number: ")
                    # Convert the integer part to an integer and format it with leading zeros
                    reg_number_int = int(reg_number_str)
                    reg_number_formatted = f"{reg_number_int:04d}"
                    newReg = "P" + reg_number_formatted
                    if any(patient["Reg No."] == newReg for patient in pData):
                        print("Patient with the given Registration No. already exists.")
                        print("\n") 
                    else:
                        break
                except ValueError:
                    print("Invalid format. Please enter numbers only.")
            while True:
                try:
                    newName = input("Enter new patient's name: ")
                    if not newName:
                        print("Name cannot be empty.")
                    elif not newName.replace(" ", "").isalpha():
                        print("Invalid format. Please enter alphabetic characters.")
                    else:
                        newName = newName.title()
                        break  # Break out of the loop if the input is valid
                except:
                    pass
            while True:
                try:
                    newAge = int(input("Enter new patient's Age: "))
                    if newAge < 0:
                        print("Invalid age. Please enter an age greater than 0.")
                    else:
                        break
                except ValueError:
                    print("Invalid format. Please enter numericals.")
            while True:
                newDiag = input("Enter new patient's Diagnosis: ").title()
                if not newDiag:
                    print("Diagnosis cannot be empty. Please enter a valid diagnosis.")
                else:
                    break
            while True:
            # Displaying hospital status options
                hospitalStatus()

                status_mapping = {
                    'a': 'Consultation',
                    'b': 'Admitted',
                    'c': 'Discharged',
                    'd': 'Emergency',
                    'e': 'Surgery',
                    'f': 'Recovery',
                    'g': 'Outpatient',
                    'h': 'Critical',
                    'i': 'Transferred',
                    'j': 'Awaiting Diagnosis'
                }

                new_hospital_status = input("Select hospital status: ")
                if new_hospital_status in status_mapping.keys():
                    new_hospital_status = status_mapping[new_hospital_status]
                    break
                else:
                    print("Invalid keys. Please enter the corresponding letters a - j.")

            # Adding new patient data to database
            pData.append({"Reg No.": newReg, "Name": newName, "Age": newAge, "Diagnosis": newDiag, "Hospital Status": new_hospital_status})
            print("Patient added successfully!")
            showData()
            loop = ifContinue()

        # MENU TO REMOVE DATA
        elif menu == 3:
            showData()
            remReg = input("Enter the Registration No. of the patient to remove: ").upper()  # Convert to capitals

            # Find the index of the patient with the specified registration numbe
            for i in range(len(pData)):
                if pData[i]["Reg No."].upper() == remReg:
                    del pData[i]
                    print(f"Patient with Registration No. {remReg.capitalize()} removed successfully.")
                    print("\n")
                    break
            else:
                print(f"Patient with Registration No. {remReg.capitalize()} was not found.")
            loop = ifContinue()

        # MENU TO MODIFY DATA 
        elif menu == 4:
            showData()
            regNoToModify = str(input("Enter the Registration No. of the patient to modify: ").capitalize())

            # Find the index of the patient with the specified registration number
            indexToModify = None
            for i in range(len(pData)):
                if pData[i]["Reg No."] == regNoToModify:
                    indexToModify = i
                    break

            # Modify the patient data if found # put in Data Validation AGAIN
            if indexToModify is not None:
                print(f"Modifying data for patient with Registration No. {regNoToModify}")
                while True:
                    try:
                        newName = input("Enter new patient's name: ")
                        if not newName:
                            print("Name cannot be empty.")
                        elif not newName.replace(" ", "").isalpha():
                            print("Invalid format. Please enter alphabetic characters.")
                        else:
                            newName = newName.title()
                            break  # Break out of the loop if the input is valid
                    except:
                        pass
                while True:
                    try:
                        newAge = int(input("Enter the new age: "))
                        if newAge < 0:
                            print("Invalid age. Please enter an age greater than 0.")
                        else: 
                            break
                    except ValueError:
                        print("Invalid format. Please enter numericals.")
                while True:
                    newDiag = str(input("Enter new patient's Diagnosis: ")).title()
                    if not newDiag:
                        print("Diagnosis cannot be empty. Please enter a valid diagnosis.")
                    else:
                        break
                while True:
                # Display hospital statuses? statii what is the plural for status
                    hospitalStatus()
                     # Dict for hospital status
                    status_mapping = {
                            'a': 'Consultation',
                            'b': 'Admitted',
                            'c': 'Discharged',
                            'd': 'Emergency',
                            'e': 'Surgery',
                            'f': 'Recovery',
                            'g': 'Outpatient', 
                            'h': 'Critical',
                            'i': 'Transferred',
                            'j': 'Awaiting Diagnosis'
                        }
                    
                    # Receiving hospital status based on user choice
                    new_hospital_status = input("Enter the corresponding letter (a-j) for Hospital Status: ").lower()
                    if new_hospital_status in status_mapping.keys():
                        new_hospital_status = status_mapping[new_hospital_status]
                        break
                    elif not new_hospital_status:
                        print("Invalid format. Hospital status cannot be empty.")
                    else:
                        print("Invalid format. Please enter the corresponding letters from a-j.")

                    # Update the patient data
                pData[indexToModify]["Name"] = newName
                pData[indexToModify]["Age"] = newAge
                pData[indexToModify]["Diagnosis"] = newDiag
                pData[indexToModify]["Hospital Status"] = new_hospital_status
                print("Patient data modified successfully.")
                print("\n")
                showData()
                print("\n")
                loop = ifContinue()
            else:
                print(f"Patient with Registration No. {regNoToModify} not found.")
                break

        # MENU TO LOOK UP PATIENT DATA
        elif menu == 5:
            while True:
                regNoToSearch = input("Enter the Registration No. of the patient to search for: ").capitalize()
                # Find patient from 0
                found_patient = 0
                for patient in pData:
                    if patient["Reg No."] == regNoToSearch:
                        found_patient = patient
                        break

                if found_patient != 0:
                    # Display the patient's information
                    print("Patient Data:")
                    print(f"Registration No.: {found_patient['Reg No.']}")
                    print(f"Name: {found_patient['Name']}")
                    print(f"Age: {found_patient['Age']}")
                    print(f"Diagnosis: {found_patient['Diagnosis']}")
                    print(f"Hospital Status: {found_patient['Hospital Status']}")
                    print("\n")
                    loop = ifContinue()
                    break
                else:
                    print(f"Patient with Registration No. {regNoToSearch} was not found.")
                    

        # MENU EXIT 
        elif menu == 6:
            print("Thank you for visiting our database. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid menu option.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
        