FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y libnet-ifconfig-wrapper-perl \
&& apt-get install -y iputils-ping \
&& apt-get install -y ssh
COPY ./delta_hosts /tmp
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

