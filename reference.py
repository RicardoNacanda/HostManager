import paramiko,threading,json
class Manage(object):
    def main(self):
        list=[]
        with open('分组', 'r') as f:
            a = f.read()
            group_info = json.loads(a)
        while True:
            name=input("your name>>")
            password=input("password>>")
            if name!="czq" or password!="123":
                print("用户名或密码错误！")
                continue
            for item in group_info.keys():
                print(item)
            while True:
                choose1 = input("choose a group>>")
                if choose1 in group_info.keys():
                    for i in group_info[choose1]:
                        print(i,group_info[choose1][i]["ip"])
                    xx = '''
                               1.执行指令
                               2.上传文件
                               '''
                    cmd_dict = {'1': self.ssh_cmd,
                                '2': self.ssh_ftp}
                    print(xx)
                    while True:
                        cmd = input("input an operation>>")
                        if cmd=='q':
                            break
                        if cmd in cmd_dict:
                            command=input("command>>")
                            func = cmd_dict[cmd]
                            for i in group_info[choose1]:
                                t = threading.Thread(target=func, args=(
                                    group_info[choose1][i]["ip"],
                                    group_info[choose1][i]["username"],
                                    group_info[choose1][i]["password"],
                                    group_info[choose1][i]["port"],command,))
                                list.append(t)
                                t.start()
                            for i in list:
                                i.join()
                        else:
                            print("请输入正确的指令!")
                            continue

                else:
                    continue

    def ssh_cmd(self,*args):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname=args[0]
        username=args[1]
        password=args[2]
        port=args[3]
        command=args[4]
        # 允许连接不在虚拟机kown_hosts中文件的主机
        ssh.connect(hostname=hostname, port=port, username=username, password=
        password)
        # 连接服务器
        stdin, stdout, stderr = ssh.exec_command(command)
        # 执行命令
        # stdin,stdout,stderr分别是标准输入，标准输出和错误输出
        res,err= stdout.read(),stderr.read()
        result=res if res else err
        print('----------------%s-------------'%hostname)
        print(result.decode())
        ssh.close()
    def ssh_ftp(self,*args):
        hostname = args[0]
        username = args[1]
        password = args[2]
        port = args[3]
        trans = paramiko.Transport((hostname, port))
        trans.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(trans)
        print('''
        1.上传文件
        2.下载文件
        ''')
        filename=input("input filename>>")
        sftp.put(filename, '/tmp/%s'%filename)
        # 上传文件到服务器
        #sftp.get('regular_express.txt', 'from_centos.txt')
        # 下载文件,服务器中的路径和本地路径
        trans.close()

x=Manage()
x.main()