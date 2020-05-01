import sys
import time
import statistics as s
import math
import time
GOOGLE_IP = '8.8.8.8'

try:
    from ping3 import ping, verbose_ping
except:
    print("Please install dependencies: ping3")
    exit()

def ping_server():
    pings = []
    try:
        for i in range(0,4):
            pings.append(ping(GOOGLE_IP))
            #i = i + 1
        average_ping = s.mean(pings)
    except:
        print("An error has occured")
    average_rounded = round(average_ping*1000,2)
    print(average_rounded)
    return average_rounded

def append_to_file(ping):
    current_unix_time = str(math.ceil(int(time.time())))
    try:
        f = open("data.txt", "a")
        p = str(ping)
        f.write(current_unix_time + "," + p + "\n")
        f.close()
    except:
        print("Error saving file")

def main(argv):
    if argv[1] == "-p":
        ping = ping_server()
        append_to_file(ping)
    elif argv[1] != "-p":
        print("Invalid command")

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        main(sys.argv)
    elif(len(sys.argv) == 1):
        print("Please provide an arguement")
        exit()
    if(len(sys.argv) > 2):
        print("Too many arguments")
        exit()