# Practice
# Goal
# Project

# from test_class.servers import create_contact, get_contact, update_contact, delete_contact
# import validation
#
# while True:
#     action = input("""
#                    Press 1 to create contact
#                    Press 2 to get contact
#                    Press 3 to edit contact
#                    Press 4 to delete contact
#                    Press 5 to exit
#                    """)
#     if action == '1':
#         create_contact()
#     elif action == '2':
#         get_contact()
#         validation.checking_get_contact()
#     elif action == '3':
#         update_contact()
#         validation.checking_update_contact()
#     elif action == '4':
#         delete_contact()
#     elif action == '5':
#         print('Goodbye!')
#         break
#     else:
#         print('Incorrect command')
#
#

from servers import create_contact, get_contact, update_contact, \
    delete_contact, get_all_contacts, incorrect_command_exception


def main():
    while True:
        action = input("""
                       Press 1 to create contact
                       Press 2 to get contact
                       Press 3 to edit contact
                       Press 4 to delete contact
                       Press 5 to show all my contacs
                       Press 6 to exit
                       """)
        if action == '1':
            create_contact()
        elif action == '2':
            get_contact()
        elif action == '3':
            update_contact()
        elif action == '4':
            delete_contact()
        elif action == '5':
            get_all_contacts()
            break
        else:
            incorrect_command_exception()


if __name__ == '__main__':
    main()







