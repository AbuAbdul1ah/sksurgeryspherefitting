# coding=utf-8
"""
Setup for scikit-surgery-sphere-fitting
"""

from setuptools import setup, find_packages
import versioneer

# Get the long description
with open('README.rst') as f:
    long_description = f.read()

setup(
    name='scikit-surgery-sphere-fitting',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='scikit-surgery-sphere-fitting implements',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/AbuAbdul1ah/sksurgeryspherefitting',
    author='Sujon Hekim',
    author_email='YOUR-EMAIL@ucl.ac.uk',
    license='BSD-3 license',
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',


        'License :: OSI Approved :: BSD License',


        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',

        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],

    keywords='medical imaging',

    packages=find_packages(
        exclude=[
            'doc',
            'tests',
        ]
    ),

    install_requires=[
        'numpy',
    ],

    entry_points={
        'console_scripts': [
            '                                a least squares sphere fitting algorithm,=                                a least squares sphere fitting algorithm,.__main__:main',
        ],
    },
)
