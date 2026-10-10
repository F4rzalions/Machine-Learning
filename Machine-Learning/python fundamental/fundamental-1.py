def kali_dua(angka):
    return angka * 2

def tambah(a, b):
    hasil = a + b
    return hasil

print(kali_dua(10)) #output: 20
print(tambah(3, 7)) #output: 10

def hello_world():
    print("print")
    
hello_world() #output: print


#1.1  Function

def clean_text(text:str) -> str: #text:str = parameter(argumen) harus string, dan -> str = return harus string
    return text.strip().lower() #strip() = menghapus spasi, lower() = mengubah ke huruf kecil

hasil = clean_text(" HELLO AI  ")
print(hasil) #output: hello ai

def calculate_average(numbers: list[float]) -> float: #parameter harus list angka desimal, dan return desimal(float)
    if not numbers: 
        raise ValueError("Data tidak boleh kosong") #jika numbers kosong maka akan memunculkan valueerror
    
    return sum(numbers) / len(numbers) #jumlah [angka] / panjang or banyak [angka]

print(calculate_average([80, 90, 100])) #output: 90.0

#parameter, argument, return, scope, default parameter, *args, **kwargs, dan fungsi yang memanggil fungsi lain.


#1.2  list 
scores = [80, 90, 75] #bentuk list

scores.append(95) #menambah 95 ke akhir
scores[0] = 85 #mengubah indeks 0 menjadi 85

print(scores) #output: 85, 90, 75, 95
print(scores[1]) #output: 90
print(scores[:2]) #output: 80, 90

#append(x) = menambah
#remove(x) = menghapus berdasar nilai
#pop(x) = menghapus sekaligus mengambil item
#lem(x) = menghitung jumlah item
#x[i] = mengakses indeks trtentu
#x[start:end] = mengambil sebagian data


#1.3  Tuple
image_size = (224, 244, 3) #bentuk tuple

height, width, channels = image_size #(224) = height, (224) = width, (3) = channels
print(width) #output: 244

#cocok untuk data yang merepresentasikan sekumpulan nilai tetap, seperti: gambar, kkordinat atau konfigurasi tertentu
#note: berisi objek mutable masih bisa memiliki objek yang berubah isinya, jadi tidak otomatis semua data immutable


#1.4  Dictionary
student = {
    "name": "Farzalions",
    "major": "Computer Science",
    "semester": 3
}

print(student["name"]) #output: Farzalions

student["semester"] = 4 #update semester value
student["gpa"] = 3.8 #menambahkan gpa ke dictionary student

print(student) 

## contoh pada ai ##

prediction = {
    "text": "produk ini bagus",
    "label": "positive",
    "confidence": 0.94
}

print(prediction["label"])

#Dictionary sering digunakan untuk merepresentasikan data JSON, hasil prediksi, konfigurasi model, dan respons API.
#Gunakan .get() ketika key mungkin tidak tersedia

confidence = prediction.get("confidence", 0.0)


#1.5  Set
# menyimpan nilai unikm dan mendukung operasi himpunan
words = ["AI", "Python", "AI", "ML", "Python"]
unique_words = set(words) #set  hanya menyimpan elemen unik sehingga duplikat otomatis dibuang

print(unique_words)

vocabulary_a = {"python", "model", "data"}
vocabulary_b = {"data", "model", "training"}

print(vocabulary_a & vocabulary_b) #irisan, hanya item sama yang dtampilkan
print(vocabulary_a | vocabulary_b) #union, semua item ditampilkan


#1.6 comprehension
#cara ringkas untuk membuat collection dari iterable

square = []

for numbers in range(5):
    square.append(numbers ** 2) #loop biasa 
#loop tradisional lalu menambahkan hasil kuadrat setiap angka menggunakan metode append
    
square = [numbers ** 2 for numbers in range(5)] #list comprehension
print(square) #output: 0,1,4,9,16
#cara yang lebih ringkas dan pythonic

positive_score = [
    score for score in [-2, 5, 0, 9, -1]
    if score > 0
]
print(positive_score) #output: 5, 9
#melakukan loop lalu menfilter bilangan genap 

x = []

#list comprehension 
square = [x * 2 for x in range(5)] #menghasilkan list berisi angka dari 0 sampai 4 yang masing masing dikalikan 2
#output: 0,2,4,6,8

#Dictionary comprehension
square = {x: x ** 2 for x in range(5)} #menghasilkan dictionary  dengan kunci berupa angka x dan nilai berupa kuadratnya
#output: {0: 0, 1: 2, 2: 4, 3: 9, 4: 16}

#set comprehension
square = {x %3 for x in range(10)} #menghasilkan sekumpulan set dari sisa bagi(modulo) 
#output: 0,1,2