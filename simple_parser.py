def simple_parser(line):
    
    # looks for the substring ' port ' and returns the following port number.
    # Returns None if no matching substring found.

    if " port " in line:
        parts = line.split()  # splits the line into tokens, separates by spaces by default
        try:
            anchor = parts.index("port")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None