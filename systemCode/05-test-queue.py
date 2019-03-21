from multiprocessing import Queue

q = Queue(3)

q.put("消息1")
q.put("消息2")
print(q.full())

if not q.full():
    q.put_nowait("xiaoxi3")
print(q.qsize())
if not q.empty():
    for i in range(q.qsize()):
        print(q.get_nowait())
# try:
#     q.put("消息4", True, 2)
# except Exception as e:
#     print(e, q.qsize())
