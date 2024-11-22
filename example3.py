import streamlit as st

# App title
st.title("To-Do List Manager 📝")

# Sidebar menu
st.sidebar.header("Menu")
menu = st.sidebar.selectbox("Navigate", ["Home", "About"])

if menu == "Home":
    st.header("Manage Your Tasks")

    # Initialize the session state for tasks if it doesn't exist
    if "tasks" not in st.session_state:
        st.session_state["tasks"] = []

    # Input box to add a new task
    new_task = st.text_input("Add a new task", "")
    if st.button("Add Task"):
        if new_task.strip():
            st.session_state["tasks"].append(new_task.strip())
            st.success(f"Task '{new_task}' added!")
        else:
            st.warning("Task cannot be empty.")

    # Display the tasks
    st.subheader("Your Tasks:")
    if st.session_state["tasks"]:
        for index, task in enumerate(st.session_state["tasks"]):
            col1, col2 = st.columns([8, 2])
            with col1:
                st.write(f"- {task}")
            with col2:
                # Use a button with a unique key to remove the task
                if st.button("Remove", key=f"remove-{task}-{index}"):
                    st.session_state["tasks"].pop(index)
                    st.experimental_rerun()  # Rerun the app after task removal
    else:
        st.info("No tasks yet. Add some!")

elif menu == "About":
    st.header("About This App")
    st.write(
        """
        This is a simple To-Do List app built with Streamlit.
        - Add new tasks
        - View your task list
        - Remove tasks when they're done

        Created for demonstration purposes.
        """
    )