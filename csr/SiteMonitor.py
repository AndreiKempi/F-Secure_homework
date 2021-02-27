from Methods import *
import time
from inputimeout import inputimeout, TimeoutOccurred


class SiteMonitor:

    def __init__(self):
        self.methods = Methods()
        self.switch = 'Again'

    def main(self):

        #configure log file
        self.methods.log_file_configuration()
        switch = self.switch

        #monitoring continue untill operaton inputs 'Stop' or 's'
        while switch not in ["Stop", "STOP", "stop", "S", "s"]:
            counter = 0
            for url in urls:
                print("Initializing new session")
                #initialize new session
                self.methods.initialize_http_session(url, schema)
                #send GET request->get response->verify that page contains required element->log
                self.methods.send_request_verify_page_and_log(requirements[counter])
                time.sleep(delay_time)
                counter += 1

            # input with time out
            # if nothing is inputed during 10 sec monitoring will start again
            try:
                switch = inputimeout(prompt='Monitoring complete! \n'
                                            'After 10 seconds process will be restarted \n'
                                            'To stop monitoring please text "Stop":',
                                     timeout=10)
            except TimeoutOccurred:
                switch = self.switch


if __name__ == '__main__':
    site_monitor = SiteMonitor()
    site_monitor.main()
