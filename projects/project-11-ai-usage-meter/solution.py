"""Project 11: AI Usage Meter."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.usage import UsageMeter
def main():
 m=UsageMeter();print(m.add("t1","ai_action"),m.add("t1","ai_action"),m.get("t1","ai_action"))

if __name__=='__main__': main()
