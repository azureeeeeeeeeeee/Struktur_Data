import streamlit as st
from RBT import *
import random

kamus = RedBlackTree()


def load_data_from_file(filename='data.txt'):
    data = {}
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    idn, eng = parts[0], parts[1]
                    data[idn] = eng
                    kamus.insert(idn, eng)
    except FileNotFoundError:
        pass
    return data

def save_data_to_file(data, filename='data.txt'):
    with open(filename, 'w') as file:
        for idn, eng in data.items():
            file.write(f"{idn},{eng}\n")

data = load_data_from_file()

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
            st.write([random.randint(1, 100) for x in range(10)])
        # elif kata == 'anime':
        #     st.image('pict/anime.jpg')
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
        if kata == 'random':
            st.write([random.randint(1, 100) for x in range(10)])
        # elif kata == 'anime':
        #     st.image('pict/anime.jpg')
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
        save_data_to_file(data)
        pesan = f'Berhasil memasukkan {ind} (ID) dan {eng} (EN)'
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