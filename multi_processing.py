"""
    MultiProcessing for CPU intensive jobs, creates multiple processes
    to run them in parallel,
    Processes are heavier than threads, but slower than threads thats 
    why they use more resources
"""
import multiprocessing as mp
from multiprocessing import Process
import time

def process_fn():
    print(f'This is a new Process')
    time.sleep(5)
    print(f'This proc is {mp.current_process()}')

def main_fn():
    proc = Process(target=process_fn, name="Sample Process")

    proc.start()
    proc.join()

if __name__ == "__main__":
    main_fn()