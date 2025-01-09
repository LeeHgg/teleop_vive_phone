from setuptools import setup, find_packages
 
with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setup(
    name="neuromeka-hri",
    version="0.1.1",
    author="Neuromeka",
    author_email="technical-support@neuromeka.com",
    description="Neuromeka protocols for HRI system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/neuromeka-robotics/neuromeka-hri",
    packages=find_packages(),
    install_requires=["neuromeka", "numpy", "scipy", "openvr"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    python_requires=">=3.7",
)
 
 