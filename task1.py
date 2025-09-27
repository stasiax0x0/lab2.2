
#task 1
def ip_parser(line):            #define a function that has line as a parameter
    if " from " in line:        #if " from " is the line
        parts = line.split()    #splits the line in tokens and separates by space by default
        try:
            anchor = parts.index("from")     #find where from is -> this is the anchor
            ip = parts[anchor+1]            #the ip is the next token
            return ip.strip()               #remove any punctuation

        except (ValueError, IndexError):
            return None
        return None

#task1.2

def task1_2():
#read the file "sample_auth_small.log" and find unique ips

    unique_ips = set()          #this creates a set
    line_count = 0              #initialise line_count as 0

    with open("sample_auth_small.log") as file:    #open the file and read and store as "file"
        for line in file:                           #for every line in file
            line_count +=1                          #add 1 to line_count
            ip = ip_parser(line)                    #to find the ip in line, call the ip_parser function
            if ip:                                  #if there's an ip in the line
                unique_ips.add(ip)                  #add the ip to the set unique_ips

    sorted_ips = sorted(unique_ips)         #this converts the set into a sorted list

    print(f"Lines read: {line_count}")
    print(f"Unique ips: {len(unique_ips)}")
    print(f"First 10 ips: {sorted_ips[:10]}")

task1_2()           #run task1.2
