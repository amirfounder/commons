from setuptools import setup, find_packages

setup(
    name='commons',
    version='0.0.45',
    packages=find_packages(),
    install_requires=[
        'mss~=6.1.0',
        'multipledispatch~=0.6.0',
        'setuptools~=60.2.0',
        'numpy~=1.22.4',
        'opencv-python~=4.5.5.64',
        'pydantic~=1.9.1',
        'orjson~=3.7.2'
    ]
)
