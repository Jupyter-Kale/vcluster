#!/usr/bin/env bash

touch /tmp/scratch/test.out
for i in {0..100}
do
   date >> /tmp/scratch/test.out
   echo "Sleeping for 3 seconds..." >> test.out
   sleep 3
done
