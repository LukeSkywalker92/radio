from setuptools import setup, find_packages

setup(
    name= 'radio',
    version= '0.0.1',
    description= 'Listen to radio.',
    url='https://github.com/LukeSkywalker92/radio',
    author='Lukas Scheffler',
    author_email='luke@lukecodewalker.de',
    license='MIT',
    packages=find_packages(),
    install_requires=['python-vlc==3.0.11115'],
    entry_points={
        'console_scripts': ['radio=radio.radio:main']
    }
)