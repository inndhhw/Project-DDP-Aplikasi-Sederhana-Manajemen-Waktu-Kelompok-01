import streamlit as st

class PrioritasDanKategori:
    def __init__(self):
        self.data = []

    def run(self):
        st.title("Prioritas & Kategori")
        st.image("prioritas.jpg", width=160)

        prioritas = st.text_input("Masukkan Prioritas/Kategori")
        if st.button("Tambahkan Prioritas"):
            self.data.append(prioritas)
            st.session_state['prioritas'] = self.data
            st.success(f"Prioritas/Kategori ditambahkan: {prioritas}")

        if 'prioritas' in st.session_state:
            st.write("Daftar Prioritas & Kategori:")
            st.table(st.session_state['prioritas'])

