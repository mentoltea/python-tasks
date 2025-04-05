from basic_task import *
from thread_task import *
from multytask import *
from joined_task import *
from chained_task import *

def fetch_unnest(task: BasicTask | MultyTask):
    t = task.fetch()
    while isinstance(t, BasicTask) or isinstance(t, MultyTask):
        t = t.fetch()
    return t