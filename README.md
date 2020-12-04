# Goal

For testing purposes we often need to create hardware_data files with realistic data that have unique IP addresses based on a given CIDR string and unique MAC addresses.

# Usage

The script expects the following parameters
1. gateway
2. netmask
3. CIDR string
4. MAC address file

Use this to pipe each hardware_json into a separate file:

(_NOTE: Run it to stdout first to check there are no errors as the following command assumes a fixed number of lines per hardware_json and the error output will break it. I need to add an option in the script to output to files to get around this so it can later deal with different schemas._)

`mkdir output_files
python3 ./write_hardware_jsons.py 192.168.1.1 255.255.255.248 192.168.1.0/28 ./MACS.txt | split -l 30 - ./output_files/hardware_data-`

# NOTES
1. It will drop out gracefully if you have more MACs in the input file than can fit in the IP space given by the CIDR as you can see in the second example

# Examples

_The repository contains an example input file called MACs.txt_

- Example input with enough IP space to create all hardware_jsons

`python3 ./write_hardware_jsons.py 192.168.1.1 255.255.255.248 192.168.1.0/28 ./MACS.txt`

- Output

`{
  "id": "09a71298-9013-4234-ae39-ffbdb07fadb8",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.0",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:01",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
{
  "id": "9ef29ed1-f1ab-4f22-bee2-06f63f1f63da",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.1",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:02",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
{
  "id": "7b140a22-0707-4a27-b76c-0977bedecfac",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.2",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:03",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
{
  "id": "d266f961-8a74-457d-aa69-24c97cc1c681",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.3",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:04",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
{
  "id": "0993606b-31bb-4046-b1a8-6b06e4c2ab93",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.4",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:05",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}`

- Example input without enough IP space to create all hardware_jsons

` ./write_hardware_jsons.py 192.168.1.1 255.255.255.248 192.168.1.0/31 ./MACS.txt`

- Output

`{
  "id": "87ab4e23-734b-444f-aaf2-bba0d637dd00",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.0",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:01",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
{
  "id": "92db9ce7-1025-49f9-826b-478c789f3fcb",
  "metadata": {
    "facility": {
      "facility_code": "onprem"
    },
    "instance": {},
    "state": ""
  },
  "network": {
    "interfaces": [
      {
        "dhcp": {
          "arch": "x86_64",
          "ip": {
            "address": "192.168.1.1",
            "gateway": "192.168.1.1",
            "netmask": "255.255.255.248"
          },
          "mac": "08:00:27:00:00:02",
          "uefi": false
        },
        "netboot": {
          "allow_pxe": true,
          "allow_workflow": true
        }
      }
    ]
  }
}
Cannot allocate IP for 08:00:27:00:00:03 on line 3. Insufficient IP space in range: 192.168.1.0/31
address out of range
