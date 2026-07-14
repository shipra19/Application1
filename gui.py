import FreeSimpleGUI
import functions

label=FreeSimpleGUI.Text("Type in a to-do item")
input_box=FreeSimpleGUI.InputText(tooltip="Enter here", key="i")
add_button=FreeSimpleGUI.Button("Add")
list_box=FreeSimpleGUI.Listbox(values=functions.get_todos(), key="j", enable_events=True, size=(45,10))
edit_button=FreeSimpleGUI.Button("Edit")
complete_button=FreeSimpleGUI.Button("Complete")
exit_button=FreeSimpleGUI.Button("Exit")

window = FreeSimpleGUI.Window("My To-Do App",
                              layout=[[label],
                                      [input_box, add_button],
                                      [list_box, edit_button, complete_button],
                                      [exit_button]],
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
            window["j"].update(values=todos)
        case "Edit":
            edit_todo=values["j"][0]
            new_todo=values["i"]
            todos=functions.get_todos()
            index = todos.index(edit_todo)
            todos[index]=new_todo+ "\n"
            functions.write_todos(todos)
            window["j"].update(values=todos)
        case "Complete":
            complete_todo = values["j"][0]
            todos = functions.get_todos()
            todos.remove(complete_todo)
            functions.write_todos(todos)
            window["j"].update(values=todos)
            window["i"].update(value='')
        case "Exit":
            break
        case "j":
            window["i"].update(value=values["j"][0])
        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()
