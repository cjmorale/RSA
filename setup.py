import setuptools
import sys

setuptools.setup(
    name='RSA',
    version='0.0.2',
    description='RSA crypto system',
    author='Carlo Morales',
    author_email='cjmorale2004@gmail.com',
    url='https://github.com/cjmorale/RSA',
    license='Public',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy'
    ]
)
