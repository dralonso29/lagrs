#!/usr/bin/python -tt
# romanserver.py   Miguel, febrero 2012
import socket, sys, SocketServer

# From https://pypi.python.org/pypi/numeral/0.1.0.10
def int2roman(number):
    numerals = { 1 : "I", 4 : "IV", 5 : "V", 9 : "IX", 10 : "X", 40 : "XL", 
        50 : "L", 90 : "XC", 100 : "C", 400 : "CD", 500 : "D", 900 : "CM", 1000 : "M" }
    result = ""
    for value, numeral in sorted(numerals.items(), reverse=True):
        while number >= value:
            result += numeral
            number -= value
    return result

def parse_data(data):
    try:
        numero=int(data)
    except ValueError :
        return "Not a valid number:"+data
    arabic=int(data)
    if arabic <1 :
        return "Not a valid number:"+data
    roman=int2roman(arabic)
    return roman

def get_tcp_conection(port):
    HOST = ''                 # Symbolic name meaning all available interfaces
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, port))
    while 1:
        s.listen(1)
        conn, addr = s.accept()
        print 'Connected by', addr
        while 1:
            data = conn.recv(1024)
            if not data: break
            print data
            conn.send(parse_data(data))
    conn.close()

# http://pleac.sourceforge.net/pleac_python/sockets.html
class handler(SocketServer.DatagramRequestHandler):  # udp
    def handle(self):
        data = self.rfile.readline().rstrip()
        print "Client %s said %s" % (self.client_address[0], data)

        self.wfile.write(parse_data(data))

def get_udp_data(port):
    s = SocketServer.UDPServer(('',port), handler)
    print "Awaiting UDP messages on port %d" % port
    s.serve_forever()

def die(msg,log=""):
    sys.stderr.write(log+'\n')
    sys.stderr.write('Error:\n')
    sys.stderr.write(msg+'\n')
    raise SystemExit

def usage():
     print sys.argv[0]+" [TCP|UDP] <PORT>"

def main():
    if len(sys.argv[1:])!=2:
        usage()
        die("Wrong arguments")
        
    protocol=sys.argv[1].lower()
    if protocol != "tcp" and protocol != "udp":
        usage()
        msg = "First argument (protocol)  must be TCP or UDP"
        die(msg)
    try:
        port=int(sys.argv[2])
    except ValueError :
        usage()
        msg = "Wrong port number "+sys.argv[1]
        die(msg)

    if protocol=="tcp":
        get_tcp_conection(port)

    if protocol=="udp":
        get_udp_data(port)

    die("Error, flow should never arrive here")

if __name__ == "__main__":
    main()
