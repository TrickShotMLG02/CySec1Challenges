# Name: Tim Schlachter
# Matriculation number: 7039326

import dns.resolver


def resolve(domain: str) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """
    This method runs queries to find all NS and their IP addresses for both the tld and domain name
    Args:
        domain: without . at the end
    Returns:
        a list of tuples with Nameservers and their IP for tld and the same for the domain name
    """
    pass


if __name__ == "__main__":
    domain = "websec.saarland"
    expected_nameservers_tld = {('a.nic.saarland.', '194.169.218.97'), ('b.nic.saarland.', '185.24.64.97'),
                                 ('c.nic.saarland.', '212.18.248.97'), ('d.nic.saarland.', '212.18.249.97')}

    expected_nameservers_domain_name = {('ns1.domaindiscount24.net.', '94.23.153.36'),
                                        ('ns2.domaindiscount24.net.', '66.206.3.125'),
                                        ('ns3.domaindiscount24.net.', '144.217.35.18')}

    nameservers_tld, nameservers_domain_name = resolve(domain)

    print(f"Nameservers for TLD:                        {set(nameservers_tld)}")
    print(f"Expected nameservers for TLD:               {expected_nameservers_tld}")
    print(f"Worked:                                     {set(nameservers_tld) == expected_nameservers_tld}")
    print()
    print(f"Nameservers for the domain name:            {set(nameservers_domain_name)}")
    print(f"Expected nameservers for the domain name:   {expected_nameservers_domain_name}")
    print(f"Worked:                                     {set(nameservers_domain_name) == expected_nameservers_domain_name}")
