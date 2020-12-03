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
 1. Apabila Dict `Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
 ```python
 def lihat():
    print("Daftar Mahasiswa")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
 ```
Seperti gambar berikut.
 
![Lihat-null](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/L-0.PNG)
 
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

#### Ubah()
1. Apabila Dict `Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
 ```python
 def ubah():
    print("Ubah Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
 ```
Seperti gambar berikut
 
![ubah-0](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/U-0.PNG)
 
2. Function **ubah()** dijalankan berdasarkan nama
- Memasukan nama sebagai key dan akan memunculkan isi data dari key tersebut
- Jika salah memasukkan nama, maka akan mengeluarkan "data nama tidak ditemukan!"
- Selanjutnya akan diberi pilihan apa yang ingin diubah, jika ingin membatalkan maka ketik 0
- Jika salah memasukkan pilihan maka mengeluarkan "Pilihan input tidak ada! Silahkan masukan [1-3]"
 ```python
else:
   nama = input("Masukan nama : ")
   if nama in Data_Mahasiswa.keys():
      print(f"Nama        = {nama}")
      print(f"NIM         = {Data_Mahasiswa[nama][0]}")
      print(f"Nilai Tugas = {Data_Mahasiswa[nama][1]}")
      print(f"Nilai UTS   = {Data_Mahasiswa[nama][2]}")
      print(f"Nilai UAS   = {Data_Mahasiswa[nama][3]}")
      print(25*"=")
      print("1. Nama\n2. NIM\n3. Nilai\n0. Kembali")
      tanya = int(input("Apa yang ingin diubah? [1-3] : "))
      ...      
      elif tanya == 0:
          pass
          
      else:
          print(f"Pilihan {tanya} tidak ada! Silahkan masukan [1-3]")
   else:
      print(f"Data {nama} tidak ditemukan!") 
 ```
 Maka program akan seperti berikut.
 
 ![ubah-1](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/U-1.PNG)
 
 ##### Ubah Nama
 Memasukan nama baru, nama akan berubah, maka akan mengeluarkan "Berhasil merubah Nama!"
 ```python
 if tanya == 1:
    _nama = input("Masukan Nama Baru : ")
    Data_Mahasiswa[_nama] = Data_Mahasiswa.pop(nama)
    print("Berhasil merubah Nama! ")
 ```
 Maka program ubah nama akan seperti berikut.

![ubah nama](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/U-N.PNG)

##### Ubah NIM
Memasukan NIM baru, NIM akan berubah, maka akan mengeluarkan "Berhasil merubah NIM!"
```python
elif tanya == 2:
    _nim = input("Masukan Nim Baru : ")
    Data_Mahasiswa[nama][0] = _nim
    print("Berhasil merubah NIM!")
```
Maka program ubah Nim akan seperti berikut.

![ubah nim](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/U-NIM.PNG)

##### Ubah Nilai
Memasukan nilai baru, nilai akan berubah, maka akan mengeluarkan "Berhasil merubah data nilai!"
```python
elif tanya == 3:
    _nilaiTugas = int(input("Masukan Nilai Tugas Baru : "))
    _nilaiUTS = int(input("Masukan Nilai UTS Baru : "))
    _nilaiUAS = int(input("Masukan Nilai UAS Baru : "))
    _nilaiAkhir = _nilaiTugas * 30/100 + _nilaiUTS * 35/100 + _nilaiUAS * 35/100
    Data_Mahasiswa[nama][1:4] = _nilaiTugas, _nilaiUTS, _nilaiUAS, _nilaiAkhir
    print("Berhasil merubah data nilai!")
```
Maka program ubah Nilai akan seperti berikut.

![ubah nilai](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/U-Nilai.PNG)

#### Hapus()
1. Apabila Dict `Data_Mahasiswa` masih kosong maka akan memanggil function `tidakAdaData`
```python
def hapus():
    print("Hapus Data Mahasiswa berdasarkan Nama")
    if len(Data_Mahasiswa) <= 0:  
        tidakAdaData()
```
Seperti gambar berikut.

![hapus 0](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/H-0.PNG)

2. Program Hapus Data Dijalankan
- Memasukan nama sebagai key data yang ingin dihapus
- Jika salah memasukan nama ,maka akan mengeluarkan "data nama tidak ditemukan!"
```python
else:
     nama = str(input("Masukan nama : "))
     if(nama in Data_Mahasiswa):
         del Data_Mahasiswa[nama]
         print(f"Data {nama} berhasil dihapus!")
     else:
         print(f"Data {nama} tidak ditemukan!") 
```
Maka program Hapus Data akan seperti berikut.

![Hapus](https://github.com/RezaRiyaldi/pertemuan10/blob/master/gambar/H-1.PNG)
 
