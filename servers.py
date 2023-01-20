from validation import name_validate, phone_number_validate, client_exist
from database import MY_CONTACTS
from config import RETRY_COUNT


def get_all_contacts():
    print(MY_CONTACTS)


def create_contact():
    for chance in range(RETRY_COUNT)[::-1]:
        name = input("Please enter contact name: ")
        phone_number = input("Please enter phone number(0555123456): ")
        validate_response = (name_validate(name=name), phone_number_validate(phone_number=phone_number))
        is_valid = all(validate_response)
        if is_valid:
            is_client_exist = client_exist(name=name)
            if is_client_exist:
                MY_CONTACTS[name].append(phone_number)
                print(f"Phone number was added to exist contact {name}!")
                return
            MY_CONTACTS[name] = [phone_number]
            print(f"New contact was {name} success!")
            return
        print(f"You have a {chance} chance!")


def get_contact():
    name = input('Please enter contact name which do you want get: ')
    contact = MY_CONTACTS.get(name)
    if contact is not None:
        print(f"""
        Hi,
        Contact name -> {name}
        Phone number -> {contact}
        """)
        return
    print(f"Sorry {name} not found!")


# noinspection PyUnreachableCode
def update_contact():
    name = input("Enter contact name which do you want change: ")
    is_client_exist = client_exist(name=name)
    if is_client_exist:
        for chance in range(RETRY_COUNT)[::-1]:
            phone_number = input(" Enter new phone number: ")
            if phone_number_validate(phone_number=phone_number):
                MY_CONTACTS[name] = [phone_number]
                print(f"Your contact {name} was update!")
                return
            print(f"You have {chance} chance!")
        return
    print(f"Sorry {name} not found!")


def delete_contact():
    name = input('Please enter contact which you want delete: ')
    is_client_exist = client_exist(name=name)
    if is_client_exist:
        MY_CONTACTS.pop(name)
        print(f"Contact {name} was deleted!")
        return
    print(f"Sorry {name} not found!")


def farewell():
    print("GoodBye! I miss you")


def incorrect_command_exception():
    print('Incorrect comand! ')
