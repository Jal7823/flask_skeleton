class Cars:
    def __init__(self,model:str,brand:str) -> str:
        self.model = model
        self.brand = brand
        self.is_start = False
        self.is_stop = False

    def start(self,status) :
        if status:
            self.is_start = True
            return self.is_start
    
    def stop(self,status) :
        if status :
            self.is_stop = True
            return self.is_stop

    def general_status(self):
        print( f'''
            The status of vehicle is:
            model: {self.model} 
            brand: {self.brand} 
            start: {self.is_start} 
            stop: {self.is_stop} 
        ''')