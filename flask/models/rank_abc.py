from abc import ABC, abstractmethod

class RankInterface(ABC):
    def __init__(self, data):
        self.data = data  
    @abstractmethod
    def rank_data(self):
        pass

