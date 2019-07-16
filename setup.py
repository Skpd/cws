import setuptools
import os

with open(os.path.dirname(os.path.realpath(__file__)) + "/README") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cws",
    version="0.0.3",
    author="Dmitrii Shabanov",
    author_email="dm.skpd@gmail.com",
    description="Simple python client for cryptowat.ch websocket streams.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skpd/cws",
    packages=['cws', 'cws.client', 'cws.markets', 'cws.stream'],
    python_requires='>=3.6',
    install_requires=['websocket-client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
