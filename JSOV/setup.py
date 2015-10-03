from setuptools import setup

setup(
	name = 'JSOV',
	packages = ['JSOV'],
	version = '0.1.2',
	description = 'JSON visualization lib based on JSOV or custom templates',
	author = 'Anas El Husseini',
	author_email = 'linux.anas@gmail.com',
	license = 'BSD',
	url = 'https://github.com/linostar/pypi-JSOV',
	download_url = 'https://github.com/linostar/pypi-JSOV/tarball/0.1.1',
	keywords = ['JSON', 'JSOV', 'templates', 'visualization'],
	install_requires = ['PyYAML>=3.11', 'cssutils>=1.0', 'dpath>=1.4.0'],
	classifiers = [
	'Development Status :: 3 - Alpha',
	'Intended Audience :: Developers',
	'Topic :: Utilities',
	'License :: OSI Approved :: BSD License',
	'Programming Language :: Python :: 3',
	],
)
