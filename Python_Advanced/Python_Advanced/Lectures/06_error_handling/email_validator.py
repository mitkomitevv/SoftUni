class NameTooShortError(Exception):
    """Name must be more than 4 characters"""
    pass

class MustContainAtSymbolError(Exception):
    """Email must contain @"""
    pass

class InvalidDomainError(Exception):
    """Domain must be one of the following: .com, .bg, .org, .net"""
    pass

valid_domains = {".com", ".bg", ".org", ".net"}

email = input()
while email != 'End':
    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    elif len(email[:email.index('@')]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif not any(email.endswith(domain) for domain in valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")
    email = input()
