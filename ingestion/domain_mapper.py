def map_domain(filename: str, domain_config: dict) -> str:
    """
    Map a filename to a clinical domain using keyword rules.

    Returns:
    - domain name (safety, labs, data_quality, coding, operations)
    - 'unknown' if no match is found
    """

    filename_lower = filename.lower()

    for domain, keywords in domain_config.items():
        for keyword in keywords:
            if keyword.lower() in filename_lower:
                return domain

    return "unknown"
 