a = str(input("Masukan Provider Anda : "))
b = float(input("Masukan IPK Anda : "))

if (a) == "Telkomsel" and (b) >= 3 :
    print(a,b, "Selamat Anda Mendapatkan Iphone X")

elif (a) == "Telkomsel" and 2.75 <= (b) <= 3 :
    print(a,b, "Selamat Anda Mendapatkan PS 4")

elif (a) == "Telkomsel" and 2.25 <= (b) <= 2.75 :
    print(a,b, "Voucher OYO")

else:
    print(a,b, "Anda Tidak Terdaftar")