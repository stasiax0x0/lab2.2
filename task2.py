def ip_parser(line):
    if " from " in line:
        parts = line.split()    #splits the line in tokens and separates by space by default
        try:
            anchor = parts.index("from")     #find where from is -> this is the anchor
            ip = parts[anchor+1]            #the ip is the next token
            return ip.strip()               #remove any punctuation

        except (ValueError, IndexError):
            return None
        return None

#task2

#count failed login attempts per ip
#Using defaultdict(int) (or normal dict) count how many failed attempts each IP has.
#Only count lines containing Failed password or Invalid user.
#Print the counts for all IPs.

from collections import defaultdict

def task2():
    counts = defaultdict(int)           #create a dictionary to keep track of ips

    with open("sample_auth_small.log") as file:
        for line in file:
            if "Failed password" in line or "Invalid user" in line:
                ip = ip_parser(line)        #extract ip
                if ip:
                    counts[ip] +=1
    print(counts)
task2()         #run task 2
