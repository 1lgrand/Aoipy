import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    # Here is the module name.
    name="AoiPy",
    version="0.8.20",
    author="Jade",
    description="Pycord made simple for learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),

    # if module has dependencies i.e. if your package rely on other package at pypi.org
    # then you must add there, in order to download every requirement of package
    install_requires=["Py-cord"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
