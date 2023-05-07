from setuptools import setup, find_packages


setup(
    name='retrolink',
    version='0.1.0',
    description="A simple web app / CLI to update content with outdated links",
    long_description="A simple web app / CLI to update content with outdated links",
    author="Kaustubh Maske Patil",
    url="https://github.com/nikochiko/retrolink",
    packages=find_packages(),
    install_requires=[
        "requests",
        "flask",
        "python-dateutil",
        "kutty @ git+https://github.com/pipalacademy/kutty.git#egg=kutty",
    ],
    entry_points={
        "console_scripts": [
            "rl=retrolink:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
