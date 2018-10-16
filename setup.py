import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="async_moip",
    version="0.0.4",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="Moip API wrapper for asyncio/aiohttp",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/async-moip",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)