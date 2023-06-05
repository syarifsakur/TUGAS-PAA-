#NAMA : SYARIF MOHAMMAD SYAKUR
#NIM : F55121020

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Membuat data acak dengan 10000 elemen
data = random.sample(range(1, 10001), 10000)

# Mengeksekusi Bubble Sort dan mengukur waktu eksekusi lumayan cepat
start_time = time.time()
bubble_sort(data)
end_time = time.time()
execution_time = end_time - start_time
print("Waktu eksekusi lumayan cepat: %.5f detik" % execution_time)

# Mengacak ulang data
random.shuffle(data)

# Mengeksekusi Bubble Sort dan mengukur waktu eksekusi lumayan lambat
start_time = time.time()
bubble_sort(data)
end_time = time.time()
execution_time = end_time - start_time
print("Waktu eksekusi lumayan lambat: %.5f detik" % execution_time)
