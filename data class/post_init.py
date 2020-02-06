from dataclasses import dataclass

@dataclass
class User:
    """
        Já vem sobreescrito __init__ e __rept__
    """
        name:str
        age:int
        

        def __post_init__(self):
            self.fulldata = f'{self.name} + {self.age}'
        
