'''
ftp 文件服务器程序
fork server训练
'''
from socket import *
import os,sys
import time

# 全局变量设置
HOST = '0.0.0.0'
PORT = 7777
ADDR = (HOST,PORT)

FILE_PATH = "/home/tarena/serverfiles/"

class FtpServer():
    def __init__(self,connfd):
        self.connfd = connfd
    def do_list(self):
        print("执行list")
        # 获取文件列表
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空")
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.1)
        
        files = ''
        for file in file_list:
            if file[0]!='.' and os.path.isfile(FILE_PATH+file):
                files = files+file+'#'
        # 将拼接号的文件名字节串发送给客户端
        self.connfd.sendall(files.encode())
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
        pid = os.fork()
        if pid == 0:
            p = os.fork()
            if p == 0:
                sockfd.close()
                ftp = FtpServer(connfd)
                while True:
                    data = connfd.recv(1024).decode()
                    if not data or data[0]=="Q":
                        connfd.close()
                        sys.exit("客户端退出")
                    elif data[0] == "L":
                        ftp.do_list()
                    elif data[0] == 'D':
                        filename = data.split(" ")[-1]
                        ftp.do_download(filename)
                    elif data[0] == 'U':
                        filename = data.split(" ")[-1]
                        ftp.do_upload(filename)
            else:
                os._exit(0)
        else:
            connfd.close()
            os.wait()



if __name__ == "__main__":
    main()


























