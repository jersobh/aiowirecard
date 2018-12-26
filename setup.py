import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aiowirecard",
    version="0.0.5",
    author="jersobh",
    author_email="jersobh@gmail.com",
    description="Wirecard API asyncio wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jersobh/aiowirecard",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)