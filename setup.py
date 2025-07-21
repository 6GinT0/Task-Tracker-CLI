from setuptools import setup, find_packages

setup(
    name="task-cli",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "task-cli=task_cli.main:main",
        ],
    },
    author="Ulises Saucedo",
    description="CLI for managing tasks",
    install_requires=[
        "termcolor",
        "tinydb",
    ],
    extras_require={
        "dev": [
            "pytest",
        ]
    },
    python_requires=">=3.7",
)