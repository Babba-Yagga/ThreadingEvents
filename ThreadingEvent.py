from threading import Thread, Event
from time import sleep


def task(event: Event) -> None:
    for i in range(1, 100):
        print(f'Running... #{i}')
        sleep(.25)
        if i % 10 == 0 and event.is_set():
            print('The thread was stopped prematurely.')
            break
    else:
        print('The thread was stopped maturely.')


def main() -> None:

    event = Event()
    thread = Thread(target=task, args=(event,))
    
    # start the thread
    thread.start()

    # suspend the main thread after 5 seconds
    sleep(5)

    # stop the child thread
    event.set()    
   

if __name__ == '__main__':
    main()