from setuptools import setup

setup(name='tinkerforge_util',
      version='1.5.1',
      description='Python utilities for internal Tinkerforge usage',
      license='LGPLv2+',
      author='Tinkerforge GmbH',
      author_email='matthias@tinkerforge.com',
      url='https://www.tinkerforge.com',
      packages=['tinkerforge_util'],
      platforms=['Any'],
      install_requires=['pyserial'])
