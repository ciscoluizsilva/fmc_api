from fmc_api import SecureFWMgmt

def pick_domain(fmc_api)->str:
    domains = fmc_api.list_domains()
    for i, domain in enumerate(domains):
        print(i+1, domain.name)
    d = input("Select Domain: ")
    try:
        d_int = int(d)
    except ValueError:
        raise
    try:
        selected_domain = domains.pop(d_int-1)
    except:
        # wrong index ?
        print("Index selected is wrong...")
        raise
    return selected_domain.uuid