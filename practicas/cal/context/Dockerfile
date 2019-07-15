FROM ubuntu:18.04
RUN apt-get update && apt-get upgrade -y && apt-get install -y bsdmainutils
COPY entrypoint.sh /
ENTRYPOINT ["/entrypoint.sh"]

