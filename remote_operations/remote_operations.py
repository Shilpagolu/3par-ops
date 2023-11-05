import paramiko

import paramiko

def run_remote_commands(hostname, username, password, commands):
    # Establish an SSH connection
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=hostname, username=username, password=password)
        print("Connected to the remote server.")

        # Execute remote commands
        command_output = ""
        for command in commands:
            stdin, stdout, stderr = ssh.exec_command(command)
            command_output += stdout.read().decode()
            command_output += stderr.read().decode()

            # For debugging purposes, print the command output
            print(f"Command: {command}")
            print("Output:")
            print(command_output)
            print("Error (if any):")
            print(stderr.read().decode())
            print("-" * 50)

        return command_output  # Return the command output

    except paramiko.AuthenticationException:
        print("Authentication failed, please verify your credentials.")
    except paramiko.SSHException as e:
        print(f"SSH connection failed: {e}")
    finally:
        # Close the SSH connection
        ssh.close()


# Example usage
if __name__ == "__main__":
    # Remote server details
    hostname = "10.157.208.240"
    username = "root"
    password = "ssmssm"

    # Commands to be executed on the remote server
    commands = [
        "ls",
        "pwd",
        "echo 'Hello, Remote Server!'"
    ]

    run_remote_commands(hostname, username, password, commands)
