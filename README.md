# Pertemuan 10
## Function

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Reza Riyaldi Irawan |
| **NIM** | 312010284 |
| **Kelas** | TI.20.A.2 |
| **Mata Kuliah** | Bahasa Pemrograman |

## Daftar Isi
* [Pertemuan 10](https://github.com/RezaRiyaldi/pertemuan10#pertemuan-10)
    * [Labspy04](https://github.com/RezaRiyaldi/Pertemuan9#Labspy-04) | [direktori](https://github.com/RezaRiyaldi/Pertemuan9/tree/main/Labspy04) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy04/labs04.py)
    * [Labspy05](https://github.com/RezaRiyaldi/Pertemuan9#Labspy-05) | [direktori](https://github.com/RezaRiyaldi/Pertemuan9/tree/main/Labspy05) | [Source Code](https://github.com/RezaRiyaldi/Pertemuan9/blob/main/Labspy05/labs05.py)
         * [Dictionary dan Variable](https://github.com/RezaRiyaldi/Pertemuan9/#--membuat-dictionary-sebagai-databasenya)
         * [Function Tambahan](https://github.com/RezaRiyaldi/Pertemuan9/#--membuat-function-tambahan-agar-bisa-dipanggil-ketika-dibutuhkan)
         * [Function Tambah Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-tambah-data)
         * [Function Lihat Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-lihat-data)
         * [Function Ubah Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-ubah-data)
         * [Function Hapus Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-hapus-data)
         * [Function Cari Data](https://github.com/RezaRiyaldi/Pertemuan9/#--function-cari-data)  
         * [Menu](https://github.com/RezaRiyaldi/Pertemuan9/#menu)
         
### Latihan 6
Konsep program :

![soal](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/soal.PNG)
Pada Latihan 6 ini saya akan menjelaskan program yang saya buat. Berikut [Source Code](https://github.com/RezaRiyaldi/pertemuan10/blob/master/latihan6.py)-nya

Penjelasan:
1. Merubah function menjadi lambda yang di deklarasikan ke a - d
```python
# Perpangkatan
# def a(x):
#     return x ** 2    
a = lambda x : x ** 2

# Perpangkatan dengan penjumlahan
# def b(x, y):
#     return x, y : x ** 2  + y ** 2
b = lambda x, y : x ** 2  + y ** 2

# Menghitung Rata - rata
# def c(*args):
#     return sum(args)/len(args)
c = lambda *args : sum(args)/len(args)

# Membuat huruf menjadi unik/acak
# def d(s):
#     return "".join(set(s))
d = lambda s: "".join(set(s))
```
2. Pemanggilan function lambda
```python
print(a(100))
print(b(5, 20))
print(c(-2, 10, 9, 7))
print(d("Reza"))
```

Maka hasil akan seperti berikut

![hasil lambda](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/hasil.PNG)

### Praktikum
Konsep Program :

Buat program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
- Fungsi tambah() untuk menambah data
- Fungsi tapilkan() untuk menampilkan data
- Fungsi hapus(nama) untuk menghapus data berdasarkan nama
- Fungsi ubah(nama) untuk mengubah

 Pada Praktikum ini saya akan menjelaskan program yang saya buat. Berikut [Source Code](https://github.com/RezaRiyaldi/pertemuan10/blob/master/praktikum.py)-nya
 
 Penjelasan
 
 1. Deklarasi Dictionary sebagai database
 ```python
 Data_Mahasiswa = {} 
 ```
 
 2. Membuat Function tambahan agar bisa dipanggil saat dibutuhkan
 ```python
 def garis():
    print(71*"=")

def header():
    garis()
    print("| {0:^2} | {1:^7} | {2:^18} | {3:^5} | {4:^5} | {5:^5} | {6:^7} |".format("No", "NIM", "Nama", "Tugas", "UTS", "UAS", "Akhir"))
    garis()

def tidakAdaData(): 
    header()          
    print("|{0:^69}|".format("TIDAK ADA DATA!!! Silahkan Tambah Data Terlebih Dahulu"))
    garis()
 ```
 
 3. Membuat Function Program
 #### Lihat()
 1. Apabila Dict Data_Mahasiswa masih kosong maka akan memanggil function tidakAdaData
 ```python
 def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
 ```
Seperti gambar berikut.
 
![Lihat-0](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/L-0.PNG)
 
2. Program Lihat Data Dijalankan
- Menggunakan looping untuk mengeluarkan data
- Dan menggunakan f-string agar tidak terlalu panjang dan format.string agar tampilan terlihat rapih
```python
else:
     no = 0
     header()
     for data in Data_Mahasiswa.items():
         no += 1 
         print(f"| {no:>2} | {data[1][0]:>7} | {data[0]:<18} | {data[1][1]:>5} | {data[1][2]:>5} | {data[1][3]:>5} | {data[1][4]:>7.2f} |")               
     garis() 
```
Seperti gambar berikut.
 
![Lihat-1](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/L-1.PNG)
 #### Tambah()
- Memasukan data
- Jika sudah, maka data akan dimasukkan kedalam Dict Data_Mahasiswa
- Dimana Nama sebagai key dan sisanya values yang dimasukkan kedalam list
- Jika berhasil maka akan mengeluarkan "Berhasil menambahkan data 'nama' dengan NIM : nim!"
 ```python
 def tambah():
    print("Tambah data")
    nim        = input("NIM         : ")
    nama       = input("Nama        : ")
    nilaiTugas = int(input("Nilai Tugas : "))
    nilaiUTS   = int(input("Nilai UTS   : "))
    nilaiUAS   = int(input("Nilai UAS   : "))
    nilaiAkhir = (nilaiTugas * 30/100) + (nilaiUTS * 35/100) + (nilaiUAS * 35/100)
    Data_Mahasiswa[nama] = [nim, nilaiTugas, nilaiUTS, nilaiUAS, nilaiAkhir]
    print(f"Berhasil menambahkan data '{nama}' dengan NIM : {nim}!") 
 ```
 Maka program cari data akan seperti berikut.
 
 ![tambah](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/T-1.PNG)

