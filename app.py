import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="✅", layout="centered")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")

with st.form("task_form"):
    new_task = st.text_input("Enter a new task:")
    submitted = st.form_submit_button("➕ Add Task")
    if submitted and new_task:
        st.session_state.tasks.append(new_task)
        st.success(f"Task added: {new_task}")

st.subheader("Your Tasks")
if st.session_state.tasks:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([4, 1])
        col1.write(f"- {task}")
        if col2.button("❌", key=f"del_{i}"):
            st.session_state.tasks.pop(i)
            st.experimental_rerun()
else:
    st.info("No tasks yet. Add one above! 🚀")
