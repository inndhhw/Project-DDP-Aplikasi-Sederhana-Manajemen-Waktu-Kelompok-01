import streamlit as st

def display_dashboard():
    st.title("MyTime Planner")
    st.write("Selamat datang di MyTime Planner! Atur jadwal, terima pengingat, dan kelola waktu Anda dengan lebih efisien. Waktu Anda, prioritas Anda!")
    st.image("alarm.gif")

    st.subheader("Tabel Data Semua Fitur")

    # Ambil data dari session_state
    alarms = st.session_state.get('alarm', [])
    kalender = st.session_state.get('kalender', [])
    todo_list = st.session_state.get('todo_list', [])
    prioritas = st.session_state.get('prioritas', [])

    # Gabungkan semua data
    if alarms or kalender or todo_list or prioritas:
        st.write("**Hasil Input Semua Fitur:**")
        combined_data = {
            "Alarm": alarms,
            "Kalender": [f"{item['Tanggal']}: {item['Acara']}" for item in kalender],
            "To-Do List": todo_list,
            "Prioritas & Kategori": prioritas,
        }
        st.table(combined_data)
    else:
        st.write("Belum ada data yang dimasukkan.")
