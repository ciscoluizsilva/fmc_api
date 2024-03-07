from fmc_api import SecureFWMgmt
from typing import List
from fmc_api.utility import pick_domain
from getpass import getpass


def clean():
    host = input("Insert FMC IP/FQDN: ")
    username = input("Username: ")
    password = getpass(f"Password for {username}: ")
    fmc = SecureFWMgmt(host=host, username=username, password=password)
    domain_uuid = pick_domain(fmc)
    fmc.set_domain(domain_uuid)

    # Cleaning the groups
    print("Deleting Unused Group Objects...")
    groups_obj = fmc.list_networkgroups_objects()
    for o in groups_obj:
        fmc.delete_networkgroups_object(o.id)

    print("Deleting Unused Network Objects...")
    net_objs = fmc.list_network_objects()
    for o in net_objs:
        fmc.delete_network_object(o.id)

    print("Deleting Unused Host Objects...")
    host_objs= fmc.list_network_objects()
    for o in host_objs:
        fmc.delete_host_object(o.id)

    print("Deleting unused Ranges...")
    range_objs = fmc.list_range_objects()
    for o in range_objs:
        fmc.delete_range_object(o.id)

    print("Deleting unused FQDNs...")
    range_objs = fmc.list_fqdn_objects()
    for o in range_objs:
        fmc.delete_fqdn_object(o.id)