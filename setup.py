# -*- coding: utf-8 -*-

import sys

from glob import iglob
from os import getcwd, path
from setuptools import setup, find_packages

if sys.version_info < (3,):
    raise Exception("""
    You are running Python {}.
    HardcodeTray is only compatible with Python 3.

    Make sure you have pip ≥ 19.0 to avoid this kind of issue,
    as well as setuptools ≥ 36.4.0:
      $ python3 -m pip install --upgrade pip setuptools

    Then you should be able to download the correct version of HardcodeTray:
      $ python3 -m pip install --upgrade HardcodeTray

    If this still gives you an error, please report the issue:
    <https://github.com/bilelmoussaoui/Hardcode-Tray/issues>

    Thanks!
    """.format(sys.version))

here = path.normpath(getcwd())

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='HardcodeTray',
    description='Themes hardcoded tray icons in Linux',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bilelmoussaoui/Hardcode-Tray',
    download_url='https://github.com/bilelmoussaoui/Hardcode-Tray/releases',
    author='Bilal Elmoussaoui',
    author_email='bil.elmoussaoui@gmail.com',
    maintainer='Peter J. Mello',
    maintainer_email='admin@petermello.net',
    license='GPL-3.0-or-later',
    platforms=['linux'],
    keywords='linux desktop tray icons panel theme',
    zip_safe=False,
    project_urls={
        'Funding': 'https://www.paypal.me/BilalELMoussaoui',
        'Issues': 'https://github.com/bilelmoussaoui/Hardcode-Tray/issues',
        'Source': 'https://github.com/bilelmoussaoui/Hardcode-Tray'
    },
    use_scm_version={
        'root': '..',
        'write_to': 'HardcodeTray/version.py',
        'write_to_template': '__version__ = "{version}"',
        'relative_to': __file__,
        'tag_regex': r'^(?P<prefix>v)?(?P<version>[^\+]+)(?P<suffix>.*)?$',
        'fallback_version': '4.4.0a1.dev0'
    },
    setup_requires=['setuptools_scm'],
    install_requires=['CairoSVG'],
    packages=find_packages(where='HardcodeTray'),
    package_dir={'': 'HardcodeTray'},
    scripts=['hardcode-tray'],
    data_files=[
        ('share/hardcode-tray/database',
         iglob('data/**/*.json', recursive=True)),
    ],
    classifiers=[
        "Development Status :: 6 - Mature",
        "Environment :: Console :: Curses",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later \
            (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Desktop Environment"
    ],
    python_requires='~=3.5'
)
