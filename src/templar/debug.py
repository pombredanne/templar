'''
centralized debugging module
'''

import sys # for stderr

# do you want to see the commands?
opt_show_commands=True

def process(l, tag):
	if opt_show_commands:
		print('executing [{0}] [{1}]...'.format(l, tag), file=sys.stderr)

def debug(s):
	if opt_show_commands:
		print(s, file=sys.stderr)
