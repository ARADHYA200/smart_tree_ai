"""
Setup configuration for Smart Tree AI Pro
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="smart-tree-ai-pro",
    version="1.0.0",
    author="Smart Tree AI Team",
    description="Ultra-advanced tree intelligence platform with AI features",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "streamlit>=1.28.1",
        "pillow>=10.0.0",
        "qrcode>=7.4.2",
        "numpy>=1.24.3",
        "pandas>=2.0.3",
        "scikit-learn>=1.3.0",
        "plotly>=5.17.0",
        "requests>=2.31.0",
        "streamlit-option-menu>=0.3.6",
    ],
)
