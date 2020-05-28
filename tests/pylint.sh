#!/bin/sh

PREFIX="$(python3 -c 'from distutils.sysconfig import PREFIX; print(PREFIX)')"
SITE_PACKAGES="$(python3 -c 'from distutils.sysconfig import get_python_lib; print(get_python_lib())' | xargs dirname)"

find "${SITE_PACKAGES}" -depth -iname 'HardcodeTray' -type d -exec pylint --rcfile=.pylintrc '{}' \; ||
find "${PREFIX}" -depth -ipath '*/HardcodeTray/*.py' -type f -exec pylint --rcfile=.pylintrc '{}' \+
