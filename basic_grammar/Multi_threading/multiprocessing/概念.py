'''
run()
表示进程活动的方法。
你可以在子类中重载此方法。标准 run() 方法调用传递给对象构造函数的可调用对象作为目标参数（如果有），分别从 args 和 kwargs 参数中获取顺
序和关键字参数。

start()
启动进程活动。
每个进程对象最多只能调用一次。它安排对象的 run() 方法在一个单独的进程中调用。

join([timeout])
如果可选参数 timeout 是 None （默认值），则该方法将阻塞，直到调用 join() 方法的进程终止。如果 timeout 是一个正数，它最多会阻塞
timeout 秒。请注意，如果进程终止或方法超时，则该方法返回 None 。检查进程的 exitcode 以确定它是否终止。

一个进程可以合并多次。
进程无法并入自身，因为这会导致死锁。尝试在启动进程之前合并进程是错误的。

name
进程的名称。该名称是一个字符串，仅用于识别目的。它没有语义。可以为多个进程指定相同的名称。
初始名称由构造器设定。 如果没有为构造器提供显式名称，则会构造一个形式为 ‘Process-N1:N2:…:Nk’ 的名称，其中每个 Nk 是其父亲的第 N 个孩子。

is_alive()
返回进程是否还活着。
粗略地说，从 start() 方法返回到子进程终止之前，进程对象仍处于活动状态。

daemon
进程的守护标志，一个布尔值。这必须在 start() 被调用之前设置。
初始值继承自创建进程。

当进程退出时，它会尝试终止其所有守护进程子进程。
请注意，不允许守护进程创建子进程。否则，守护进程会在子进程退出时终止其子进程。 另外，这些 不是 Unix守护进程或服务，它们是正常进程，如果
非守护进程已经退出，它们将被终止（并且不被合并）。

除了 threading.Thread API ，Process 对象还支持以下属性和方法：

pid
返回进程ID。在生成该进程之前，这将是 None 。

exitcode
的退子进程出代码。如果进程尚未终止，这将是 None 。负值 -N 表示孩子被信号 N 终止。

authkey
进程的身份验证密钥（字节字符串）。

当 multiprocessing 初始化时，主进程使用 os.urandom() 分配一个随机字符串。
当创建 Process 对象时，它将继承其父进程的身份验证密钥，尽管可以通过将 authkey 设置为另一个字节字符串来更改。

参见 认证密码 。

sentinel
系统对象的数字句柄，当进程结束时将变为 “ready” 。
如果要使用 multiprocessing.connection.wait() 一次等待多个事件，可以使用此值。否则调用 join() 更简单。
在Windows上，这是一个操作系统句柄，可以与 WaitForSingleObject 和 WaitForMultipleObjects 系列API调用一起使用。在Unix上，这是一个文件描述符，可以使用来自 select 模块的原语。

3.3 新版功能.

terminate()
终止进程。 在Unix上，这是使用 SIGTERM 信号完成的；在Windows上使用 TerminateProcess() 。 请注意，不会执行退出处理程序和finally子句等。

请注意，进程的后代进程将不会被终止 —— 它们将简单地变成孤立的。
警告 如果在关联进程使用管道或队列时使用此方法，则管道或队列可能会损坏，并可能无法被其他进程使用。类似地，如果进程已获得锁或信号量等，则终止它可能导致其他进程死锁。
注意 start() 、 join() 、 is_alive() 、 terminate() 和 exitcode 方法只能由创建进程对象的进程调用。

'''


import multiprocessing
import time
import signal
p = multiprocessing.Process(target=time.sleep, args=(1000,))
print(p, p.is_alive())
# <Process(Process-1, initial)> False
p.start()
print(p, p.is_alive())
# <Process(Process-1, started)> True
p.terminate()
time.sleep(0.1)
print(p, p.is_alive())
# <Process(Process-1, stopped[SIGTERM])> False
print(p.exitcode == -signal.SIGTERM)
