class Computer:
    description: str
    processor: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, description: str, 
                processor: str, 
                hard_drive_capacity: int, 
                memory: int, 
                operating_system: str, 
                year_made: int, 
                price: int):
        self.description = description
        self.processor = processor
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price