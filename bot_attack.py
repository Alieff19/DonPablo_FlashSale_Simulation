import threading
import requests
import time

URL = "http://localhost/beli"
TOTAL_REQUESTS = 500  # 500 orang
CONCURRENT_USERS = 50 # 50 orang serentak

success = 0
fail = 0

def serang(i):
    global success, fail
    try:
        r = requests.post(URL, timeout=5)
        if r.json()['status'] == 'success':
            success += 1
            print(f"\033[92mUser {i}: BERHASIL\033[0m")
        else:
            fail += 1
            print(f"\033[91mUser {i}: GAGAL (Stok Habis)\033[0m")
    except:
        print(f"User {i}: Connection Retry...")

print(f"--- MEMULAI FLASH SALE WAR ({TOTAL_REQUESTS} Requests) ---")
threads = []
for i in range(TOTAL_REQUESTS):
    t = threading.Thread(target=serang, args=(i,))
    threads.append(t)
    t.start()
    if i % CONCURRENT_USERS == 0: time.sleep(0.1)

for t in threads: t.join()
print(f"\n--- HASIL: Sukses={success} | Gagal={fail} ---")