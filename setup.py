from setuptools import setup, Extension

setup(name='hellopkg',
      version='0.1.0',
      packages=['hellopkg'],
      install_requires=['requests'],
      entry_points={
          'console_scripts': ['hellopkg-cli=hellopkg.hello:hello'],
      },
      ext_modules=[Extension('demo', sources=['hello.c'])])
