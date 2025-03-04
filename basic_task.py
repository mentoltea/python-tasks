from typing import Callable, Any, Literal

class BasicTask:
    def __init__(self, 
                task: Callable,
                *args,
                **kwargs
                ):
        self.task = task
        self.args = args
        self.kwargs = kwargs
        
        self.called = False
        self.calling = False
        self.finished = False
        self.result_ = None
        
    def __call__(self, *args, **kwds) -> Any:
        if (not self.calling):
            self.called = True
            
            self.calling = True
            self.finished = False
            
            self.result_ = self.task(*self.args, **self.kwargs)
            
            self.calling = False
            self.finished = True
        
        
        return self
    
    def fetch(self):
        # self.finished = False
        return self.result_
    
    def join(self):
        return self
    
