from typing import List
from fmc_api.models.domain import Domain

def list_domains(self)->List[Domain]:
    target = self.generate_url('fmc_platform/v1/info/domain')
    api_answer = self.get(target)

    raw_answer = api_answer.json()
    domains = []
    for domain in raw_answer['items']:
        domains.append(Domain(**domain))
    return domains