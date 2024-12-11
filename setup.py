from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Base requirements
requirements = [
    "openai>=1.0.0",
    "ollama>=0.1.0",
    "pydantic>=2.0.0",
    "typing-extensions>=4.5.0",
    "aiohttp>=3.8.0",
    "asyncio>=3.4.3",
    "rich>=13.0.0"
]

# If requirements.txt exists, use it instead
if os.path.exists("requirements.txt"):
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="juryllm",
    version="0.1.0",
    author="Sujith",
    description="An experimental framework for LLM discussions with judge oversight",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sujith/juryLLM",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
)
