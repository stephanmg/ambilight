#!/bin/sh
git clone https://github.com/stephanmg/ola.git
cd ola
automake --add-missing
autoreconf
automake --add-missing
./configure --enable-python-libs
make dist
