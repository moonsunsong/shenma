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

FILE_PATH = "E:/data/"
# 连接数据库
msql = mysqltool.Mysqltool('tt')
msql.open()
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
        sql = "select username from userinfo where username=%s and password=%s"
        try:
            info = msql.all(sql,[username,password])
            print(info)
        except:
            print("服务器查询失败")
            # 发送失败标志
            connfd.send(b'ServerError')
            return
        if info != ():
            print("ok")
            # 发送登录成功标志
            connfd.send(b'SUCCESS')
        else:
            connfd.send(b'FAIL')
        
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
      
    def do_upload(self,filename,username):
        try:
            filelist = os.listdir(FILE_PATH+username)
        except FileNotFoundError:
            os.mkdir(FILE_PATH+username)
            filelist = os.listdir(FILE_PATH+username)
        if filename in filelist:
            self.connfd.send("文件已经存在".encode())
            return
        try:
            fd = open(FILE_PATH+username+"/"+filename,'wb')
        except:
            self.connfd.send("服务器异常".encode())
            return
        else:
            self.connfd.send(b'ok')
            time.sleep(0.2)
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                print("文件接收完毕")
                break
            fd.write(data)
        fd.close()
    def linkDB(self,connfd,username,password):
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
        sql = "insert into userinfo(username,password) values('%s','%s')"%(username,password)
        try:
            msql.insert_update_delete(sql)
        except:
            print("插入数据库失败")
            connfd.send(b'Error')
            msql.close()
            return
        # 插入数据库成功
        connfd.send(b"OK")
        return


    # def do_chat(self,username,data,connfd):
        
    def do_list(self,username):
        # 获取文件列表
        try:
            file_list = os.listdir(FILE_PATH+username)
            if not file_list:
                self.connfd.send("文件库为空")
                return
            else:
                self.connfd.send(b'ok')
                time.sleep(0.1)
            
            files = ''
            for file in file_list:
                files = files+file+'#'
            # 将拼接号的文件名字节串发送给客户端
            self.connfd.sendall(files.encode())
        except FileNotFoundError:
            os.mkdir(FILE_PATH+username)
def handle(connfd):
    ftp = FtpServer(connfd)
    while True:
        try:
            data = connfd.recv(1024).decode()
        except:
            connfd.close()
            sys.exit("客户端断开")
        if not data or data[0]=="Q":
            connfd.close()
            sys.exit(0)
        elif data[0] == "R":#代表发来的是注册信息
            ftp.do_register(data,connfd)
        elif data[0] == 'L':#代表发来的是登录消息
            ftp.do_login(data,connfd)
        elif data[0] == 'U':#代表发来的是上传请求
            filename = data.split(" ")[-2]
            username = data.split(" ")[-1]
            ftp.do_upload(filename,username)


        # # 发来聊天信息请求
        # elif data[0] == "C":
        #     ftp.do_chat(username,data,connfd)
           
        elif data[0] == "F":
            username = data.split(" ")[-1]
            ftp.do_list(username)
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
        p.daemon = True
        p.start()
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






