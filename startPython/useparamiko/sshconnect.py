import paramiko
# private_key=paramiko.RSAKey.from_private_key('useparamiko/id_rsa')
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='github.com',port=22,username='zuohd',pkey=private_key)
stdin,stdout,stderr=ssh.exec_command('df -h')
result=stdout.read()
ssh.close()
print(str(result,encoding='utf-8'))