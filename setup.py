from setuptools import setup, find_packages
import os

setup(
    name="gaze_estimation",
    version="0.1.0",
    author="yakhyo",
    description="Gaze estimation",
    long_description="Gaze estimation",
    long_description_content_type="text/markdown",
    include_package_data=True,
    python_requires=">=3.6",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
)
