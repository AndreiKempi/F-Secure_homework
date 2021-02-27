from Configuration import *

import logging
import logging.config
import requests
import datetime


class Methods:

    def __init__(self):
        self.host = None
        self.response = None
        self.session = requests.Session()
        #creating name for the new log file
        self.logfile = log_file_name + '%s' % (datetime.datetime.now().strftime("%b_%d_%Y_%H-%M-%S") + '.log')

    #Initializing an HTTP session for a given URL and schema (http, https).
    def initialize_http_session(self, url, schema):
        try:
            self.host = schema + '://' + url
            logging.info('selected host: %s, schema: %s' % (url, schema))
        except:
            logging.error("Host name not created!")

    #Log configuration and creating new log file
    def log_file_configuration(self):
        try:
            logging.basicConfig(filename=self.logfile,
                                format=u'%(levelname)-8s [%(asctime)s]  %(message)s',
                                level=logging.INFO)
        except OSError:
            logging.error("error reading the file")
        except:
            logging.error("Log file configuration failed!")

    #Sending GET request to chosen host
    def send_get_request_and_get_response(self):
        try:
            response = self.session.get(self.host)
            logging.info('Sending GET request to %s' % response.url)
            self.response = response
        except requests.exceptions.ConnectionError:
            logging.error("Connection Error!")
        except requests.exceptions.HTTPError:
            logging.error("Invalid HTTP response!")
        except requests.exceptions.Timeout:
            logging.error("Time out!")
        except requests.exceptions.RequestException:
            logging.error("Bad request!")
        except:
            logging.error("Unexpected error in GET request!")
        else:
            logging.info("Request sent successfully!")

    #logging response info (such as status code and response time) into log file
    def log_response_info(self):
        try:
            status_code = self.response.status_code
            response_time = self.response.elapsed
            url = self.response.url
            logging.info('Status Code: %s' % status_code)
            logging.info('Response Time: %s' % response_time)
        except:
            logging.error("Response not correct!")

    #Page verifying using required page object and logging
    def send_request_verify_page_and_log(self, requirement):
        self.send_get_request_and_get_response()
        try:
            if requirement in self.response.text:
                logging.info('Page verified successfully')
                self.log_response_info()
            else:
                logging.info('!!! Page not verified')
                self.log_response_info()
        except ValueError:
            logging.error("Data type incorrect!")