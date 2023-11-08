"""
Ethan Smith

caseStudy.py

This program tests wether a student qualifies for the deans list or honor roll

"""
def main():
    fullName = get_Names()
    studentGpa = get_Gpa()
    test_Gpa(fullName,studentGpa)

def get_Names():
    lName = input("Please enter the students last name or ZZZ to exit: ")\

    if lName == "ZZZ":
        exit()

    fName = input("Please enter the students first name: ")
    return fName + " " + lName

def get_Gpa():
    while True:
        try:
            gpa = float(input("Please enter the students GPA: "))
        except ValueError:
            print("Please enter a number")
        else:
            return gpa
        

def test_Gpa(name, gpa):
    if gpa >= 3.5:
        print(name, "has made the Honor Roll and the Deans list")
    elif gpa >= 3.25 and gpa < 3.5:
        print(name, "has made the Honor Roll")
    else:
        print(name, "has not made the Honor Roll and the Deans list")

main()
