import psutil
import json
import time
from datetime import datetime
from config import settings
time_stmp = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")

class snapshot:


    def monitor(self):
        print("SNAPSHOT:")
        print("CPU load             -", psutil.cpu_percent(interval=1), "%")
        print("Physical memory used -", psutil.disk_usage('/'))
        print("Virtual memory used  -", psutil.virtual_memory()[2], "%")
        print("IO information       -", psutil.net_io_counters())
        print("Network information  -", psutil.net_io_counters(pernic=True))

    def print(self):
        outpfile = settings['output']
        tinterval = settings['interval']
        tlength = settings['time']
        i = 0
        if outpfile == "json":
            data = {}
            for i in range(tlength):
                time_stmp = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                data['SNAPSHOT' + str(i)] = []
                data['SNAPSHOT' + str(i)].append({
                    '': time_stmp,
                    'CPU load': psutil.cpu_percent(interval=1),
                    'Physical memory used': psutil.disk_usage('/'),
                    'Virtual memory used': psutil.virtual_memory()[2],
                    'IO information': psutil.net_io_counters(),
                    'Network information': psutil.net_io_counters(pernic=True)
                })
                with open('data2.json', 'w') as outfile:
                    json.dump(data, outfile, indent=2)
                time.sleep(tinterval)
        elif outpfile == "txt":
            for i in range(tlength):
                print(i)
                time_stmp = datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S")
                with open('data2.txt', 'a+') as file:
                    file.write("'SNAPSHOT" + ":" + str(i + 1) + ":" + str(time_stmp) + ':' + '\n')
                    file.write("CPU load             -" + str(psutil.cpu_percent(interval=1)) + '\n')
                    file.write("Physical memory used -" + str(psutil.disk_usage('/')) + '\n')
                    file.write("Virtual memory used  -" + str(psutil.virtual_memory()[2]) + '\n')
                    file.write("IO information       -" + str(psutil.net_io_counters()) + '\n')
                    file.write("Network inform" + str(psutil.net_io_counters(pernic=True)) + '\n')
                time.sleep(tinterval)
        else:
            print("write txt or json in conf file ")
snp = snapshot()
snp.print()
