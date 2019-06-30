import logging
import yaml
from src.worklist import Work_list
import time


def main():
    logging.basicConfig(format="%(asctime)s; %(message)s", 
                        filename='wynik.log', level=logging.INFO)
    logging.info('Main loop')
    
    x = Work_list('./config.yml')
    for task in x.tasks:
        task.run()
    
    
    
    # x = Task('http://www.google.pl', 15, 'search')
    # x.run()
    
    # while True:
    #     time.sleep(5)
    #     print(x.url, x.keyword, x.contains, x.status_code, x.time_took)

if __name__ =='__main__':
    main()