import nmap

nm = nmap.PortScanner()
result = nm.scan(hosts="127.0.0.1",ports='20-443', arguments='-sV')
print(result)
