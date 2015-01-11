#!/bin/sh
git clone https://github.com/stephanmg/ola.git
cd ola
autoreconf
./configure --enable-python-libs
make dist
