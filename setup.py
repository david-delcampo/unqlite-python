import glob
from distutils.core import setup, Extension

try:
    from Cython.Build import cythonize
except ImportError:
    raise RuntimeError('Cython must be installed to build unqlite-python.')


python_source = 'unqlite.pyx'
library_source = glob.glob('src/*.c')

unqlite_extension = Extension(
    'unqlite',
    sources=[python_source] + library_source)

setup(
    name='unqlite',
    version='0.6.0',
    description='Fast Python bindings for the UnQLite embedded NoSQL database.',
    author='Charles Leifer',
    author_email='',
    url='https://github.com/coleifer/unqlite-python',
    license='MIT',
    install_requires=['Cython'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: C',
        'Programming Language :: Cython',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Embedded Systems',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    ext_modules=cythonize([unqlite_extension])
)
