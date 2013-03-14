from setuptools import setup, find_packages
from setuptools.extension import Extension
import sys
import os
import glob

version = '2.0'

c_ext = Extension("facs/_facs", define_macros = [('DEBUG', '1'), ('FIFO', '1'), ('FILE_OFFSET_BITS', '64'), ('LARGE_FILE', '1')],
                           sources = [f for f in glob.glob('facs/*.c') if 'mpi' not in f],
                           extra_compile_args = ['-fopenmp', '-mavx', '-mfma4'],
                           extra_link_args=['-lgomp', '-lz'])

setup(name='facs',
      version=version,
      description="FACS bloom filter implementation",
      long_description="""FACS you""",
      ext_modules=[c_ext],
      classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Healthcare Industry",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: C",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering :: Bio-Informatics"
      ],
      keywords='bloom filter probabilistic bioinformatics',
      author='Enze Liu, Lars Arvestad, Henrik Stranneheim, Roman Valls Guimera',
      author_email='roman@scilifelab.se',
      url='http://facs.scilifelab.se/',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            "nose-timer"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
