"""Project 13: Async Automation Worker."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.idempotency import IdempotencyStore
def main():
 s=IdempotencyStore();print(s.run("job-1",lambda:{"status":"queued"}));print(s.run("job-1",lambda:{"status":"duplicate"}))

if __name__=='__main__': main()
