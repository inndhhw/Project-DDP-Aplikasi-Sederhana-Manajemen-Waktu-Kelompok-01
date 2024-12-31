import streamlit as st
from datetime import datetime
# from PIL import Image  # Tambahkan impor untuk Pillow

class Alarm:
    def __init__(self):
        # Menyimpan alarms di session_state untuk persisten data
        if 'alarms' not in st.session_state:
            st.session_state['alarms'] = []  # Menyimpan alarm di session_state

    def add_alarm(self, time, message):
        # Menambahkan alarm ke dalam session_state
        st.session_state['alarms'].append({"time": time, "message": message})

    def show_alarms(self):
        # Menampilkan daftar alarm
        if len(st.session_state['alarms']) > 0:
            st.write("Daftar Alarm:")
            for alarm in st.session_state['alarms']:
                st.write(f"Alarm pada {alarm['time']}: {alarm['message']}")
        else:
            st.write("Tidak ada alarm yang ditambahkan.")

    def run(self):
        st.title("Pengingat Alarm")
        st.image("alarm-clock.jpg", width=160)
        # st.image("alarm1.jpg", width=150)
        
        # Waktu default adalah waktu sekarang jika belum ada di session_state
        if 'time' not in st.session_state:
            st.session_state['time'] = datetime.now().time()

        # Menampilkan input time yang nilainya diambil dari session_state
        time = st.time_input("Waktu Alarm", value=st.session_state['time'])
        
        # Simpan waktu yang dipilih ke session_state agar tetap ter-update
        st.session_state['time'] = time

        # Pesan alarm
        message = st.text_input("Pesan Alarm")
        
        # Menambahkan alarm jika tombol ditekan
        if st.button("Tambahkan Alarm"):
            if message:  # Jika pesan tidak kosong
                self.add_alarm(time, message)
                st.success(f"Alarm pada {time} berhasil ditambahkan!")
            else:
                st.warning("Pesan alarm tidak boleh kosong.")
        
        # Menampilkan daftar alarm
        self.show_alarms()

# Menjalankan aplikasi
if __name__ == "__main__":
    alarm = Alarm()
    alarm.run()