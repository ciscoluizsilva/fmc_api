import requests
from requests.auth import HTTPBasicAuth
from typing_extensions import Self
from typing import Any
from pydantic import BaseModel, Field, model_validator
import time

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class SecureFWMgmt(BaseModel):
    from .domains import list_domains, set_domain
    from .objects import list_network_objects,delete_network_object, list_host_objects, delete_host_object
    from .objects import list_networkgroups_objects, delete_networkgroups_object, list_range_objects, delete_range_object
    from .objects import list_fqdn_objects, delete_fqdn_object


    host: str = Field(description="Secure Firewall Management Center Host, IP or FQND")
    username: str = Field(default='admin', description="Secure Firewall Management Center Host, IP or FQND")
    verify_cert:bool = Field(default=False, description='Will verify the certification or not')
    password:str = None
    current_token:str = None
    refresh_token:str = None
    session:Any = None
    refresh_count:int = 0
    token_timeout:int = 0
    domain:str = None
    
    @model_validator(mode='after')
    def verify_credentials(self) -> Self:
        self.authenticate()
        if self.current_token is not None:
            print("Auth Successful.")
        return self
    
    def generate_url(self, target)->str:
        base_url = f'https://{self.host}/api/'
        return f'{base_url}{target}'
    
    def authenticate(self):
        target = self.generate_url('fmc_platform/v1/auth/generatetoken')
        auth = HTTPBasicAuth(self.username, self.password)
        try:
            response = requests.post(target, auth=auth, data='', verify=self.verify_cert)
        except Exception as e:
            raise ValueError("Host most likely is invalid?")
        if response.status_code == 204:
            # auth successful
            self.current_token = response.headers['X-auth-access-token']
            self.refresh_token = response.headers['X-auth-refresh-token']
            self.token_timeout = int(time.time()) + 1800
        else:
            raise ValueError('Credentials set are invalid.')

    def token_refresh(self):
        if self.token_timeout > int(time.time()):
            return
        if self.refresh_count >= 3:
            self.authenticate()
            return
        target = self.generate_url('fmc_platform/v1/auth/refreshtoken')
        headers = self.generate_header_x_auth()
        headers['X-auth-refresh-token'] = self.refresh_token
        response = requests.post(target, headers=headers, data='', verify=self.verify_cert)
        if response.status_code == 204:
            # auth successful
            self.current_token = response.headers['X-auth-access-token']
            self.refresh_token = response.headers['X-auth-refresh-token']
            self.token_timeout = int(time.time()) + 1800
        else:
            raise ValueError('Refreshing token failed...')

    def generate_header_x_auth(self):
        return {'X-auth-access-token': self.current_token}

    def get(self, target):
        self.token_refresh()
        try:
            response = requests.get(target, headers=self.generate_header_x_auth(), verify=self.verify_cert)
        except Exception as e:
            raise ValueError("Host most likely went offline ?")
        return response

    def __post(self, target, content=None):
        pass

    def __put(self, target, content=None):
        pass

    def delete(self, target):
        self.token_refresh()
        try:
            response = requests.delete(target, headers=self.generate_header_x_auth(), verify=self.verify_cert)
        except Exception as e:
            raise ValueError("Host most likely went offline ?")
        return response