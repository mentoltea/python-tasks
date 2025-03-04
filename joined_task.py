from multytask import *


class JoinedTask(MultyTask):
    def __init__(self, 
                ts: list[ BasicTask | ThreadTask | MultyTask ]
                ):
        super().__init__()
        self.tasks = ts
        
        
    def __call__(self, *args, **kwds):
        if (not self.calling):
            self.called = True
            
            self.calling = True
            self.finished = False
            
            for t in self.tasks:
                self.result_ = t().join().fetch()
            
            self.calling = False
            self.finished = True
        
        return self
    
    def join(self, *args, **kwargs):
        if (self.called):
            for t in self.tasks:
                t.join()
        
        return self