from distutils.core import setup

setup(
    name='gsutils',
    version='0.1',
    packages=['gsutils'],
    url='https://github.com/oktopac/gsutils',
    license='Apache',
    author='oktopac',
    author_email='',
    install_requires=[
        "google-cloud-storage"
    ]
    description='Some utilities for google cloud'
)
