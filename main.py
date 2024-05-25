import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)   # ini variable dengan library random integer


print("*****************************") # TAMPILAN LUAR GAMES
print(f"** {welcome_message} **")   
print("*****************************")

nama_user = input ("masukan nama anda: ") # INPUT NAMA 

bentuk_goa = "|_|" # VARAIBEL BENTUK GOA
goa = [bentuk_goa] * 4 # INI HARUS TETAP KOSONG 

goa_kosong = goa.copy() #  INI ADALAH TEMPAT BARU UNTUK SI CUYPY

goa[cuypy_position - 1] = "|0_0|"


print (f''' Hallo {nama_user}! Coba perhatikan gambar dibawah ini
       {goa_kosong}
       ''')

pilihan_user = int(input ("Menurut kamu GOA nomor berapa CUYPAY berada? [1 / 2 / 3 / 4]: "))

confirm_answer = input (f"Apakah kamu yakin jawabannya adalah? {pilihan_user}?[y/n]:")

if confirm_answer == "n":
    print ("PROGRAM DIHENTKAN!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"{goa} \n SELAMAT KAMU MENANG !")
    else:
        print (f"{goa} \n MAAF KAMU KALAH !, CUYPY BERADA DI {cuypy_position}")
else:
    print("SILAHKAN ULANGI PROGRAMNYA!")
exit() 
        