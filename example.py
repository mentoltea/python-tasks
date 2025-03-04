from taks import *
import time

def f(x, **kwargs):
    if 'chained' in kwargs:
        x = kwargs['chained']
    
    print(f"processing {x}...")
    time.sleep(1)
    print("finished")
    return x**2
    
    
jt = ChainedTask(
    [
        BasicTask(f, 3),
        BasicTask(f)
    ]
)


print(fetch_unnest( jt().join() ))
