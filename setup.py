from distutils.core import setup
from setuptools import find_packages


setup(name='OpenMDOC',
    version='0.1',
    description='Open-source Multidisciplinary Dynamics and Optimal Control',
    url='https://github.com/OpenMDAO/OpenMDOC',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache 2.0',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    license='Apache License',
    packages=find_packages(),
    install_requires=[
        'openmdao',
        'numpy',
        'scipy',
        'pep8',
        'parameterized'
    ],
    zip_safe=False,
)
