import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to do ")
input_box = sg.InputText(tooltip = "enter todo")
add_button = sg.Button("add")

window = sg.Window('MY FIRST TO-Do APP', layout = [[label],[input_box,add_button]])
window.read()
window.close()