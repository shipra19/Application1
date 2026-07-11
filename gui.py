import FreeSimpleGUI
import functions

label=FreeSimpleGUI.Text("Type in a to-do item")
input_box=FreeSimpleGUI.InputText(tooltip="Enter here")
add_button=FreeSimpleGUI.Button("Add")

window = FreeSimpleGUI.Window("My To-Do App", layout=[[label, input_box, add_button]])
window.read()
print("Hey")
window.close()
