class araba():
    def __init__(self,marka,model):
        
        self.marka = marka
        self.model = model

    def __str__(self):
        return "Araba oluşturuldu"
        
honda = araba("Honda","Civic")
print(honda)