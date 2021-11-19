from datetime import datetime as dt


def hello_world():
    print("Hello!")
    
    
def time_function(func):
    time_before = dt.now()
    func()
    time_after = dt.now()
    time_dif_ms = (time_after-time_before).total_seconds()*1000
    print(f"Function took {time_dif_ms} milliseconds to run")
    
   
def time_function2(func):
    def wrapper():
        time_before = dt.now()
        func()
        time_after = dt.now()
        time_dif_ms = (time_after-time_before).total_seconds()*1000
        print(f"Function took {time_dif_ms} milliseconds to run")
    return wrapper
    
    
@time_function2
def hello_world2():
    print("Hello!")
    
    
if __name__ == '__main__':
    time_function(hello_world)
    hello_world2()
