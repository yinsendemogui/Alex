#!usr/bin/env python
# -*- coding:utf-8 -*-
# auther:Mr.chen
# 描述：


import SocketServer
import os
class Myserver(SocketServer.BaseRequestHandler):



    def handle(self):
        conn = self.request
        print ("收到来自{0}的客户端连接:".format(self.client_address[0]))

        while True:
            try:
                print ("正在等待客户端指令：")
                self.data = self.request.recv(1024).strip()
                print ("收到客户端指令：{0}".format(self.data))
                data = os.popen(self.data).read()
                data_size = len(data)
                if data_size == 0 :
                    conn.sendall("Exit!")
                else:
                    conn.sendall(str(data_size))
                    self.data = conn.recv(1024)
                    if self.data == 'Ready!':
                        conn.sendall(data)
            except Exception,e:
                print "客户端出现异常",e
                break

if __name__ == "__main__":
    HOST,PORT = 'localhost',9999
    server = SocketServer.ThreadingTCPServer((HOST, PORT), Myserver)
    server.serve_forever()






# s = socket.socket()
# s.bind(('localhost',9999))
# s.listen(5)
#
# while True:
#     conn,addr = s.accept()
#     print ("new conn:",addr)
#     while True:
#         print ("等待新指令：")
#         data = conn.recv(1024)
#         if not data:
#             print ("客户端已经断开！")
#             break
#         print "执行指令！",data
#         cmd_res = os.popen(data).read()
#         print (cmd_res)
#         print ("before send",len(cmd_res))
#         if len(cmd_res) == 0 :
#             cmd_res = "cmd has no out put..."
#             conn.send("Exit!")
#         else:
#             conn.send(str(len(cmd_res)).encode("utf-8"))
#             if conn.recv(1024) == 'Ready!':
#                 conn.send(cmd_res)
#                 print ("send done")








