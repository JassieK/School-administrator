import csv


def write_into_csv(info_list):
    with open("Student_info.csv", "a", newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact", "E-Mail"])
        writer.writerow(info_list)






condition = True
i = 1
while condition:
    student_info = input(
        "Enter the information about the student number: {} in format (Name Age Contact E-mail)\n".format(
            i
        )
    )
    print("The Info is " + student_info)
    student_info_list = student_info.split(" ")
    print("\nThe Entered information is :")
    print(
        "Name :{} \nAge :{} \nContact :{} \nE-mail :{}".format(
            student_info_list[0],
            student_info_list[1],
            student_info_list[2],
            student_info_list[3],
        )
    )
    choice = input("Is the information finalised ? (yes/no) :")
    if choice == "yes":
         write_into_csv(student_info_list)
         ch = input("Do you want to do more enteries (yes/no) :")
         if ch == "yes":
            condition = True
            i = i + 1
         elif ch == "no":
            condition = False
        

    elif choice == "no":
        print("Please re-enter the information for student number: {}".format(i))
