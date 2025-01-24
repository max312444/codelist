import threading

my_lock = threading.Lock()

def bar():
    for count in range(1, 6):
        with my_lock:
            print(f"bar : {count}")

def foo():
    for count in range(1, 6):
        with my_lock:
         print(f"foo : {count}")
        
thread_1 = threading.Thread(target=bar)
thread_2 = threading.Thread(target=foo)

thread_1.start()
thread_2.start()

thread_1.join() # 1이 번저 join되거나 2가 먼저 join되거나 두개는 차이가 있음
thread_2.join()

print("finish")