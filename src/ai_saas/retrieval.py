import math,re
def _tokens(text): return set(re.findall(r"[a-z0-9]+",text.lower()))
def score(query,text):
    q=_tokens(query); t=_tokens(text)
    if not q or not t: return 0.0
    return len(q&t)/math.sqrt(len(q)*len(t))
def retrieve(query,docs,k=3,tenant=None):
    filtered=[d for d in docs if tenant is None or d.get("tenant")==tenant]
    return sorted(filtered,key=lambda d:score(query,d.get("text","")),reverse=True)[:k]
