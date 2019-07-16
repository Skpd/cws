import setuptools

with open("README.md") as fh:
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
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=['websocket-client'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
