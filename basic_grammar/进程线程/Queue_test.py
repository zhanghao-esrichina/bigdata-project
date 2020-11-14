from multiprocessing import Queue

q = Queue(5)

q.put('a')
q.put('b')
q.put('c')
q.put('d')
q.put('e')

if not q.full():
    q.put('f', timeout=3)
else:
    print('队列已满')
# q.put('f') #put()如果队列满了则只能等待（阻塞），等待队列的内容有空缺

print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())

if not q.empty():
    print(q.get())
else:
    print('队列为空')
