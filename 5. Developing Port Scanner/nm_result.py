import nmap

nm = nmap.PortScanner()
result = nm.scan(hosts="127.0.0.1",ports='20-443', arguments='-sV')

for host in nm.all_hosts():
    print('-------------------------------------------------')
    print('Host : %s (%s)' %(host, nm[host].hostnames()))
    print('State : %s' % nm[host].state())
    proto = 'tcp'
    print('--------')
    print('Protocol : %s' %proto)
    lport = nm[host][proto].keys()
    for port in sorted(lport):
        print ('port : %s\tstate : %s' % (port,str(nm[host][proto][port]['state'])))

