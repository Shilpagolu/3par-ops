from array_ops.array_data import (
    precheck_showsys,
    precheck_showsysmgr,
    precheck_shownode,
    precheck_showport,
    precheck_showvv,
    precheck_showvlun,
    precheck_showhost,
    precheck_showpd,
    precheck_showcage,
    precheck_clwait,
)
from utils.ssh_utils import SSHClient

def main():
    host = "10.157.208.240"
    username = "root"
    password = "ssmssm"

    # Create an SSH client
    ssh_client = SSHClient(host, username, password)
    ssh_client.connect()

    # Call precheck methods
    print(precheck_showsys(ssh_client))

    # Close the SSH connection
    ssh_client.close()

if __name__ == "__main__":
    main()
