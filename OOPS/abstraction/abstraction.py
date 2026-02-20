from abc import ABC,abstractmethod

class feature(ABC):
    @abstractmethod
    def login(self):
        pass
    
    @abstractmethod
    def logout(self):
        pass
    
    def checkout(self):
        pass

class web(feature):
    def login(self):
        print("login to web")
        
    def logout(self):
        print("logout from web")    
        
W=web()
W.login()
W.logout()          