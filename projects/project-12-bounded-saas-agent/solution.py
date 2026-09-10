"""Project 12: Bounded SaaS Agent."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.agents import run_bounded_agent
def main(): print(run_bounded_agent("refund",{"lookup","refund"},True,False));print(run_bounded_agent("refund",{"lookup","refund"},True,True))

if __name__=='__main__': main()
