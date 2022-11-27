from setuptools import setup

setup(
   name='ColorfulSnowflakes',
   version='0.1.0',
   author='An Awesome snowy experience',
   author_email='adarsh.raghunath@gmail.com',
   packages=['colorfulsnow'],
   license='LICENSE',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   install_requires=[
       "numpy >= 1.19.12",
   ],
)