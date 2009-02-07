#!/usr/bin/env python


from distutils.core import setup


setup(name='textile',
      version='2.1.2',
      description='This is Textile. A Humane Web Text Generator.',
      author='Jason Samsa',
      author_email='jsamsa@gmail.com',
      url='http://loopcore.com/python-textile/',
      py_modules=['textile'],
      platforms = ['any'],
      license = ['BSD'],
      long_description = """Textile is a XHTML generator using a simple markup developed by Dean Allen."""
      )