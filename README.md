# HostManager
tiny C/C++ program to manage hosts
这是一个简单到不能再简单的主机管理程序
几天前老师给的任务，中间耽搁了一天，寻思着先上传个版本看看吧。

一 功能
	管理多台主机,基于C/C++,通过ssh,支持cmd&sftp
1.简单的主机分组，指定部分主机或主机小组来执行当前的cmd
	出于交互体验的考虑，这部分写得很凌乱，颇有C语言课设的感觉。
	调了很久（manager4:修改自https://blog.csdn.net/KiteRunner/article/details/44888703）
	还是有点儿瑕疵，考虑到大头(ftp)还没写完，暂时这样吧。

	>Commad@allHosts:
		一般来说，cmd总是作用于所有主机，所以设此为默认情况
	_q:
		退出，同时做一下数据更新保存
	_cg:
		change group setting
		将指定编号(seq)的主机所属的groupId修改掉
	_cat:
		展示一下hosts.txt,groupSetting.txt，省得去翻这两个txt
	_sg:
		>Commad@SpecifiedGroups:
		specify hosts by group
		指定一些小组的主机执行命令
	_s:
		>Commad@SpecifiedHosts:
		指定一些主机执行命令

	PS:
		对于指定主机seq或者主机分组group,
		支持单值 1  和范围 1-3
2.由libssh2完成文件传输
	修改自https://www.libssh2.org/examples/
	下载写(调)好了，明天就可以整合到manager中去，目前在sftptest.c中。
	上传总是Error，还没改出来。
	对官方的轮子改动不大，仅修改了环境相关的部分，还是比较坑的。

3.非阻塞与多线程要求
	
	网上的轮子已经实现非阻塞(至少它自己是这么说的),但笔者还未完全弄清楚这是个什么东西

	目前把多线程放在最后一步，虽然没有多线程可能很影响效率和使用体验
	但笔者没有多线程使用经验，还是先实现主要功能吧

	在前期学习并实践多线程的时候，我发现多线程可能出现如下问题：
		1.影响交互时的回显
			从 本地完成cmd输入,传输数据,主机接收执行，返回并显示回显数据有一定时延
			考虑多线程的运行流程，可能出现回显数据相互交错的情况
			即

				[来自主机A的回显数据]
				[来自主机B
				[来自主机C的回显数据]
				的回显数据]

			也可能是我水平不够,还没掌握避免这种情况的方法(或者不会有这种情况)
		
		2.libssh2的轮子不能多线程?
			每当我尝试用数组建立一个保存ssh链接的指针数组，就会莫名Error
			难道是端口或者某个变量的复用引发的?
二 使用
	1.环境 
		linux
		考虑笔者孱弱的操作系统常识带来的不便，请使用Ubuntu虚拟机避免环境变量的折磨以获取良好体验
	2.用于支持的库
		请先update&upgrade一下

		openSSL  Libgcrypt11 libssh2

		apt-get install openSSL
		apt-get install Libgcrypt11-dev(注意)
		libssh2
			wget http://www.libssh2.org/download/libssh2-1.4.3.tar.gz
			tar -zxvf libssh2-1.4.3.tar.gz
			./configure
			make
			make install
	3.编译
		若对代码做出修改后重新编译，请置环境变量 LD_LIBRARY_PATH=.
		设置  export LD_LIBRARY_PAYH=.
		查看  echo $LD_LIBRARY_PAYH
		此处是为了告知编译器还需要看看当前目录有没有需要引用的 .h .a .so 文件
		事实上通过在编译命令中设置rpath=.的方法达到同样效果，但遗憾我多次尝试未果。
	4.参数
		manager4的参数在前文给出
		sftptest.c最终是会被整合的，具体可看代码
		./sftptest ip username password filepath -p

		当从多台主机上下载文件时，回出现重名问题，这里将文件命名为ip+filename
		其实应该将文件传到主机对应的文件夹里

三 心路历程
	
	以前我觉得我只会C/C++,现在我觉得我连这个都不会了。
	
	以前都是一条cpp源代码走天下，连库都没怎么用(比赛不许)
	如今被环境变量，库函数折磨到不行

	一开始在win下面写,发现差了好多库函数，上网查了半天的解决方法
	后来猛然反应过来这是在Linux上用的
	转移后一瞬解决库函数问题

	漏看了一个.so文件，弄了一天多，想找到缺失的函数源码来编译供主函数调用
	结果加载一下这个so就解决了......

	没有关闭文件指针，导致键盘输入cmd被拒绝，改了一上午......

	后面还会有这类的问题吧，先睡了


