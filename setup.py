
from setuptools import setup

with open('requirements.txt') as f:
    install_packs = f.read().splitlines()


setup(
    name='pyucs',
    version='1.0.0',
    description='Customized UCS Python Module',
    license='Apache',
    packages=['pyucs'],
    install_requires=install_packs,
    author='Sammy Shuck github.com/ToxicSamN',
    keywords=['pyucs'],
    url='https://github.com/ToxicSamN/pyucs'
)
