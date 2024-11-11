from threading import Thread
import time

def thrd_func():
    print(f'Thread Function....!!!')

    time.sleep(5)

    print(f'End of thread function')

# Creating a thread does not mean that the thread is started, you need to 
# explicity start a thread.

# thrd.start() can only be used once for a thread otherwise 
# it will give a run time error

# thrd.join() is function is to wait for thread to finish, 
# write at the end of the main thread

# thrd.is_alive() is used to check is a thread is active or not

# thrd.identity, unique to thread is only assigned when thread is STARTED, name
# can be assigned while creating but not identity
# thrd.identity remains even after thread execution

# Check is thread is started and is already finished
"""
    thrd.ident != None and thrd.isalive() == False -> True
"""
thrd = Thread(target=thrd_func)
print(f'is thread alive - started yet: \t{thrd.is_alive()}')
# Starting Thread
thrd.start()

print(f'thread identity: \t{thrd.ident}')
print(f'thread running: \t{thrd.is_alive()}')
print(f'thread name: \t{thrd.name}')

# Waiting for thread to finish
thrd.join()

print(f'thread started and already finished: \t{(thrd.ident != None) and (thrd.is_alive() == False)}')

