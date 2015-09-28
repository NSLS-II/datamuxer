try:
    from setuptools import setup
except ImportError:
    try:
        from setuptools.core import setup
    except ImportError:
        from distutils.core import setup


setup(
    name='datamuxer',
    version='v0.3.0',
    author='Brookhaven National Laboratory',
    py_modules=['datamuxer']
)
