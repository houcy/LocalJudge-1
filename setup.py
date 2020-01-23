# -*-coding:utf-8-*-
from distutils.core import setup

from setuptools import find_packages

with open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()

version = ".".join(map(str, __import__("lj").__VERSION__))

setup(name="LocalJudge",
      version=version,
      description="",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="NoCLin",
      author_email="engineelin@gmail.com",
      url="https://github.com/NoCLin/LocalJudge",
      license="MIT Licence",
      install_requires=[
          'psutil==5.6.3',
          'colorful==0.5.4',
          'prettytable==0.7.2',
          'jsonpickle==1.2',
          'fire==0.2.1'
      ],
      packages=find_packages(),
      zip_safe=False,
      classifiers=[
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'
      ],
      package_data={
          'lj': ['*.json'],
      },
      entry_points={
          'console_scripts': [
              'lj = lj.lj:lj_main',
              'ljc = lj.lj:ljc_main',
              'ljr = lj.lj:ljr_main',
          ]},
      )
