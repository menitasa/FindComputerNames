import winrm
import findhost_credentials  # Import domain user Credentials

computers_list = []
# Connect to Remote machine using winrm
session = winrm.Session(findhost_credentials.host,
                        auth=('{}@{}'.format(findhost_credentials.user, findhost_credentials.domain), findhost_credentials.password),
                        transport='ntlm')

# run Powershell block
result = session.run_ps(
    'Get-DnsServerResourceRecord -ZoneName "Domain.com"  -RRType "A" | Select-Object "HostName" | Format-List')


clear = str(result.std_out).replace("\\r\\n\\r\\n", '')
clear = clear.replace("HostName", '')
clear = clear.replace('@', '')
clear = clear.replace("b'", '')
clear = clear.replace(":", '')
clear = clear.split()

computers = set(clear)  # Remove duplicates
computers = (list(computers))
for host in computers:
    full_hostname = host + ".domain.com"
    computers_list.append(full_hostname)
print(computers_list)


