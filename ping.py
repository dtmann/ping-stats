import sys
import time
import statistics as s
import math
import time
GOOGLE_IP = '8.8.8.8'

try:
    from ping3 import ping, verbose_ping
    import matplotlib.pyplot as plt
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

def run_program():
    ping = ping_server()
    append_to_file(ping)

def run_program_loop():
    while True:
        ping = ping_server()
        append_to_file(ping)  
        time.sleep(1)

def show_graph():
    x, y = [], []
    f = open("data.txt", "r")
    while True:
        data = str(f.readline())
        if not data: 
            break
        d = data.strip().split(",")
        x.append(float(d[0]))
        y.append(float(d[1]))
    print(x, y)
    plt.plot(x, y)
    plt.show()


def main(argv):
    if argv[1] == "-p":
        print("Running main loop")
        run_program_loop()
    elif argv[1] == "-g":
        show_graph()    
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