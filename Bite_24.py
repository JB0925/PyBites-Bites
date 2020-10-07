from abc import ABC, abstractmethod


class Challenge(ABC):
    def __init__(self, number, title):
        super().__init__()
        self.number = number
        self.title = title
    
    @abstractmethod
    def verify(self):
        return NotImplemented
    
    @abstractmethod
    def pretty_title(self):
        return NotImplemented

class BlogChallenge(Challenge):
    def __init__(self, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs
    
    def verify(self):
        return super().verify()

class BiteChallenge(Challenge):
    def __init__(self, result):
        super().__init__(number, title)
        self.result = result
    
    def pretty_title(self):
        return super().pretty_title()
    
    
