import subprocess
obj=subprocess.Popen(['python'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,\
                     stderr=subprocess.PIPE,universal_newlines=True)
obj.stdin.write('print(1)\n')
obj.stdin.write('print(2)')

obj.stdin.close()

cmd_out=obj.stdout.read()
obj.stdout.close()
cmd_error=obj.stderr.read()
obj.stderr.close()
print(cmd_out)
print(cmd_error)

obj1=subprocess.Popen(['python'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,\
                     stderr=subprocess.PIPE,universal_newlines=True)
out_error_list=obj1.communicate('print("Hello")')
print(out_error_list)

