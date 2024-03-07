from typing import List
from fmc_api.models.object import NetworkObject, HostObject, NetworkGroups, RangeObject, FQDNObject

def list_network_objects(self)->List[NetworkObject]:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networks?limit=100')
    api_answer = self.get(target)
    raw_answer = api_answer.json()
    raw_objs = raw_answer['items']

    pages = raw_answer['paging']['pages']
    offset = raw_answer['paging']['limit']
    while pages > 1:
        target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networks?limit=100&offset={offset}')
        api_answer = self.get(target)        
        pages -= 1
        offset += 100
        raw_answer = api_answer.json()
        raw_objs += raw_answer['items']

    objs = []
    for obj in raw_objs:
        objs.append(NetworkObject(**obj))
    return objs

def delete_network_object(self, object_uuid:str)->bool:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networks/{object_uuid}')
    api_answer = self.delete(target)
    if api_answer.status_code == 403:
        # Forbidden, system object
        return False
    elif api_answer.status_code == 400:
        return False
    elif api_answer.status_code == 200:
        return True
    

def list_host_objects(self)->List[HostObject]:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/hosts?limit=100&expanded=true')
    api_answer = self.get(target)
    raw_answer = api_answer.json()
    raw_objs = raw_answer['items']

    pages = raw_answer['paging']['pages']
    offset = raw_answer['paging']['limit']
    while pages > 1:
        target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/hosts?limit=100&offset={offset}&expanded=true')
        api_answer = self.get(target)        
        pages -= 1
        offset += 100
        raw_answer = api_answer.json()
        raw_objs += raw_answer['items']

    objs = []
    for obj in raw_objs:
        objs.append(HostObject(**obj))
    return objs

def delete_host_object(self, object_uuid:str)->bool:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/hosts/{object_uuid}')
    api_answer = self.delete(target)
    if api_answer.status_code == 403:
        # Forbidden, system object
        return False
    elif api_answer.status_code == 400:
        return False
    elif api_answer.status_code == 200:
        return True
    
def list_networkgroups_objects(self)->List[NetworkGroups]:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networkgroups?limit=100')
    api_answer = self.get(target)
    raw_answer = api_answer.json()
    raw_objs = raw_answer['items']

    pages = raw_answer['paging']['pages']
    offset = raw_answer['paging']['limit']
    while pages > 1:
        target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networkgroups?limit=100&offset={offset}')
        api_answer = self.get(target)        
        pages -= 1
        offset += 100
        raw_answer = api_answer.json()
        raw_objs += raw_answer['items']

    objs = []
    for obj in raw_objs:
        objs.append(NetworkGroups(**obj))
    return objs

def delete_networkgroups_object(self, object_uuid:str)->bool:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/networkgroups/{object_uuid}')
    api_answer = self.delete(target)
    if api_answer.status_code == 403:
        # Forbidden, system object
        return False
    elif api_answer.status_code == 400:
        return False
    elif api_answer.status_code == 200:
        return True
    
def list_range_objects(self)->List[RangeObject]:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/ranges?limit=100')
    api_answer = self.get(target)
    raw_answer = api_answer.json()
    raw_objs = raw_answer['items']

    pages = raw_answer['paging']['pages']
    offset = raw_answer['paging']['limit']
    while pages > 1:
        target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/ranges?limit=100&offset={offset}')
        api_answer = self.get(target)        
        pages -= 1
        offset += 100
        raw_answer = api_answer.json()
        raw_objs += raw_answer['items']

    objs = []
    for obj in raw_objs:
        objs.append(RangeObject(**obj))
    return objs

def delete_range_object(self, object_uuid:str)->bool:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/ranges/{object_uuid}')
    api_answer = self.delete(target)
    if api_answer.status_code == 403:
        # Forbidden, system object
        return False
    elif api_answer.status_code == 400:
        return False
    elif api_answer.status_code == 200:
        return True
    
def list_fqdn_objects(self)->List[RangeObject]:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/fqdns?limit=100&expanded=true')
    api_answer = self.get(target)
    raw_answer = api_answer.json()
    raw_objs = raw_answer['items']

    pages = raw_answer['paging']['pages']
    offset = raw_answer['paging']['limit']
    while pages > 1:
        target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/fqdns?limit=100&offset={offset}&expanded=true')
        api_answer = self.get(target)        
        pages -= 1
        offset += 100
        raw_answer = api_answer.json()
        raw_objs += raw_answer['items']

    objs = []
    for obj in raw_objs:
        objs.append(FQDNObject(**obj))
    return objs

def delete_fqdn_object(self, object_uuid:str)->bool:
    target = self.generate_url(f'fmc_config/v1/domain/{self.domain}/object/fqdns/{object_uuid}')
    api_answer = self.delete(target)
    if api_answer.status_code == 403:
        # Forbidden, system object
        return False
    elif api_answer.status_code == 400:
        return False
    elif api_answer.status_code == 200:
        return True