"""
Materials Studio 自动化接口安装脚本
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="automs",
    version="0.1.0",
    author="AutoMS Team",
    description="Materials Studio 自动化接口 - Python 封装",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/AutoMS",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="materials studio automation com interface python",
    project_urls={
        "Documentation": "https://github.com/yourusername/AutoMS/docs",
        "Source": "https://github.com/yourusername/AutoMS",
        "Tracker": "https://github.com/yourusername/AutoMS/issues",
    },
)

