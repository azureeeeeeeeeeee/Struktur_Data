import streamlit as st
from RBT import *
import random

# Inisiasi kamus sebagai objek dari RedBlackTree()
kamus = RedBlackTree()
    
# Helper Function
def load_data(filename='data.txt'):
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    idn, eng = parts[0], parts[1]
                    kamus.insert(idn, eng)
    except FileNotFoundError:
        pass

def save_data(data, filename='data.txt'):
    with open(filename, 'w') as file:
        for idn, eng in data.items():
            file.write(f"{idn},{eng}\n")

# Load data
data = load_data()


# Membuat web page dengan menggunakan streamlit
st.header('Kamus ENG - IDN')

tab1, tab2 = st.tabs(['EN - ID', 'ID - EN'])
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        kata = st.text_input('Masukkan Kata (EN)')
        kata = kata.lower()

    with col2:
        st.write('Arti (ID) : ')
        if kata == 'random':
            arr = [random.randint(1,100) for x in range(10)]
            for i in arr:
                st.write(i)
        elif kata.startswith('odd'):
            if len(kata.split()) == 1:
                st.write('ganjil')
            else:
                mode, num = kata.strip().split()
                num = int(num)
                odd = [x for x in range(1, num*2, 2)]
                for i in odd:
                    st.write(i)
        elif kata.startswith('even'):
            if len(kata.split()) == 1:
                st.write('genap')
            else:
                mode, num = kata.strip().split()
                num = int(num)
                even = [x for x in range(0, num*2, 2)]
                for i in even:
                    st.write(i)
        else:
            translation = kamus.search_en(kata)
            st.write(translation)

with tab2:
    col1, col2 = st.columns(2)
    with col1:
        kata = st.text_input('Masukkan Kata (ID)')
        kata = kata.lower()

    with col2:
        st.write('Arti (EN) : ')
        if kata == 'acak':
            arr = [random.randint(1,100) for x in range(10)]
            for i in arr:
                st.write(i)
        elif kata.startswith('ganjil'):
            if len(kata.split()) == 1:
                st.write('odd')
            else:
                mode, num = kata.strip().split()
                num = int(num)
                odd = [x for x in range(1, num*2, 2)]
                for i in odd:
                    st.write(i)
        elif kata.startswith('genap'):
            if len(kata.split()) == 1:
                st.write('even')
            else:
                mode, num = kata.strip().split()
                num = int(num)
                even = [x for x in range(0, num*2, 2)]
                for i in even:
                    st.write(i)
        else:
            translation = kamus.search_id(kata)
            st.write(translation)



st.header('Input Kata Baru (ID) & (EN)')
ind = st.text_input('Masukkan kata (ID)')
eng = st.text_input('Masukkan Arti (EN)')

btn = st.button('Input')
if btn:
    if ind and eng:
        kamus.insert(ind.lower(), eng.lower())
        data[ind.lower()] = eng.lower()
        save_data(data)
        pesan = f'Berhasil memasukkan {ind} (ID) dan {eng} (EN) ke kamus'
        st.write(pesan)
    else:
        st.write('Belum Memasukkan apa apa')



st.header('Print Tree di Terminal')
col1, col2 = st.columns(2)
with col1:
    tree_en = st.button('Print RBT (EN)')
    if tree_en:
        print('\n\nRBT Untuk kata EN :')
        kamus.print_tree_en()
with col2:
    tree_id = st.button('Print RBT (ID)')
    if tree_id:
        print('\n\nRBT Untuk kata ID :')
        kamus.print_tree_id()