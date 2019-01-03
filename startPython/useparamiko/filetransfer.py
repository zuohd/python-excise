import paramiko

t = paramiko.Transport(('localhost', 22))
t.connect(username='root', password='root123')
sftp = paramiko.SFTPClient.from_transport(t)
remotepath = '/tmp/uploadtxt'

localpath = 'test.txt'

sftp.put(localpath, remotepath)
# sftp.get(remotepath,localpath)
t.close()
