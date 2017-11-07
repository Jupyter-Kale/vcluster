#!/usr/bin/env bash

pass=`date -I`

until lpad reset --password $pass
do
   sleep 0.1
done

lpad webgui
