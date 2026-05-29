def insert():
    print('element inserted')

def delete():
    print('element deleted')

def update():
    print('element updated')

def lists():
    print('list displayed')

def end():
    print('end of program')


def get_menu(choice):
    menu = {
        1: insert,
        2: delete,
        3: update,
        4: lists,
        5: end
    }
    return menu[choice]


def run_menu():
    while True:
        print('\n1:Insert 2:Delete 3:Update 4:List 5:Exit')
        choice = int(input('your choice please: '))
        get_menu(choice)()

        if choice == 5:
            break


run_menu()