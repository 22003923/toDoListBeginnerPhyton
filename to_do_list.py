choice = "a"
task = []

while choice.lower() != "d":
    print("a) Add a task\nb) View tasks\nc) Delete a task \nd)Exit the application\n")
    choice = input("Enter value a, b, c, d: ")
    if choice == "a":
        task_val = input("Enter a task: ")
        task.append(task_val)

    elif choice == "b":
        index = 0
        for item in task:
            print("{} {}".format(index, ") " + item))
            index += 1


    elif choice == "c":
        try:
            which = int(input("Choose task to be deleted with the number of the task: "))
            if 0 <= which < len(task):
                del task[which]
            else:
                print("Invalid index entered.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    elif choice == "d":
        print("Good bye!")
    else:
        print("Invalid choice")
