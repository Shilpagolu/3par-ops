from utils.ssh_utils import SSHClient
import re
import time


def controlport_offline(ssh_client, port_number):
    print("Controlport Offline: Waiting 45 secs before proceeding to next step")
    time.sleep(45)
    command = f" echo y | controlport offline {port_number}"
    command_output = ssh_client.execute_command(command)
    print(f"Port {port_number} is offline now")

def controlport_reset(ssh_client, port_number):
    print("Controlport Reset: Waiting 45 secs before proceeding to next step")
    time.sleep(45)
    command = f"controlport rst -f {port_number}"
    command_output = ssh_client.execute_command(command)
    print(f"Port {port_number} is reset now")

def get_port_info(ssh_client, port_number):
    print("Get Port Info: Waiting 45 secs before proceeding to next step")
    time.sleep(45)
    command = "showport"
    command_output = ssh_client.execute_command(command)
    # Parse the command output to find the specific port information
    port_info = [line for line in command_output.splitlines() if re.search(fr"\b{port_number}\b", line)]
    return port_info

def main():
    host = "10.157.208.240"
    username = "root"
    password = "ssmssm"

    port_number = "1:4:1"  # Replace this with the actual port number you want to perform operations on

    # Create an SSH client
    ssh_client = SSHClient(host, username, password)
    ssh_client.connect()

    # Perform port perturbations
    port_info = get_port_info(ssh_client, port_number)
    print("Current port status : ")
    print(f"Port Information: {port_info}")

    print("Making port offline ")
    controlport_offline_output = controlport_offline(ssh_client, port_number)
    print(f"Controlport Offline Output: {controlport_offline_output}")

    print("Current port status : ")
    port_info = get_port_info(ssh_client, port_number)
    print(f"Port Information: {port_info}")

    print("Making port online with soft reseting the port : ")
    controlport_reset_output = controlport_reset(ssh_client, port_number)
    print(f"Controlport Reset Output: {controlport_reset_output}")

    print("Checking port status: ")
    port_info = get_port_info(ssh_client, port_number)
    print(f"Port Information: {port_info}")

    # Close the SSH connection
    ssh_client.close()

if __name__ == "__main__":
    main()
