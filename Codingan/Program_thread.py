import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Thread 1: {i}")
        time.sleep(1)

def print_letters():
    for letter in "ABCDE":
        print(f"Thread 2: {letter}")
        time.sleep(1)

# Membuat thread
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Menjalankan thread
thread1.start()
thread2.start()

# Menunggu kedua thread selesai
thread1.join()
thread2.join()

print("Selesai!")
