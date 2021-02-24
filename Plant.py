class Plant:
    def __init__(self, name, season, temperature, ph):
        self.name=name
        self.season=season
        self.temperature=temperature
        self.ph=ph
    # methods
    def checkTemp(self):
        return self.ph*self.temperature
    def average(self,Plants):
        s=0
        for plant in Plants:
            s += plant.temperature
        return s/len(Plants)