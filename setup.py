import setuptools


def open_requirements(path):
    with open(path) as f:
        requires = [
            r.split("/")[-1] if r.startswith("git+") else r
            for r in f.read().splitlines()
            if not r.startswith("-")
        ]
    return requires


requires = open_requirements("requirements.txt")

with open("README.md") as file:
    readme = file.read()

with open("HISTORY.md") as file:
    history = file.read()


setuptools.setup(
    name="xsectron",
    version="0.0.0",
    description="A cross section calculation handbook for students",
    author="Dacheng Xu",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/markdown",
    setup_requires=["pytest-runner"],
    install_requires=requires,
    python_requires=">=3.9",
    packages=setuptools.find_packages(),
    package_data={
        "xsectron": [
            "data/*",
        ],
    },
    url="https://github.com/dachengx/cross_section",
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    zip_safe=False,
)
