class IdempotencyStore:
    def __init__(self): self.results={}
    def run(self,key,fn):
        if key in self.results:
            return {"replayed":True,"result":self.results[key]}
        result=fn()
        self.results[key]=result
        return {"replayed":False,"result":result}
