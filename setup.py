from setuptools import setup

setup(
    name='BlaApi',
    version='1.0',
    description='A wrapper for the BlaApi',
    author='Omer-Farooqui',
    author_email='deaddogfuneral@gmail.com',
    packages=['BlaApi'],
    license= "MIT",
    requires=['httpx', 'fake_useragent']
)