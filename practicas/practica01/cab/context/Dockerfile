FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y \
&& apt-get install -y libnet-ifconfig-wrapper-perl \
&& apt-get install -y iputils-ping \
&& apt-get install -y ssh \
&& apt-get install -y openssh-server
COPY ./delta_hosts /tmp

RUN mkdir /var/run/sshd
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

COPY entrypoint.sh /

EXPOSE 22
ENTRYPOINT ["/entrypoint.sh"]

