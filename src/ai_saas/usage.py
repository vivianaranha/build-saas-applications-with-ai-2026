class UsageMeter:
    def __init__(self): self.counts={}
    def add(self,tenant,event,amount=1):
        key=(tenant,event)
        self.counts[key]=self.counts.get(key,0)+amount
        return self.counts[key]
    def get(self,tenant,event):
        return self.counts.get((tenant,event),0)
