bil_awal = 1
bil_sebelas = 11
kelipatan = int(input("Deret dengn Kelipatan: "))


for i in range(bil_awal, bil_sebelas+1):
    akhir = bil_awal*(kelipatan**(i-1))
    hasil = akhir
    print(akhir)

print("\n", "Deret: ", kelipatan, "suku ke-11: ", hasil)
