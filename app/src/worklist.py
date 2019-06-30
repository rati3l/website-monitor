import yaml
from src.task import Task



class Work_list:
    """ loads yaml config file and creates list of workers for each main key
        in yaml """
    def __init__(self, path):
        self.dict = self.get_config(path)
        for item in self.dict:
            self.dict[item]['frequency'] = self.convert_to_seconds(self.dict[item]['frequency'])
        self.tasks = []
        self.create_task_list()
        
    def get_config(self, path):
        with open(path) as f:
            return(yaml.load(f, Loader=yaml.FullLoader))
    
    def create_task_list(self):
        for item in self.dict:
            self.tasks.append(Task(**self.dict[item]))
    
    def convert_to_seconds(self, time):
        # to unify different time units
        helper = lambda: int(''.join(x for x in time if x.isdigit()))
        time_chars = {'s': 1, 'm': 60, 'h': 3600}
        
        for char in time_chars:
            if char in time:
                return helper() * time_chars[char]
        