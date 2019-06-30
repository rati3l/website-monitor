import requests
import threading
import logging
import time

class Task:
    def __init__(self, url, frequency, keyword):
        self.url = url
        self.frequency = frequency
        self.keyword = keyword
    
    def run(self):
        task = threading.Thread(target=self.worker)
        task.start()

    def worker(self):
        while True:
            self.timer_start()
            try:
                response = requests.get(self.url)
            except requests.exceptions.ConnectionError:
                self.contains = None
                self.status_code = 'website unreachable'
            else:
                self.status_code = response.status_code
                if self.keyword in response.text:
                    self.contains = True
                else:
                    self.contains = False
            self.timer_stop()
            logging_vars =  [self.url, self.keyword, self.contains,
                         self.status_code, self.time_took]
            logging_vars = map(lambda x: str(x), logging_vars)
            logging.info('; '.join(logging_vars))
            time.sleep(self.frequency)

    def timer_start(self):
        self.start_time = time.time()
        self.last_run = time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.gmtime(self.start_time))
    
    def timer_stop(self):
        self.time_took = round(time.time() - self.start_time,3)
        