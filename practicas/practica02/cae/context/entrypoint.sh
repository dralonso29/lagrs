#!/bin/bash
cat /tmp/delta_hosts >> /etc/hosts
mkdir ~/.ssh
cp /tmp/id_ed25519 ~/.ssh
chmod 0700 ~/.ssh
chmod 0600 ~/.ssh/*
/bin/bash
