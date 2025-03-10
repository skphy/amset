from setuptools import find_packages, setup

from amset import __version__

with open("README.md", "r") as file:
    long_description = file.read()

if __name__ == "__main__":
    setup(
        name="amset",
        version=__version__,
        description="AMSET is a tool to calculate carrier transport properties "
        "from ab initio calculation data",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/hackingmaterials/amset",
        author="Alex Ganose",
        author_email="aganose@lbl.gov",
        license="modified BSD",
        keywords="mobility conductivity seebeck scattering lifetime rates dft vasp",
        packages=find_packages(),
        package_data={
            "amset": [
                "defaults.yaml",
                "plot/amset_base.mplstyle",
                "plot/revtex.mplstyle",
            ]
        },
        data_files=["LICENSE"],
        zip_safe=False,
        install_requires=[
            "quadpy>=0.16.10",
            "numpy",
            "pymatgen>=2022.0.16",
            "scipy",
            "monty",
            "matplotlib",
            "BoltzTraP2",
            "tqdm",
            "tabulate",
            "memory_profiler",
            "spglib",
            "click",
            "sumo",
            "h5py",
            "pyFFTW",
            "interpolation",
            "numba",
        ],
        extras_require={
            "docs": [
                "mkdocs==1.2.3",
                "mkdocs-material==8.0.1",
                "mkdocs-minify-plugin==0.5.0",
                "mkdocs-macros-plugin==0.6.3",
                "markdown-include==0.6.0",
                "markdown-katex==202109.1033",
            ],
            "tests": ["pytest==6.2.5", "pytest-cov==3.0.0"],
            "all-electron": ["pawpyseed==0.7.1"],
            "dev": [
                "coverage==6.2",
                "codacy-coverage==1.3.11",
                "pycodestyle==2.8.0",
                "mypy==0.910",
                "pydocstyle==6.1.1",
                "flake8==4.0.1",
                "pylint==2.12.1",
                "black==21.11b1",
                "pre-commit==2.15.0",
            ],
        },
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Information Technology",
            "Operating System :: OS Independent",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Scientific/Engineering",
        ],
        tests_require=["pytest"],
        entry_points={
            "console_scripts": [
                "amset = amset.tools.cli:cli",
                "desym = amset.tools.desym:desym",
            ]
        },
    )
