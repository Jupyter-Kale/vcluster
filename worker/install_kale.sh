#!/bin/bash

sudo chown -R jovyan:users /usr/local/miniconda

if [ -f /opt/kale/setup.py ]; then
    cd /opt/kale
    /usr/local/miniconda/bin/pip install -e .
else
    cd /tmp
    git clone https://github.com/Jupyter-Kale/kale
    cd kale && git checkout 83398b1 && /usr/local/miniconda/bin/pip install .
fi

