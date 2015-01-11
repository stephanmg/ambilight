#!/bin/sh
git clone https://github.com/stephanmg/ola.git
cd ola
autoreconf --add-missing
./configure --enable-python-libs
make dist
