from setuptools import setup, find_packages

with open('README.md') as f:
    description = f.read()

setup(
    name='dataclasses-binary',
    version='0.1',
    license='MIT',
    description=description,
    author='Tom Gringauz',
    author_email='tomgrin10@gmail.com',
    url='https://github.com/tomgrin10/binary-core',
    packages=find_packages(),
    install_requires=[
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
