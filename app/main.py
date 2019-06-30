import logging
from src.worklist import Work_list
from flask import Flask, render_template

def main():
    logging.basicConfig(format="%(asctime)s; %(message)s", 
                        filename='wynik.log', level=logging.INFO)
    logging.info('Main loop')
    
    Workers = Work_list('./config.yml')
    for task in Workers.tasks:
        task.run()
    
    app = Flask(__name__)
    
    @app.route('/')
    def mainpage():
        html_table = [[x.last_run , x.url, x.keyword, x.contains, 
                       x.status_code, str(x.time_took)+'s']
                      for x in Workers.tasks]
        
        return render_template('main.html', table = html_table)

    app.run()

if __name__ =='__main__':
    main()