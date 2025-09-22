def ip_parser(line):
    """
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    """
    if " from " in line:
        parts = line.split()     # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("from")    # Find the position of the token "port", our anchor
            ip = parts[anchor+1]          # the port value will be next token, anchor+1
            return ip.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None

    if __name__ == "__main__":
        with open(sample_auth_small.log, "r") as f:
            for line in f:
                print (ip_parser(line.strip()))

    print("Lines read:")
    print("Unique ips:")
    print("First 10 ips:")