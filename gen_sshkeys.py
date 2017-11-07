#!/usr/bin/env python

# stdlib
import argparse
import getpass
import os
import socket

# 3rd party
import paramiko

def gen_sshkeys():
    print("Generating ssh keys")
    if os.path.exists('ssh/id_rsa'):
        print("Private keyfile exists, skipping ssh keygen")
        return
    else:
        print("Generating new ssh private keyfile")
        private_key = paramiko.rsakey.RSAKey.generate(2048)
        private_key.write_private_key_file('ssh/id_rsa')
        print("Generating new ssh public keyfile")
        with open('ssh/id_rsa.pub', 'w') as f:
            id = getpass.getuser() + '@' + socket.getfqdn()
            f.write("{} {} {}".format(private_key.get_name(),
                                      private_key.get_base64(),
                                      id))

if __name__ == "__main__":
    gen_sshkeys()
