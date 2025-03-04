from multytask import *


class ChainedTask(MultyTask):
    def __init__(self, 
                ts: list[ BasicTask | ThreadTask | MultyTask ],
                contype: Literal["positional", "keyword"] = "positional", 
                keyword: str = "chained",
                ):
        super().__init__()
        self.tasks = ts
        self.contype = contype
        self.keyword = keyword
        
        
    def __call__(self, *args, **kwds):
        if (not self.calling):
            self.called = True
            
            self.calling = True
            self.finished = False
            
            self.result_ = None
            for i, t in enumerate(self.tasks):
                if (i > 0): 
                    if (self.contype == "positional"): t.args = tuple(list(t.args) + [self.result_])
                    if (self.contype == "keyword"): t.kwargs[self.keyword] = self.result_
                
                self.result_ = t().join().fetch()
            
            self.calling = False
            self.finished = True
        
        return self
    
    def join(self, *args, **kwargs):
        if (self.called):
            for t in self.tasks:
                t.join()
        
        return self