import ipaddress
import uuid
import sys
import json

def write_hardware_json(ip_address, gateway, netmask, MAC, uuid):

    ##### ip
    ip = {}
    ip['address']   = str(ip_address)
    ip['gateway']   = gateway
    ip['netmask']   = netmask

    #### dhcp
    dhcp = {}
    dhcp['arch']    = 'x86_64'
    dhcp['ip']      = ip
    dhcp['mac']     = MAC
    dhcp['uefi']    = False

    #### netboot
    netboot                     = {}
    netboot['allow_pxe']        = True
    netboot['allow_workflow']   = True

    ### interfaces
    interfaces = []
    interfaces.append({})

    ### facility
    facility = {}
    facility['facility_code'] = 'onprem'

    ### interfaces 1
    interfaces[0]['dhcp']       = dhcp
    interfaces[0]['netboot']    = netboot
    
    ## network
    network = {}
    network['interfaces']       = interfaces


    ## metadata
    metadata = {}
    metadata['facility']    = facility
    metadata['instance']    = {}
    metadata['state']       = ''
    
    # hardware_data
    hardware_data = {}
    hardware_data['id']         = uuid
    hardware_data['metadata']   = metadata
    hardware_data['network']   = network

    print(json.dumps(hardware_data, indent=2))

def main():

    # Command line arguments
    # 1. gateway
    # 2. netmask
    # 3. CIDR string
    # 4. MAC address file

    # Parse command line arguments
    NUM_CMD_LINE_ARGUMENTS = 4

    if((len(sys.argv) - 1) != NUM_CMD_LINE_ARGUMENTS):
        print('Invalid command line argument') # TODO Print help here
        exit(1)
    else:
        gateway                 = sys.argv[1]
        netmask                 = sys.argv[2]
        CIDR_string             = sys.argv[3]
        MAC_address_file_path   = sys.argv[4]        

    # Create CIDR object and check it is valid else exit
    try:
        CIDR = ipaddress.ip_network(CIDR_string)
    except ValueError:
        print('Invalid CIDR: %s Did you set the host bits?' % CIDR_string)
        exit(1)

    # Read MACs from input file to list
    f = open(MAC_address_file_path, "r", encoding="utf-8")
    MACS = f.read().splitlines()
    ip_counter = 0

    # Iterate through MACs in input file until no more MACs or no more IP space in subnet
    for MAC in MACS:
        try:
            write_hardware_json(CIDR[ip_counter], gateway, netmask, MAC, str(uuid.uuid4()))
            ip_counter += 1
        except IndexError as ex:
                print("Cannot allocate IP for %s on line %s. Insufficient IP space in range: %s" % (MAC, ip_counter+1, CIDR_string))
                print(ex)
                f.close()
                exit(1)
            

    # Close file handle if we enoutered no exceptions
    f.close()

if __name__ == "__main__":
    main()
