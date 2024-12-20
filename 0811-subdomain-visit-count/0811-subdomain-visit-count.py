class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hashmap = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            hashmap[domain] = hashmap.get(domain, 0) + int(count)
            subdomains = domain.split('.')[1:]
            print(hashmap)
            # if len(subdomains) == 1:
            #     hashmap[subdomains] = hashmap.get(subdomains, 0) + int(count)
            for i, s in enumerate(subdomains):
                subdomain = ".".join(subdomains[i:])
                hashmap[subdomain] = hashmap.get(subdomain, 0) + int(count)
        res = []
        for k, val in hashmap.items():
            cpd = str(val) + " " + k
            res.append(cpd)
        return res
        