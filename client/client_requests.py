from typing import List, Any, Tuple
import socket
from config import app_config

def data_handler(data: List[Any]) -> str:
    output = ""
    
    for index in data:
        output += str(index)
        output += "_"
        
    return data

class Client:
    def __init__(self, IP: str, port: int) -> None:
        self.server = socket.socket()
        self.IP = IP
        self.port = port
        
    def send_message(self, message_data: Tuple[Any], type_message: str) -> None | str:
        try:
            self.server.connect((self.IP, 77))
        except:
            return "connect_error"
        
        list_data = []
        
        for index in message_data:
            list_data.append(message_data[index])
            
        if type_message == "text":
            self.server.send((data_handler(data = list_data) + "SEND-MESSAGE").encode())
    
    def connect_to_server(self, user_data: List[Any] = None) -> None | str:
        try:
            self.server.connect((self.IP, self.port))
        except:
            return "connect_error"
        
        self.server.send((data_handler(data = user_data) + "CR-ACCOUNT").encode()) #nick_id
    
if __name__ == "__main__":
    client = Client(app_config["IP"], app_config["Port"])
    client.connect_to_server(["user", "f14d1rf2152fqw", "q2wr2424wwrwrw", "mail@gmail.com"])
        
    
    
