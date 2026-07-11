import FreeSimpleGUI
import functions

label=FreeSimpleGUI.Text("Type in a to-do item")
input_box=FreeSimpleGUI.InputText(tooltip="Enter here", key="i")
add_button=FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[
                                  [label],
                                  [input_box, add_button]
                                      ],
                              font=("Arial", 20))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["i"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()
