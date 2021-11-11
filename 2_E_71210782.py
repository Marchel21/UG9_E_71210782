#program membalik nama belakang menajdi nama depan dan menampilkan tempat tanggal lahir
nama = input("Nama: ")
lahir = input("Tempat tanggal lahir : ")

#proses
a = nama.split()
b = lahir.split()

#print hasil
print("Haloo!", a[1], ",", a[0])
print("Anda lahir di", b[0], "pada tanggal", b[1], b[2], b[3])


#program membalik nama belakang menajdi nama depan dan menampilkan tempat tanggal lahir
nama = input("Nama:")
lahir = input("Tempat tanggal lahir:")

#proses
a = nama.split()
b = lahir.split()

#print hasil
print("Haloo!", a[2],",",a[0],a[1])
print("Anda lahir di",b[0],"pada tanggal",b[1],b[2],b[3])
