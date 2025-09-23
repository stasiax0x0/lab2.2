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

#task3      TOP 5 ATTACKERS IPS AND EXPORTS
#Produce a list of top 5 IPs by failed attempts and print them nicely:
#Format: Rank. IP — Count.
#Write the full counts dictionary to failed_counts.txt with headers ip,failed_count.
#Run your script on the larger mixed_logs_5000.log and time how long it takes. Print the elapsed time

import time

def top_n(counts, n=5):
    #return top n items from a dictionary by value
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n] 

def task3():
    start = time.time()

    from collections import defaultdict
    counts = defaultdict(int)           #create a dictionary to keep track of ips

    #count failed attempts (task2)
    with open("sample_auth_small.log") as file:
        for line in file:
            if "Failed password" in line or "Invalid user" in line:
                ip = ip_parser(line)        #extract ip
                if ip:
                    counts[ip] +=1

    #get top 5 attackers
    top_attackers = top_n(counts, 5)

    print("Top 5 attacker ips:")        #print top 5
    for rank, (ip, count) in enumerate(top_attackers, 1):
        print(f"{rank}. {ip} - {count}")

    #export to file failed_counts.txt
    with open("failed_counts.txt", "w")as file:
        file.write("ip,failed_count\n")        #write hearder
        for ip, count in counts.items():
            file.write(f"{ip},{count}\n")
    
    end = time.time()
    print("Elapsed:", end-start, "seconds")

task3()     #run task3


