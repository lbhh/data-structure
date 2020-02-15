from pythonds.basic.queue import Queue
def hotPotato(namelist,num):
    simqueue = Queue()   #创建一个空队列对象，返回值未Queue对象
    for name in namelist:
        simqueue.enqueue(name)  #将数据项item添加到队尾，无返回值；将所有人加入到空队列中
    
    while simqueue.size() > 1: #将数据项item添加到队尾，无返回值
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())# 从队首移除数据项，返回值为队首数据项，队列被修改。每次传7个人，传到第7个后将7号dequeue掉
            
        simqueue.dequeue()
    return simqueue.dequeue()

print(hotPotato(['Bill','David','Susan','Jane','Kent','Brad'],7))
