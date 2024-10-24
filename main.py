#from functions import get_todos, write_todos
import functions
import time
now = time.strftime("%b %d, %Y %H:%F")
print(now)
while True:
    user_action = input("Enter add,show edit, complete or exit")
    user_action = user_action.strip()

    if user_action.startswith('add'):

        todo = user_action[4:]
        todos = functions.get_todos()


        #file = open('files/todos.txt', 'r')
        #todos = file.readlines()
        #file.close()

        #with open('todos.txt', 'r') as file:
         #   todos = file.readlines()


        todos.append(todo + '\n')

        #file = open('todos.txt', 'w')
        #file.writelines(todos)
        #file.close()
        #with open('todos.txt','w') as file:
         #    file.writelines(todos)
        functions.write_todos(todos)

    elif  user_action.startswith('show'):
        # file = open('files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = functions.get_todos()
        #with open('todos.txt','r') as file:
        #    todos = file.readlines()
      #  new_todos = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
        print(f"length is {index +1}")


    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:] )
            print(number)
            number = number - 1
            todos = get_todos('todos.txt')
            print('here is todos existing', todos)


            new_todo = input("enter a new todo ")
            todos[number] = new_todo + '\n'

            print('here is how it will be', todos)

           # with open('todos.txt', 'w') as file:
           #     file.writelines(todos)
            write_todos(todos)
        except ValueError:
            print("your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            functions.write_todos(todos)

            message = f"todo {todo_to_remove} was removed here from the  list "
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print("command is not valid")
print("bye")