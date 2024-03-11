import nmap

# Crie um objeto NmapScanner
nm = nmap.PortScanner()

# Realize um escaneamento básico de um host
nm.scan('192.168.1.1', '22-80')

# Itere sobre os resultados do escaneamento
for host, result in nm.all_hosts().items():
    print(f'Host: {host}')
    for protocol, ports in result.items():
        print(f'Protocol: {protocol}')
        for port, state in ports.items():
            print(f'Port: {port}, State: {state}')

# Exiba informações sobre um host específico
print(f"Host state: {nm['192.168.1.1'].state()}")