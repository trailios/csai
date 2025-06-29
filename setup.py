from setuptools import setup, find_packages

setup(
    name="cs-ai",  # 📦 This is the name on PyPI
    version="0.1.0",
    author="trailios",
    author_email="you@example.com",
    description="Python API wrapper for the Captcha Solver AI service",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/trailios/csai",
    license="Apache License 2.0",
    packages=find_packages(include=["cs_ai", "cs_ai.*"]),
    install_requires=[
        "requests>=2.25",
        "typing-extensions>=4.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
)
