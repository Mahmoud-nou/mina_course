from models.langs import LangsModel
from models.users import UsersModel
from models.todos import TodosModel

print(" ")
print("=" * 30)
print(" ")

exit_var = False
new_start = True
show_todos = True
while not exit_var:
    if new_start:
        print('what do you wanna do?')
        print(' ')
        print('1: Show todos')
        print('2: Create a new todo')
        print('3: Update a todo')
        print('4: Delete a todo')
        print('5: Delete all todos')
        print('\\: EXIT')
        print('0: Main list')
        print(' ')
        action = input(f"YOUR ANSWOR: ")
    
    if action != '\\':
        print(" ")
        print("=" * 30)
        print(" ")
    
    new_start = False

    match action:
        case '\\':
            exit_var = True
        case '0':
            new_start = True
        case '1':
            show_todos = True
        case '2':
            print('What Do You want to write in your todo ?')
            print(' ')
            action = input(f"YOUR ANSWOR: \n")

            TodosModel.add_data({
                'todo': action
            })

            show_todos = True
        case '3':
            print('Come ON ? let\'s update it')
            print('exmaple: ( id: new todo )')
            print(' ')
            action = input(f"YOUR ANSWOR: ")
            
            if action != '\\':
                TodosModel.update_data({
                    'todo': action[(action.find(':') + 2):]
                }, int(action[3:action.find(':')]))

                show_todos = True
        case '4':
            print('Which one ?')
            print(' ')
            action = input(f"YOUR ANSWOR: ")
            
            if action != '\\':
                TodosModel.delete_data(f'"todo_id" = { int(action[3:]) }')
                show_todos = True
        case '5':
            TodosModel.delete_data()
            show_todos = True
        
    if show_todos:
        show_todos = False
        
        print(" ")
        print("=" * 30)
        print(" ")

        print(f"your todos is :\n")
        for todo in TodosModel.get_data():
            print(f"id_{ todo['todo_id'] }: " + todo['todo'])

        print(' ')
        print('\\: EXIT')
        print('0: Main list')
        print(' ')
        action = input(f"YOUR ANSWOR: ")