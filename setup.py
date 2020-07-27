import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gymgif",
    version="0.0.1",
    author="Tianhao Zhou",
    author_email="jacksonzhou666@gmail.com",
    description="Utility package to save gym game play as GIF images for the engineers who are too broke to afford a local training machine :(",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tianhaoz95/gymgif",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)