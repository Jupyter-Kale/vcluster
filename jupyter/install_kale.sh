#!/bin/bash

if [ -f /opt/kale/setup.py ]; then
    cd /opt/kale && pip install -e .
    cp -R /opt/kale/examples /home/jovyan/work/examples
else
    git clone https://github.com/Jupyter-Kale/kale
    cd kale && git checkout 83398b1 && pip install .
    cp -R /home/jovyan/kale/examples /home/jovyan/work/examples
fi
