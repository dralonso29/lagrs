#!/usr/bin/python -tt
#romanclient.py
# Miguel, marzo 2012
import socket,sys
MAXLEN = 1024
TIMEOUT = 5

def send_tcp_request(host,port,message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(message)
    data = s.recv(1024)
    s.close()
    print  data

def  send_udp_request(server,port,message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(TIMEOUT)
    sock.connect((server, port))
    sock.send(message)
    try:
        msg = sock.recv(MAXLEN)
        ipaddr, port = sock.getpeername()
        hishost = socket.gethostbyaddr(ipaddr)
        print "Server %s responded ``%s''" % ( hishost[0], msg)
    except:
        print "recv from %s failed (timeout or no server running)." % ( server )
    sock.close()


def die(msg,log=""):
    sys.stderr.write(log+'\n')
    sys.stderr.write('Error:\n')
    sys.stderr.write(msg+'\n')
    raise SystemExit

def usage():
     print sys.argv[0]+" <SERVER> [TCP|UDP] <PORT> <MESSAGE>"

def main():
    if len(sys.argv[1:])!=4:
        usage()
        die("Wrong arguments")

    server=sys.argv[1]

    protocol=sys.argv[2].lower()
    if protocol != "tcp" and protocol != "udp":
        msg = "Second argument (protocol)  must be tcp or udp"
        usage()
        die(msg)

    try:
        port=int(sys.argv[3])
    except ValueError :
        msg = "Wrong port number "+sys.argv[1]
        usage()
        die(msg)

    message=sys.argv[4]

    if protocol=="tcp":
        send_tcp_request(server,port,message)

    if protocol=="udp":
        send_udp_request(server,port,message)

if __name__ == "__main__":
    main()
