#!/usr/bin/env bash
echo "\$pbsserver torque" > /var/spool/torque/mom_priv/config
echo "\$usecp *:/tmp/scratch /tmp/scratch" >> /var/spool/torque/mom_priv/config
echo "\$attempt_to_make_dir true" >> /var/spool/torque/mom_priv/config
echo "\$loglevel 7" >> /var/spool/torque/mom_priv/config

echo "torque" > /var/spool/torque/server_name
