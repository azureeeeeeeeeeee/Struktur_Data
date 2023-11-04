import streamlit as st
from RBT import *
import random

# Inisiasi kamus sebagai objek dari RedBlackTree()
kamus = RedBlackTree()

# Memasukkan beberapa kata    
kamus.insert('kucing', 'cat')
kamus.insert('guru', 'teacher')
kamus.insert('botol', 'bottle')
kamus.insert('baterai', 'battery')
kamus.insert('kunci', 'key')
kamus.insert('baju', 'shirt')
kamus.insert('ibu', 'mother')
kamus.insert('ayah', 'father')


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
        elif kata == 'detective':
            st.write('conan')
        elif kata == 'anime':
            st.image('pict/anime.jpg')
        elif kata == 'karateka':
            st.image('pict/karateka.jpg')
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
        elif kata == 'detektif':
            st.write('conan')
        elif kata == 'anime':
            st.image('pict/anime.jpg')
        elif kata == 'karateka':
            st.image('pict/karateka.jpg')
        else:
            translation = kamus.search_id(kata)
            st.write(translation)



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