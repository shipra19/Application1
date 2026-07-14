import streamlit as st
import functions

todos=functions.get_todos()

def add_todo():
    todo=st.session_state["j"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("To-Do App")
st.subheader("This is my to-do app")
st.write("This app is to increase your productivity")

for index, i in enumerate(todos):
    cb=st.checkbox(i, key=i)
    if cb:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label="", placeholder="Enter your new to-do", on_change=add_todo, key="j")