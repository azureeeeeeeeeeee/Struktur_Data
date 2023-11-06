import streamlit as st
from RBT import *
import random

# Inisiasi kamus sebagai objek dari RedBlackTree()
kamus = RedBlackTree()

# Memasukkan beberapa kata    
kamus.insert('kucing', 'cat', 'kucing adalah hewan', 'cat is animal')
kamus.insert('guru', 'teacher', 'guru itu baik', 'teacher is good')
kamus.insert('botol', 'bottle', 'botol adalah barang', 'bottle is item')
kamus.insert('baterai', 'battery', 'baterai bagus', 'battery is good')
kamus.insert('kunci', 'key', 'kunci hebat', 'key is great')
kamus.insert('baju', 'shirt', 'baju itu bagus', 'that shirt is good')
kamus.insert('ibu', 'mother', 'ibu itu cewek', 'mother is woman')
kamus.insert('ayah', 'father', 'ayah itu laki laki', 'father is a man')


# Membuat web page dengan menggunakan streamlit
st.header('Kamus ENG - IDN')

tab1, tab2 = st.tabs(['EN - ID', 'ID - EN'])
with tab1:
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            kata = st.text_input('Masukkan Kata (EN)')
            kata = kata.lower()

        with col2:
            st.write('Arti (ID) : ')
            if kata == 'random':
                st.write('acak')
            elif kata.startswith('odd'):
                st.write('ganjil')
            elif kata.startswith('even'):
                st.write('genap')
            else:
                translation = kamus.search_en(kata)
                st.write(translation)

    with st.expander('Description', expanded=True):
        if kata.startswith('odd'):
            arr = kata.strip().split()
            if len(arr) < 2:
                st.write('odd is bad')
            elif len(arr) == 2:
                _, num = arr[0], int(arr[1])
                arrodd = [x for x in range(1, num*2, 2)]
                for i in arrodd:
                    st.write(i)
            else:
                st.write('Description not found')
    
        elif kata.startswith('even'):
            arr = kata.strip().split()
            if len(arr) < 2:
                st.write('even is good')
            elif len(arr) == 2:
                _, num = arr[0], int(arr[1])
                arrodd = [x for x in range(0, num*2, 2)]
                for i in arrodd:
                    st.write(i)
            else:
                st.write('Description not found')

        elif kata == 'random':
            arr = [random.randint(1,100) for x in range(10)]
            for i in arr:
                st.write(i)

        else:
            desk = kamus.search_descen(kata)
            if desk != 'Not Found':
                st.write(desk)
            else:
                st.write('Description not found')


with tab2:
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            kata = st.text_input('Masukkan Kata (ID)')
            kata = kata.lower()

        with col2:
            st.write('Arti (EN) : ')
            if kata == 'acak':
                st.write('random')
            elif kata.startswith('ganjil'):
                st.write('odd')
            elif kata.startswith('genap'):
                st.write('even')
            else:
                translation = kamus.search_id(kata)
                st.write(translation)

    with st.expander('Deskripsi', expanded=True):
        if kata.startswith('ganjil'):
            arr = kata.strip().split()
            if len(arr) < 2:
                st.write('ganjil adalah bagus')
            elif len(arr) == 2:
                _, num = arr[0], int(arr[1])
                arrodd = [x for x in range(1, num*2, 2)]
                for i in arrodd:
                    st.write(i)
            else:
                st.write('Deskripsi tidak ditemukan')
    
        elif kata.startswith('genap'):
            arr = kata.strip().split()
            if len(arr) < 2:
                st.write('genap adalah bagus')
            elif len(arr) == 2:
                _, num = arr[0], int(arr[1])
                arrodd = [x for x in range(0, num*2, 2)]
                for i in arrodd:
                    st.write(i)
            else:
                st.write('Deskripsi tidak ditemukan')

        elif kata == 'acak':
            arr = [random.randint(1,100) for x in range(10)]
            for i in arr:
                st.write(i)
            
        else:
            desk = kamus.search_descid(kata)
            if desk != 'Not Found':
                st.write(desk)
            else:
                st.write('Deskripsi tidak ditemukan')


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