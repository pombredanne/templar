'''
run any command line and do not emit it's standard error or output unless there is an error
or there was an error.

Notice that we run the commands via a shell so that we will be able to do the following:
this_script.py 'ls -l 2> /dev/null'
In this case we will have on argument and we MUST run it to preserve the intention of the user.
if on the other hand we are run this way:
this_script.py ls -l
in which case we get many arguments, its ok to run them without a shell and save some resources.
'''

import sys # for exit
import subprocess # for Popen, PIPE

def run(args):
	if len(args)==1:
		pr=subprocess.Popen(args[0], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
	else:
		pr=subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(output,errout)=pr.communicate()
	output=output.decode()
	errout=errout.decode()
	print(output, end='')
	print(errout, end='')
	sys.exit(0)

'''
This version is intersting but alas wrong. If you pass a command that generates errors
and fails the errors will not be printed out. Example: this_script.py 'ls nonexistant'
This will succeed: this_script.py 'ls nonexistant; exit 0'
'''

'''
try:
	if len(args)==1:
		out=subprocess.check_output(args[0], stderr=subprocess.STDOUT, shell=True)
	else:
		out=subprocess.check_output(args, stderr=subprocess.STDOUT)
	print(out.decode(), end='')
except:
	pass
'''
