import paramiko

class SSHClient:
    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect(self):
        try:
            self.client.connect(hostname=self.host, username=self.username, password=self.password)
            print("Connected to the Storage Array.")
        except paramiko.AuthenticationException:
            print("Authentication failed, please verify your credentials.")
        except paramiko.SSHException as e:
            print("SSH connection failed:", str(e))
        except Exception as e:
            print("An error occurred:", str(e))

    def execute_command(self, command):
        stdin, stdout, stderr = self.client.exec_command(command)
        return stdout.read().decode()

    def close(self):
        self.client.close()
        print("SSH connection closed from storage Array.")