

def weightForItem(item):
    if item.startswith("[Level 1]"):
        return 800
    
    if item.startswith("[Level 2]"):
        return 800

    if item.startswith("[Level 3]"):
        return 900
    
    if item.startswith("[Level 4]"):
        return 1000
    
    if item.startswith("[Level 5]"):
        return 1000

class ExchangeOptimizerState:

    def __init__(exchanges):
        self.ship_lt = 10900
        self.exchanges = exchanges
        self.portfolio = []
        self.taken_routes = []

    def mutate():

        # value / distance
        # assign value by rarity, boost if item is needed

    

    


        
