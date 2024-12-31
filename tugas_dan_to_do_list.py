import streamlit as st

class TugasDanToDoList:
    def __init__(self):
        self.data = []

    def run(self):
        st.title("To-Do List")
        st.image("to-do-list.jpg", width=160)

        tugas = st.text_input("Masukkan Tugas")
        if st.button("Tambahkan Tugas"):
            self.data.append(tugas)
            st.session_state['todo_list'] = self.data
            st.success(f"Tugas ditambahkan: {tugas}")

        if 'todo_list' in st.session_state:
            st.write("Daftar Tugas:")
            st.table(st.session_state['todo_list'])

