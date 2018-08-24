import os, re, win32api, psutil, time, wmi, requests, socket
from sys import platform

class SystemAnalysis:

    def system_architecture(self):
        #Returning system architecture
        try:
            if platform == "linux" or platform == "linux2":
                return "Linux"            
            elif platform == "darwin":
                return "OS X"            
            elif platform == "win32":
                return "Windows"            
            else:
                raise Exception                
        except Exception:
            pass
        return False

    def network_status(self):
        try:
            #Opening socket
            netSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            #Connecting to Google Public DNS recursive name servers on port 80
            netSocket.connect(("8.8.8.8.", 80))
            
            #Getting local IP through socketname
            ip_address = netSocket.getsockname()[0]
            
            #Closing socket
            netSocket.close()

            #Verifying IPV4 connectivity and DNS resolution
            requests.get("http://www.msftncsi.com", timeout=3)
            
            return ip_address
        
        except Exception:
            return False

    def cpu_activity(self):
        self.detailing = psutil.cpu_times()
        self.frequency = psutil.cpu_freq()
        self.usage = int(round(psutil.cpu_percent(), 1))
        if self.usage >= 90:
            return True
        else:
            return False

    def active_processes(self):
        process_names = [proc.name() for proc in psutil.process_iter()]
        return process_names

    def main(self):
        print(self.network_status())
        while True:
            if self.cpu_activity() == True:
                print("---CPU WARNING---")
                print("%d\n%s\n%s" % (self.usage, self.detailing, self.frequency))
            else:
                print("---SYSTEM STABLE---")
                print("%d\n%s\n%s\n" % (self.usage, self.detailing, self.frequency))
            time.sleep(2)
                  

if __name__ == "__main__":
    sysanl = SystemAnalysis()
    sysanl.main()
        
