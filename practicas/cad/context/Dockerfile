FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y libnet-ifconfig-wrapper-perl \
&& apt-get install -y iputils-ping \
&& apt-get install -y ssh \
&& apt-get install -y locales \
&& apt-get install -y openssh-server \
&& localedef -i es_ES -c -f UTF-8 \
-A /usr/share/locale/locale.alias es_ES.UTF-8
ENV LANG es_ES.UTF-8
RUN useradd juan
RUN mkdir /home/juan
# Se van a copiar las claves en /tmp del contenedor (/tmp/id_ed25519 y /tmp/id_ed25519.pub)
COPY ./claves_compartidas /tmp
COPY ./delta_hosts /tmp
RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
COPY entrypoint.sh /
EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]

