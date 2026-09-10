"""Project 08: Plans & Entitlements Engine."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.plans import entitled,limit
def main(): print(entitled("pro","agents"),limit("starter","ai_actions"))

if __name__=='__main__': main()
