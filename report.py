#!/usr/bin/env python

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pynetbox

nb = pynetbox.api(
  'https://localhost',
  token='3cd90773e3283637eee1103a5a97a3a5eebf9d74',
  ssl_verify=False
)

cpu = 0
disk = 0
mem = 0

with open('vm_list') as f:
    for vm in f.readlines():
      vm = vm.strip()
      vm = vm[:64]
      vm_obj = nb.virtualization.virtual_machines.get(name=vm)
      if not vm_obj:
        print(f"Could not find VM: {vm}")
        continue
      print(f"Name: {vm}\tDisk: {vm_obj.disk}GB\tMemory: {vm_obj.memory}MB\tCPU:{vm_obj.vcpus}")
      cpu += vm_obj.vcpus
      mem += vm_obj.memory
      disk += vm_obj.disk

print(f"Total resources:")
print(f"Disk: {disk} GB")
print(f"Memory: {mem} MB")
print(f"CPUs: {cpu}")
