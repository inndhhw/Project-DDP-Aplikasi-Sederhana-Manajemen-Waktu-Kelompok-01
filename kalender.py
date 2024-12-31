import streamlit as st

class Aktivitas:
    def __init__(self):
        # Inisialisasi data untuk menyimpan daftar acara
        self.data = st.session_state.get('kalender', [])

    def run(self):
        st.title("Aktivitas")
        st.image("aktivitas.jpg", width=160)

        # Input tanggal dan acara
        tanggal = st.date_input("Pilih Tanggal")
        acara = st.text_input("Masukkan Acara")
        
        # Tombol untuk menambahkan acara
        if st.button("Tambahkan Acara"):
            new_event = {"Tanggal": tanggal, "Acara": acara}
            self.data.append(new_event)  
        # Tambahkan ke daftar
            st.session_state['kalender'] = self.data  
        # Simpan ke session_state
            st.success(f"Acara ditambahkan: {acara} pada {tanggal}")

        # Tampilkan daftar acara yang sudah dimasukkan
        if self.data:
            st.write("### Daftar Acara:")
            st.table(self.data)  
        # Tampilkan data sebagai tabel
        else:
            st.write("Belum ada acara yang ditambahkan.")




