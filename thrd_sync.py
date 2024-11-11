import time
import threading
from threading import Thread

"""
    Multi Threading - Thread Sync using Mutual Exclusion (Only occupied by 1 person)

    Why we need Thread Sync? Mutex
    -> Resources shared across threads, there is no mutual exculsion, we do not know 
    thread behaviour and how and in what order threads will execute.
    -> Solution is Mutex Locks

    -> Locks as a function argument
"""
# Global Mutex Thread Lock
lock = threading.Lock()

def first_person(lock):
    # Acquire the lock
    lock.acquire()

    print(f'person - 1 occupies the meeting room - 1')
    time.sleep(0.5)
    print(f'person - 1 vacates the meeting room - 1')

    # Release the lock
    lock.release()

def second_person(lock):
    # Acquire the lock, but instead of blocking and waiting for acquiring
    # check is lock is already blocked if it is wait for it to get free
    # instead of trying to acquiring this saves us from a deadlock situation
    # where the lock you want is already locked in some other place and now
    # nothing moves
    while True:
        if lock.acquire(blocking=False) is True:
            break
        else:
            print('Lock is Not Free')
            time.sleep(0.1)

    print(f'person - 2 occupies the meeting room - 1')
    time.sleep(0.5)
    print(f'person - 2 vacates the meeting room - 1')

    # Release the lock
    lock.release()
    
# Creating 2 threads 
thrd1 = Thread(target=first_person, args=(lock,))
thrd2 = Thread(target=second_person, args=(lock,))

thrd1.start()
thrd2.start()

# Waiting for completion
thrd1.join()
thrd2.join()