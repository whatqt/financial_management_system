class ValidateType:
    def get_validate_purpose(self):
        return ["накопление", "распределение"]
    
    def get_validate_married(self):
        return ["женат", "не женат"]
    
    def get_validate_flat_or_house(self):
        return ["квартира", "дом"]
    
    def methods(self):
        return {
            "purpose": self.get_validate_purpose, 
            "family": self.get_validate_married,
            "flat_or_house": self.get_validate_flat_or_house
        }
        
