from basic_task import *
from thread_task import *

class MultyTask:
    pass

class MultyTask:
    def __init__(self):
        
        self.called = False
        self.calling = False
        self.finished = False
        self.result_ = None

    def fetch(self):
        # self.finished = False
        return self.result_
    
    def __call__(self, *args, **kwargs):
        print("Multytaks is not supposed to be called directly!")
        
        return self
    
    def join(self, *args, **kwargs):
        print("Multytaks is not supposed to be joined directly!")
        
        return self