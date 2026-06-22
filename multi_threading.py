import threading
import time

start_time = time.time()  # to measure the time taken to complete all chores

def walk_dog(first, last="Holt"):
    time.sleep(8)
    print(f"You finished walking {first} {last}.")


def take_out_trash():
    time.sleep(2)
    print("You took out the trash.")


def get_emails():
    time.sleep(3)
    print("You checked your emails.")

# all these fns will run in same single main thread sequeentailly, so it takes time
# walk_dog()
# take_out_trash()
# get_emails()


chore1 = threading.Thread(target=walk_dog,args=("Brandy",), kwargs={"last": "Holt"})  # note that, we have to give comma if only one member in the tuple, creating a thread for walk_dog fn
chore1.start()  # starts the thread and runs the walk_dog fn in that thread

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_emails)
chore3.start()

chore1.join()  # waits for chore1 thread to finish before moving to next line of code
# by the time chore1 is done which is 8 sec, the chore2 and chore3 are alredy done parallely with 2 sec and 3 sec resp, so the joins of chore2 and chore3 threads will immediately go to next line
chore2.join()  # waits for chore2 thread to finish before moving to next line of code
chore3.join()  # waits for chore3 thread to finish before moving to next line of code

print(f"All chores completed in {time.time() - start_time:.2f} seconds.")