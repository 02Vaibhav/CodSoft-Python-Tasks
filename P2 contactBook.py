# PROGRAM OF CONTACT BOOK

contact={}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))

while True:
    choice=int(input("1.  Add New Contact \n 2.  Search Contact \n 3.  Display Contact\n 4.  Edit Contact \n 5.  Delete Contact \n 6.  EXIT  \n Enter Your Choice "))
    if choice ==1:
        name=input("Enter the Name")
        phone=input("Enter the mobile number")
        contact[name] = phone
    elif choice==2:
        search_name=input("Enter the Contact Name")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name])
        else:
            print("Name is NOT Found in Contact Book")
    elif choice==3:
        if not contact:
            print("Empty Contact Book")
        else:
            display_contact()
    elif choice ==4:
        edit_contact = input("enter the contact to be edited")
        if edit_contact in contact:
                phone = input("Enter Mobile Number")
                contact[edit_contact]=phone
                print("contact updated")
                display_contact()
        else:
                print("Name is NOT Found in Contact Book")
    elif choice==5:
        del_contact = input("Enter the Contact to be Deleted")
        if del_contact in contact:
            confirm = input(" Do You Want to Delete this Contact y/n")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
                display_contact()
            else:
                print("Name is NOT Found in The Contact Book")
    else:
        break
