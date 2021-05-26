#!/usr/bin/env python3.9
from contact import Contact

def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()

def del_contact(contact):
    '''
    Function to delete a contact
    '''
    contact.delete_contact()

def find_contact(number):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return Contact.find_by_number(number)

def check_existing_contacts(number):
    '''
    Function that checks if a contact exists with that number and return a Boolean
    '''
    return Contact.contact_exists(number)

def display_contacts():
    '''
    Function that returns all the saved contacts
    '''
    return Contact.display_contacts()

def email_copy(number):
    '''
    Function that copies the email address to the clipboard.
    '''
    return Contact.copy_email(number)
# Main
def main():
    print('Hello Welcome to your contact list. What is your name?')
    user_name = input('>> ')
    print('\n')
    print(f'Hello {user_name}. What would you like to do?\n')

    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, dn -delete the contact, cp -copy the email, ex -exit the contact list ")
        short_code = input('>> ').lower()
        if short_code == 'cc':
            print('\n')
            print('New Contact')
            print('-'*15)
            print ("First name ....")
            f_name = input('>> ')

            print("Last name ...")
            l_name = input('>> ')

            print("Phone number ...")
            p_number = input('>> ')

            print("Email address ...")
            e_address = input('>> ')

            save_contacts(create_contact(f_name,l_name,p_number,e_address))
            print('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')

        elif short_code == 'dc':
            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')
        elif short_code == 'fc':
            print("Enter the number you want to search for")
            
            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)
                
                print(f"Phone number.......{search_contact.phone_number}")
                
                print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")
        elif short_code == 'dn':
            print("Enter the number you want to delete\n")

            delete_number = input()
            if check_existing_contacts(delete_number):
                found_contact = find_contact(delete_number)
                print("/n")
                print(f"Contact {found_contact.first_name} {found_contact.last_name} deleted successfully")
                print("/n")
                del_contact(found_contact)
                print('-' * 20)
            else:
                print("That contact does not exist")
        elif short_code == 'cp':
            print("Enter the number whose email you want to copy\n")

            copy_number = input()
            if check_existing_contacts(copy_number):
                copy_contact = find_contact(copy_number)
                email_copy(copy_contact)
                print("/n")
                print(f"{copy_contact.email} copied to clipboard.")
                print("/n")
                print('-' * 20)
            else:
                print("That contact does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':
    main()

