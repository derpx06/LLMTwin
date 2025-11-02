from abc import ABC, abstractmethod

class DeplymentStrtegy(ABC):
    @abstractmethod
    def deploy(self,model,endpoint_name:str,endpoint_config_name:str)->None:
        pass

class Inference(ABC):
    def __init__(self):
        self.model = None

    @abstractmethod
    def set_payload(self, inputs, parameters=None):
        pass

    @abstractmethod
    def inference(self):
        pass