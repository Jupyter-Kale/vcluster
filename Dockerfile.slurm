FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    supervisor \
    python-pip \
    munge \
    slurm-wlm

RUN /usr/sbin/create-munge-key

RUN pip install docker-py
COPY slurm/init.sh /usr/local/bin/init.sh
COPY slurm/detect_nodes.py /usr/local/bin/detect_nodes.py
COPY slurm/detect_nodes.conf /etc/supervisor/conf.d/detect_nodes.conf
COPY slurm/slurm.conf /etc/slurm-llnl/slurm.conf

RUN mkdir /var/spool/slurm
RUN chmod a+w /var/spool/slurm/.

CMD ["sh", "-c", "/usr/bin/supervisord -n"]
