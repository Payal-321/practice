import threading
import time

# Define a custom thread class
class MyThread(threading.Thread):
    def __init__(self, name, delay):
        super().__init__()
        self.name = name
        self.delay = delay

    def run(self):
        print(f"Thread {self.name} starting.")
        time.sleep(self.delay)
        print(f"Thread {self.name} finished after {self.delay} seconds.")

# Create instances of the custom thread
if __name__ == "__main__":
    thread1 = MyThread("Thread-1", 2)
    thread2 = MyThread("Thread-2", 3)

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()

    print("All threads finished.")
