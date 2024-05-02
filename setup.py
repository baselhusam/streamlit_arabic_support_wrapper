import setuptools

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit_arabic_support_wrapper",
    version="1.0",
    author="Basel Husam",
    author_email="baselmathar@gmail.com",
    description="A simple component to perfectly align Arabic text in Streamlit Apps.",
    license="Apache 2",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/baselhusam/streamlit_arabic_support_wrapper",
    packages=setuptools.find_packages(exclude=["tests", "tests.*"]),
    install_requires=["streamlit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
)