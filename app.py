import streamlit as st
from dashboard import display_dashboard
from alarm import Alarm
from kalender import Aktivitas
from tugas_dan_to_do_list import TugasDanToDoList
from prioritas_dan_kategori import PrioritasDanKategori

# Instansiasi fitur
alarm = Alarm()
kalender = Aktivitas()
tugas = TugasDanToDoList()
kategori = PrioritasDanKategori()

# Menjalankan fitur
def main():
    # Set the page configuration
    st.set_page_config(page_title="Pengingat Jadwal.jpeg", layout="wide")
    

    # Load CSS for styling
    st.markdown('<style>body {background-color: #f0f2f5;}</style>', unsafe_allow_html=True)

    # Sidebar for navigationt
    with st.sidebar:
        col1, col2 = st.columns([20, 18]) 
        
        with col1:
            st.image("haldepan.jpg")

        with col2:
            st.sidebar.title("Time Craft")
    
    # st.sidebar.title("Pilih Menu")


    menu = st.sidebar.radio("Menu", ["Dashboard", "Alarm", "Aktivitas", "To-Do List", "Prioritas & Kategori"])

    if menu == "Dashboard":
        display_dashboard()
    elif menu == "Alarm":
        alarm.run()
    elif menu == "Aktivitas":
        kalender.run()
    elif menu == "To-Do List":
        tugas.run()
    elif menu == "Prioritas & Kategori":
        kategori.run()

if __name__ == "__main__":
    main()


# Tambahkan CSS untuk styling tambahan

st.markdown("""

<style>

.main {background-color: #DE4F5;}
.stSidebar {background: #F5F5F5;}
.stSidebarContent {color: #000000;} /* Mengubah warna font sidebar menjadi hitam */
.stButton>button {background-color: #A9A9A9; color: white; border: none; padding: 10px 20px; cursor: pointer; transition : 0.3s;}
.stButton>button:hover {background-color: #A9A9A9;}
.stTextInput>div>input {border: 2px solid #A9A9A9; border-radius: 5px;}
            
</style>

""", unsafe_allow_html=True)    

    

