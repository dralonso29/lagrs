FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y libnet-ifconfig-wrapper-perl \
&& apt-get install -y iputils-ping \
&& apt-get install -y ssh \
&& apt-get install -y locales \
&& localedef -i es_ES -c -f UTF-8 \
-A /usr/share/locale/locale.alias es_ES.UTF-8
ENV LANG es_ES.UTF-8
COPY ./claves_compartidas /tmp
COPY ./delta_hosts /tmp
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]
