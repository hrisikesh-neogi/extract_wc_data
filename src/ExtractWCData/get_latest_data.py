from ._scrape_data import Scrape

class GetData(Scrape):
    def __init__(self):
        super().__init__()
    
    def get_data(self):
        df = self.scrape()
        return df
