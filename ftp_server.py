'''
ftp 文件服务器程序
fork server训练
'''
from socket import *
import os
import sys
import time
import tools.mysqltool as mysqltool
from socket import *
from multiprocessing import Process
# 全局变量设置
HOST = '0.0.0.0'
PORT = 7777
ADDR = (HOST,PORT)

FILE_PATH = "/home/tarena/serverfiles/"

class FtpServer():
    def __init__(self,connfd):
        self.connfd = connfd
    def do_register(self,data,connfd):
        l = data.split(' ')
        username = l[1]
        password = l[2]
        # 进入数据库查找用户名 
        self.linkDB(connfd,username,password)

    def do_login(self,data,connfd):
        l = data.split(' ')
        username = l[1]
        password = l[2]
        # 进入数据库进行比对

    def do_download(self,filename):
        try:
            fd = open(FILE_PATH+filename,'rb')
        except:
            self.connfd.send("文件不存在".encode())
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        # 发送文件内容
        while True:
            data = fd.read(1024)
            if not data:
                time.sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)
        
    def do_upload(self,filename):
        filelist = os.listdir(FILE_PATH)
        if filename in filelist:
            self.connfd.send("文件已经存在".encode())
            return
        try:
            fd = open(FILE_PATH+filename,'wb')
        except:
            self.connfd.send("服务器异常".encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                print("文件接收完毕")
                break
            fd.write(data)
        fd.close()
    def linkDB(self,connfd,username,password):
        msql = mysqltool.Mysqltool('tt')
        msql.open()
        try:
            l = msql.all("select username from userinfo")
        except:
            print("数据库出错!")
            connfd.send(b'Error')
            return
        for i in l:
            if i[0] == username:
                # 用户已存在
                connfd.send(b'USED')
                return
        # 将数据存入数据库
        try:
            msql.insert_update_delete("insert into userinfo(username,password) values('%s','%s')"%(username,password))
        except:
            print("插入数据库失败")
            connfd.send(b'Error')
            return
        # 插入数据库成功
        connfd.send(b"OK")
        return

def handle(connfd):
    ftp = FtpServer(connfd)
    print("3")
    data = connfd.recv(1024).decode()
    print(data)
    if not data or data[0]=="Q":
        print("in")
        connfd.close()
        sys.exit(0)
    elif data[0] == "R":#代表发来的是注册信息
        ftp.do_register(data,connfd)
    elif data[0] == 'L':#代表发来的是登录消息
        ftp.do_login(data,connfd)
    elif data[0] == 'U':
        filename = data.split(" ")[-1]
        ftp.do_upload(filename)
    connfd.close()
    sys.exit("客户端断开")

# 创建网络连接
def main():
    # 创建套接字
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(7)

    print("监听端口",PORT)

    while True:
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("服务器异常：",e)
            continue
        print("连接客户端：",addr)

        # 创建子进程
        p = Process(target=handle,args=(connfd,))
        print("1")
        p.daemon = True
        p.start()
        print("2")
        # pid = os.fork()
        # if pid == 0:
        #     p = os.fork()
        #     if p == 0:
        #         sockfd.close()
        #         ftp = FtpServer(connfd)
        #         while True:
        #             data = connfd.recv(1024).decode()
        #             if not data or data[0]=="Q":
        #                 connfd.close()
        #                 sys.exit("客户端退出")
        #             elif data[0] == "R":#代表发来的是注册信息
        #                 ftp.do_register(data,connfd)
        #             elif data[0] == 'D':
        #                 filename = data.split(" ")[-1]
        #                 ftp.do_download(filename)
        #             elif data[0] == 'U':
        #                 filename = data.split(" ")[-1]
        #                 ftp.do_upload(filename)
        #     else:
        #         os._exit(0)
        # else:
        #     connfd.close()
        #     os.wait()



if __name__ == "__main__":
    main()


























