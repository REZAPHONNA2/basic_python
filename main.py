import random

welcome_message = "WELCOME TO CUYPY GAMES!"
cuypy_position = random.randint(1, 4)


print("*****************************")
print(f"** {welcome_message} **")
print("*****************************")

nama_user = input ("masukan nama anda: ")

print (f''' Hallo {nama_user}! Coba perhatikan gambar dibawah ini 
       |_| |_| |_| |_|
       ''')

pilihan_user = int(input ("Menurut kamu GOA nomor berapa CUYPAY berada? [1 / 2 / 3 / 4]: "))

confirm_answer = input (f"Apakah kamu yakin jawabannya adalah? {pilihan_user}?[y/n]:")

if confirm_answer == "n":
    print ("PROGRAM DIHENTKAN!")
    exit()
elif confirm_answer == "y":
    if pilihan_user == cuypy_position:
        print(f"SELAMAT {nama_user} KAMU MENANG! posisi CUYPY ada di GOA nomor {cuypy_position} dan pilihanmu adalah GOA nomor {pilihan_user}.")
    else:
        print (f"KAMU KALAH! CUYPY BUKAN BERADA DISITU, Tapi Ada di GOA nomor {cuypy_position}. Sedangkan kamu memilih GOA nomor {pilihan_user} ")
else:
    print("SILAHKAN ULANGI PROGRAMNYA!")
exit()
        