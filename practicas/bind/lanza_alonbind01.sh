#!/bin/bash
docker run --rm -it -h alonbind01 --name alonbind01 \
-v $HOME/lagrs/practica01/bind/context:/home/$USER \
alonsod29/bind
