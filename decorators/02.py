import time

def timer (fun):
    def wrapper(*args,**kwargs):
        start=time.time()
        print(fun(*args,**kwargs))
        end=time .time()
        return f"{fun.__name__}={end-start}"
    return wrapper
@timer   
def hello (name):
    r=time.sleep(2)
    return f"hello!,{name}"

print(hello("satyam"))


