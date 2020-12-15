# Goal

For testing purposes we often need to create hardware_data files with realistic data that have unique IP addresses based on a given CIDR string and unique MAC addresses.

# Usage

The script expects the following parameters
1. gateway (e.g. 192.168.1.1)
2. CIDR string (e.g. 192.168.1.0/28)
3. MAC address file (A file containing MAC addresses separated by newlines)

Use this to pipe each hardware_json into a separate file:

(_NOTE: Run it to stdout first to check there are no errors as the following command assumes a fixed number of lines per hardware_json and the error output will break it. I need to add an option in the script to output to files to get around this so it can later deal with different schemas._)

`mkdir output_files`


`python3 ./write_hardware_jsons.py 192.168.1.1 192.168.1.0/28 ./MACS.txt | split -l 30 - ./output_files/hardware_data-`

# NOTES
1. It will drop out gracefully if you have more MACs in the input file than can fit in the IP space given by the CIDR as you can see in the second example

# Examples

_The repository contains an example input file called MACs.txt_

- Example input with enough IP space to create all hardware_jsons

`python3 ./write_hardware_jsons.py 192.168.1.1 192.168.1.0/28 ./MACS.txt`

- Output

```json
{
  "id": "0dd32a37-7c94-430d-abbe-18ae6686e5cf",
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
            "netmask": "255.255.255.240"
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
  "id": "92cfcdec-8979-457b-bccb-ed68910b7005",
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
            "netmask": "255.255.255.240"
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
  "id": "d902cd80-8e9c-427e-8f80-810dfb1b7049",
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
            "netmask": "255.255.255.240"
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
  "id": "011d1291-9aea-4ffb-b67a-c0ede3ca4908",
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
            "netmask": "255.255.255.240"
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
  "id": "a820ed64-c946-4bf4-8216-a6a08ee58154",
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
            "netmask": "255.255.255.240"
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
}
```

- Example input without enough IP space to create all hardware_jsons

`python3 ./write_hardware_jsons.py 192.168.1.1 192.168.1.0/31 ./MACS.txt`

- Output

```json
{
  "id": "1654a1f1-aa57-4574-9c3e-b743b2f52a24",
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
            "netmask": "255.255.255.254"
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
  "id": "665ac5c8-a334-43ac-9432-16bab653919c",
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
            "netmask": "255.255.255.254"
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
```
