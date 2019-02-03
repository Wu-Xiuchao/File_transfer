import tkinter as tk
import paramiko
from tkinter import filedialog
from tkinter.filedialog import askdirectory
import os,json

setting_file = json.load(open('default_set.json','r'))

window = tk.Tk()
window.title('文件传输助手')
window.geometry('{}x{}'.format(setting_file['width'],setting_file['height']))

def select_path():
	path = filedialog.askopenfilename()
	UPLOAD.set(path)

def select_path2():
	path = askdirectory()
	DOWNLOAD.set(path)
	
def upload():
	username = USER.get()
	password = PASS.get()
	host = IP.get()
	port = PORT.get()
	path = UPLOAD.get()
	remote_path = UP_REMOTE_FILE.get()
	print('本地地址:{}\n上传地址:{}\n'.format(path,remote_path))
	if path is '':
		return
	try:
		t = paramiko.Transport((host,int(port)))
		t.connect(username=username,password=password) 
		sftp = paramiko.SFTPClient.from_transport(t)
		sftp.put(path,'{}'.format(os.path.join(remote_path,os.path.split(path)[-1])))
		t.close() 
	except:
		REMIND.set('文件{}上传失败！'.format(os.path.split(path)[-1]))
	else:
		REMIND.set('文件{}上传成功！'.format(os.path.split(path)[-1]))

def download():
	username = USER.get()
	password = PASS.get()
	host = IP.get()
	port = PORT.get()
	path = DOWN_REMOTE_FILE.get()
	local_path = DOWNLOAD.get()
	print('本地地址:{}\n下载地址:{}\n'.format(local_path,path))
	if path is '':
		return
	try:
		t = paramiko.Transport((host,int(port)))
		t.connect(username=username,password=password) 
		sftp = paramiko.SFTPClient.from_transport(t)
		sftp.get(path,os.path.join(local_path,os.path.split(path)[-1]))
		t.close()
	except:
		REMIND.set('文件{}下载失败！'.format(os.path.split(path)[-1]))
	else:
		REMIND.set('文件{}下载成功！'.format(os.path.split(path)[-1]))

IP = tk.StringVar()
PORT = tk.StringVar()
USER = tk.StringVar()
PASS = tk.StringVar()
DISPLAY = tk.StringVar()
COMMOND = tk.StringVar()
DOWNLOAD = tk.StringVar()
UPLOAD = tk.StringVar()
UP_REMOTE_FILE = tk.StringVar()
DOWN_REMOTE_FILE = tk.StringVar()
UP_REMOTE_FILE.set(setting_file['remote_path'])
DOWN_REMOTE_FILE.set(setting_file['remote_path'])
DOWNLOAD.set(setting_file['local_path'])
REMIND = tk.StringVar()
IP.set(setting_file['ip'])
PORT.set(setting_file['port'])
USER.set(setting_file['user'])
PASS.set(setting_file['pass'])

frame0 = tk.Frame(window)
frame0.pack()
tk.Label(frame0,text='文件传输助手',font=('Arial', 20)).grid(row = 0, column = 0, padx = 10, pady = 20)

frame1 = tk.Frame(window)
frame1.pack()
tk.Label(frame1, text = "IP地址:",font=('Arial', 15)).grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Entry(frame1, textvariable = IP,font=('Arial', 15)).grid(row = 1, column = 1)
tk.Label(frame1, text = "端口:",font=('Arial', 15)).grid(row = 1, column = 2, padx = 10, pady = 10)
tk.Entry(frame1, textvariable = PORT,font=('Arial', 15)).grid(row = 1, column = 3)
tk.Label(frame1, text = "用户名:",font=('Arial', 15)).grid(row = 2, column = 0, padx = 10, pady = 0)
tk.Entry(frame1, textvariable = USER,font=('Arial', 15)).grid(row = 2, column = 1)
tk.Label(frame1, text = "密码:",font=('Arial', 15)).grid(row = 2, column = 2, padx = 10, pady = 0)
tk.Entry(frame1, textvariable = PASS,show = '*',font=('Arial', 15)).grid(row = 2, column = 3)


frame2 = tk.Frame(window)
frame2.pack()
tk.Label(frame2, text = "远程目录:",font=('Arial', 15)).grid(row = 0, column = 0, padx = 10, pady = 10)
tk.Entry(frame2, textvariable = UP_REMOTE_FILE,font=('Arial', 15)).grid(row = 0, column = 1)
tk.Label(frame2, text = "上传文件:",font=('Arial', 15)).grid(row = 0, column = 2, padx = 10, pady = 10)
tk.Entry(frame2, textvariable = UPLOAD,font=('Arial', 15)).grid(row = 0, column = 3)
tk.Button(frame2,text = "浏览",font=('Arial', 15), padx = 5, pady = 5, command=select_path).grid(row = 0, column = 4,padx=10, pady = 10)
tk.Button(frame2,text = "上传",font=('Arial', 15), padx = 5, pady = 5, command=upload).grid(row = 0, column = 5,padx=10, pady = 10)

tk.Label(frame2, text = "远程文件:",font=('Arial', 15)).grid(row = 1, column = 0, padx = 10, pady = 0)
tk.Entry(frame2, textvariable = DOWN_REMOTE_FILE,font=('Arial', 15)).grid(row = 1, column = 1)
tk.Label(frame2, text = "下载目录:",font=('Arial', 15)).grid(row = 1, column = 2, padx = 10, pady = 0)
tk.Entry(frame2, textvariable = DOWNLOAD,font=('Arial', 15)).grid(row = 1, column = 3)
tk.Button(frame2,text = "浏览",font=('Arial', 15), padx = 5, pady = 5, command=select_path2).grid(row = 1, column = 4,padx=10, pady = 0)
tk.Button(frame2,text = "下载",font=('Arial', 15), padx = 5, pady = 5, command=download).grid(row = 1, column = 5,padx=10, pady = 0)

frame3 = tk.Frame(window)
frame3.pack()
tk.Label(frame3, textvariable = REMIND, font=('Arial',13)).grid(row = 0, column = 0,padx=10, pady = 20)
window.mainloop()