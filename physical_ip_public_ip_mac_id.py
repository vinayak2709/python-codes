import urllib.request
import socket
import uuid

hostname = socket.gethostname()

IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)

print("mac_id :", end="")
print(':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
                for ele in range(0, 8 * 6, 8)][::-1]))

external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

print("Your public IP Address is:" + external_ip)


