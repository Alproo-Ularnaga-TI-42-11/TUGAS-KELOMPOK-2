print("Start")
a = 1500000

print("Project Ular Naga Group")

print("Link.aja #BeresTanpaCash")
print("Pilih Menu")
print("\n1. Cek Saldo\n2. Debit\n3. Credit")
menu = int(input("Pilih menu : "))

if menu ==1:
    print("Rp. ",a)

if menu ==2:
    print("Top Up")
    Debit = float(input("Debit link = Rp "))
    x = a+Debit
    print("Saldo Total = Rp ",x)
    print("Selamat! Transaksi Berhasil")

if menu ==3:
    print("Pilih nominal yang mau diambil")
    Kredit = eval(input("Kredit link = Rp "))

    if a > Kredit:
        print("Nilai saldo mencukupi")
        Sisa_Saldo_Total = a - Kredit
        print("Sisa Saldo Total = Rp ",Sisa_Saldo_Total)
        print("Selamat! Transfer Berhasil")
    if a < Kredit:
        print("Nilai saldo tidak mencukupi")
        print("Maaf! Saldo Anda Tidak Mencukupi")
print("End")

