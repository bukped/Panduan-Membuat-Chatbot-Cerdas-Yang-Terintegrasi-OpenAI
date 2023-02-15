# Variabel:
# integer variable
from math import *
from math import cos, pi
import math as m
import math
x = 5

# string variable
name = "John"

# boolean variable
is_student = True

# list variable
marks = [75, 80, 90]

# dictionary variable
person = {"name": "John", "age": 25}

# Operasi Aritmatika
# Penjumlahan
x = 5
y = 3
result = x + y
print(result)  # Output: 8

# Pengurangan
x = 5
y = 3
result = x - y
print(result)  # Output: 2

# Perkalian
x = 5
y = 3
result = x * y
print(result)  # Output: 15

# Pembagian
x = 5
y = 3
result = x / y
print(result)  # Output: 1.6666666...

# Percabangan
#  contoh if
x = 5
if x > 0:
    print("x positif")

# contoh if-else
x = 5
if x > 0:
po
print("x positif")
else:
    print("x negatif")

# contoh if-elif-else
x = 5
if x > 0:
    print("x positif")
elif x == 0:
    print("x sama dengan 0")
else:
    print("x negatif")

# Perulangan
# contoh for loop
for i in range(5):
    print(i)

# output: 0 1 2 3 4

# contoh for loop dengan list
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    print(fruit)

# output: apple banana mango

# contoh while loop
i = 0
while i < 5:
    print(i)
    i += 1
# output: 0 1 2 3 4
= 5
if x > 0:
    print("x positif")
elif x == 0:
    print("x sama dengan 0")
else:
    print("x negatif")

# Fungsi
# contoh function tanpa parameter


def greet():
    print("Hello, World!")


greet()  # Output: Hello, World!


# contoh function dengan parameter
def add(x, y):
    result = x + y
    print(result)


add(5, 3)  # Output: 8

# contoh function dengan return value


def multiply(x, y):
    result = x * y
    return result


result = multiply(5, 3)
print(result)  # Output: 15

# String
# contoh concatenation string
name = "John"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")

# contoh string indexing
word = "hello"
print(word[0])  # Output: 'h'
print(word[-1])  # Output: 'o'

# contoh slicing string
word = "hello"
print(word[1:4])  # Output: 'ell'
print(word[:3])  # Output: 'hel'
print(word[2:])  # Output: 'llo'

# Exception handling
x  # contoh try-except
try:
    x = 5 / 0
except ZeroDivisionError:
    print("Tidak bisa membagi dengan 0")
# contoh try-except-else
try:
    x = 5 / 2
except ZeroDivisionError:
    print("Tidak bisa membagi dengan 0")
else:
    print(x)

# contoh try-except-finally
try:
    x = 5 / 2
except ZeroDivisionError:
    print("Tidak bisa membagi dengan 0")
finally:
    print("Proses selesai")

# contoh menangkap dan memberikan nama untuk exception
try:
    x = 5 / 0
except ZeroDivisionError as e:
    print(e)

# Modules:
# contoh import module
x = math.cos(math.pi)
print(x)  # Output: -1.0

# contoh import module dengan alias

x = m.cos(m.pi)
print(x)  # Output: -1.0

# contoh import function dari module

x = cos(pi)
print(x)  # Output: -1.0

# contoh import semua function dari module

x = cos(pi)
print(x)  # Output: -1.0
