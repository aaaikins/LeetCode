class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        addresses = set()
        
        for email in emails:
            local, domain = email.split("@")
            name = local.split("+")[0]
            name = name.replace('.','')
            addresses.add((name, domain))
        return len(addresses)

        