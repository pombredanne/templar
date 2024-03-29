'''
run any command line and do not emit it's standard
error or output unless there is an error, in which case
emit them and exit with the original commands exit code.

This wrapper is DIFFERENT than the wrapper_noerr.py wrapper
since this one actually emits error codes.
'''

import sys # for exit
import subprocess # for Popen, PIPE

def run(args):
	pr=subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	(output,errout)=pr.communicate()
	status=pr.returncode
	if status:
		print(output.decode(), end='')
		print(errout.decode(), end='')
		sys.exit(status)
