import threading

def print_numbers():
    for i in range(5):
        print(i)

# Create a thread that will execute the print_numbers function
thread = threading.Thread(target=print_numbers)
# Start the thread
thread.start()
# Wait for the thread to finish
thread.join()
