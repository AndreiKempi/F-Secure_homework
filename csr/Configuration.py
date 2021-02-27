# Transfer protocol type
schema = 'http'
# List of url addresses
urls = ['www.google.com', 'twitter.com', 'f-secure.com']
# Required page object which page (response body) should contain
requirements = ['Google</title>', 'title="Twitter"', 'F-Secure</title>']
# Log file location and name template
log_file_name = '../logs/SiteMonitoringLog_'
# Repeating time period (in sec)
delay_time = 5

