'''
program to get use of scheduler and time module
'''
import sched, time
s = sched.scheduler(time.time, time.sleep)

'''
function print_time for getting defult time
'''
def print_time(a='defult'):
    print ("From print_time ",time.time(),a)


'''
function print_some_times for getting time from some_time function
'''
def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())

print_some_times()


