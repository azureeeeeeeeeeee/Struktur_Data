from RBT import *
import random

kamus = RedBlackTree()


while True:
    try:
        option = int(input(
            'Menu : \n1. Cari kata\n2. Masukkan kata baru\n3. Print Tree\n4. Keluar\nMasukkan Pilihan : '))
        if option == 1:
            bahasa = int(input('1. ID -> EN\n2. EN -> ID\nMasukkan pilihan Bahasa : '))
            if bahasa == 1:
                kata = input('Masukkan kata yang ingin dicari (ID) : ').lower()
                if kata == 'random':
                    print([random.randint(1, 101) for x in range(10)])
                    print()
                elif kata == 'anime':
                    print('Detective Connan\n')
                elif kata == 'death note':
                    print('My handmade\nkakkoi desu yo\n')
                elif kata == 'boby':
                    print('Hilang dari lms')
                else:
                    print('Arti (EN) : ', end="")
                    kamus.search_en(kata)
                    print()

            elif bahasa == 2:
                kata = input('Masukkan kata yang ingin dicari (EN) : ').lower()
                if kata == 'random':
                    print([random.randint(1, 101) for x in range(10)])
                    print()
                elif kata == 'anime':
                    print('Detective Connan\n')
                elif kata == 'death note':
                    print('My handmade\nkakkoi desu yo\n')
                elif kata == 'boby':
                    print('Hilang dari lms')
                else:
                    print('Arti (ID) : ', end="")
                    kamus.search_id(kata)
                    print()
            else:
                print('Invalid Command!')

        elif option == 2:
            kata = input('Masukkan Kata (ID) : ').lower()
            arti = input('Masukkan Arti (EN) : ').lower()
            kamus.insert(kata, arti)

        elif option == 3:
            kamus.print_tree()

        elif option == 4:
            print('Goodbye !!')
            break

        else:
            print('Invalid Command!')
    except ValueError:
        print('Input bukan angka\n')
