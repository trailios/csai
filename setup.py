from setuptools import setup, find_packages

setup(
    name="cs-ai",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Python client for solving captchas via CaptchaSolver.ai",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/cs-ai",
    license="MIT",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25",
        "typing-extensions>=4.0"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    python_requires=">=3.7",
    include_package_data=True,
)
