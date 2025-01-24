import threading

def bar():
    for _ in range(5):
        print("Hello")

my_thread = threading.Thread(target=bar, daemon=True)

my_thread.start()

my_thread.join()

print("finish")
