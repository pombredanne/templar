#!/usr/bin/python3

'''
This is the installation tool. use minimal packages here.
dont use setuptools, dont use subprocess.

We really this file to be generated.
'''

import distutils.core # for setup

distutils.core.setup(
	name='templar',
	version='${tdefs.git_lasttag}',
	description='Templating engine for python',
	long_description='Templating engine for python (long description)',
	author='Mark Veltzer',
	author_email='mark.veltzer@gmail.com',
	maintainer='Mark Veltzer',
	maintainer_email='mark.veltzer@gmail.com',
	keywords=[
		'mako',
		'templating',
		'python',
	],
	url='https://veltzer.net/templar',
	license='LGPL',
	platforms=[
		'ALL',
	],
	packages=['templar'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: LGPL',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 3',
		'Topic :: Software Development :: Building',
		'Topic :: Software Development :: Libraries',
		'Topic :: Utilities',
	],
	data_files=[
		('/usr/share/templar', ['make/Makefile']),
		('/usr/share/templar/templates', ['templates/README.md.mako']),
		('/usr/share/templar/templates', ['templates/changelog.mako']),
		('/usr/bin', ['templar_cmd']),
		('/usr/bin', ['make_helper']),
		('/usr/bin', ['release_helper']),
		('/usr/bin', ['wrapper_css_validator']),
		('/usr/bin', ['wrapper_noerr']),
		('/usr/bin', ['wrapper_ok']),
		('/usr/bin', ['wrapper_silent']),
	],
)