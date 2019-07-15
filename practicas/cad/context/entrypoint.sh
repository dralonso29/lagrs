#!/bin/bash
#copiamos ficheros
cat /tmp/delta_hosts >> /etc/hosts
mkdir /home/juan/.ssh
cat /tmp/id_ed25519.pub >> /home/juan/.ssh/authorized_keys
#cambiamos metadatos directorio /home/juan
chown juan /home/juan
chgrp juan /home/juan
chown juan /home/juan/.ssh
chgrp juan /home/juan/.ssh
chown juan /home/juan/.ssh/*
chgrp juan /home/juan/.ssh/*
#cambiamos permisos
chmod 0700 /home/juan/.ssh
chmod 0600 /home/juan/.ssh/*
echo "IdentifyFile ~/.ssh/id_ed25519" >> /etc/ssh/ssh_config
#lanzamos el sever
/usr/sbin/sshd
#lanzamos el shell
/bin/bash

