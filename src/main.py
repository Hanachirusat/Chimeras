import time
import unittest
from observer import InteractionQueue, Task
from chimeras import *

if __name__=="__main__":
    queue=InteractionQueue()
    jxf=Jxf("急先锋")
    queue.add_member(jxf)
    gzk=Gzk("工作狂")
    queue.add_member(gzk)
    bdm=Bdm("帮倒忙")
    queue.add_member(bdm)
    xkk=Xkk("小夸夸")
    queue.add_member(xkk)
    bgx=Bgx("背锅侠")
    queue.add_member(bgx)
    zcql=Zcql("职场清流")
    queue.add_leader(zcql)
    work=Task(atk=5,hp=80)

    queue.begin_work(work)