import logging
import sys
from src.worklist import Work_list
from flask import Flask, render_template

def main():
    logging.basicConfig(format="%(asctime)s; %(message)s", 
                        level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout),
                                                      logging.FileHandler('out.log')])
    # disable Flask logging - useful for monitoring localhost 
    flask_logger = logging.getLogger('werkzeug')
    flask_logger.setLevel(logging.CRITICAL)
    
    Workers = Work_list('./config.yml')
    for task in Workers.tasks:
        task.run()
    
    app = Flask(__name__)
    
    
    @app.route('/')
    def mainpage():
        # all important parameters from task, to be rendered
        # as table in jinja template
        html_table = [[x.last_run , x.url, x.keyword, x.contains, 
                       x.status_code, str(x.time_took)+'s']
                      for x in Workers.tasks]
        
        return render_template('main.html', table = html_table)
    
    # host keyword can be skipped if not using Docker
    # deafult port used by website - 5000
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    main()