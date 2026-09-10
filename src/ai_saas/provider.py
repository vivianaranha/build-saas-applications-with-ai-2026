class AIProvider:
    def generate(self,prompt):
        raise NotImplementedError

class MockProvider(AIProvider):
    def generate(self,prompt):
        return {"text":f"Mock AI response for: {prompt[:80]}","model":"mock-local"}
