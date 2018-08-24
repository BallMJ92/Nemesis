import requests, time
from stem import Signal
from stem.control import Controller
import socks

class Boa:    
    
    def IP_alternate(self):
        # Tor running from local port 9151
        with Controller.from_port(port=9151) as controller:
            controller.authenticate()
            # Defining proxy port on local machine
            socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9150)
            while True:
                try:
                    # Getting current IP address from requests through url
                    current_ip = requests.get(url='http://httpbin.org/ip')
                    print(current_ip.text)
                    controller.signal(Signal.NEWNYM)
                    # Wait until Tor controller sets a new IP address
                    time.sleep(controller.get_newnym_wait())
                except:
                    print("Waiting for controller to assign new IP address..")
                    time.sleep(20)
                    continue

    def main(self):
        self.IP_alternate()

if __name__ == "__main__":
    mainFunc = Boa()
    mainFunc.main()
