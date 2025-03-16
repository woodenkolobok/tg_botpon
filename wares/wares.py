from aiogram.types import FSInputFile

import json
import os
class Ware:
    def __init__(self, name: str, 
                 price: int, description: str, 
                 imageURL: str, id: int):
        self.name = name
        self.price = price
        self.description = description
        self.imageURL = imageURL
        
        img_folder_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img')
        image_path = os.path.join(img_folder_path, self.imageURL)
        self.inputImage = FSInputFile(image_path)

        self.id = id



    @classmethod
    def from_dict(cls, data: dict, id):
        return Ware(name=data['name'], 
                    price=data['price'], 
                    description=data['description'],
                    imageURL=data['imageURL'],
                    id=id)
    
    def get_ware_detail(self):
        return f"{self.name}\nЦена: {self.price} руб.\n{self.description}\n"
    
    @classmethod
    def get_ware_by_id(cls, wares: list, id: int):
        for ware in wares:
            if ware.id == id:
                return ware
    

with open('wares.json', 'r', encoding='utf-8') as f:
    wares = json.load(f)
    wares = [Ware.from_dict(ware, id=index) for index, ware in enumerate(wares)]