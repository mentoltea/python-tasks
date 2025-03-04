from basic_task import *
from threading import Thread


class ThreadTask(BasicTask):
    def __init__(self, task: Callable, *args, **kwargs):
        super().__init__(task, *args, **kwargs)
    
    def __call__(self, *args, **kwds):
        if (not self.calling):
            self.thread = Thread(target=super().__call__,
                            daemon=True,
                            )
            
            self.thread.start()
        return self
        
    def join(self):
        if (self.called):
            if self.thread.is_alive():
                self.thread.join()
        
        return self