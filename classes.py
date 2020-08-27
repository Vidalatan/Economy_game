class Player:
  #intented to hold all of the player's resources and products
    def __init__(self,name,password):
        self.name = name
        self.password = password
        self.resources = []
        self.products = []
    
    def __str__(self):
        print(self.name+"|"+self.password+"|"+",".join(self.resources)+"|"+",".join(self.products))


class Product:
    def __init__(self,name,resources):
      self.name = name
      self.resources = resources

    def __str__(self):
      print(self.name+"|"+self.resources)
