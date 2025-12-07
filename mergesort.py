

## 🧾 Source Code (mergesort.py)

# Program MergeSort (Urutan dari BESAR ke KECIL)

def merge_sort(arr):
    # Jika panjang array 1 atau kosong, langsung kembalikan (sudah terurut)
    if len(arr) <= 1:
        return arr

    # Mencari titik tengah
    mid = len(arr) // 2

    # Bagi 2 bagian
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Gabungkan sambil diurutkan
    return merge(left, right)


def merge(left, right):
    hasil = []
    i = j = 0

    # Bandingkan elemen kiri & kanan
    # Gunakan > agar hasil menjadi BESAR → KECIL
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            hasil.append(left[i])
            i += 1
        else:
            hasil.append(right[j])
            j += 1

    # Tambahkan sisa elemen jika masih ada
    hasil.extend(left[i:])
    hasil.extend(right[j:])

    return hasil


# Data yang diberikan
data = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

print("Data sebelum diurutkan:", data)

hasil = merge_sort(data)

print("Data setelah diurutkan (dari besar ke kecil):")
print(hasil)
