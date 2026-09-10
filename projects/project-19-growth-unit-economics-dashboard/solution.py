"""Project 19: Growth & Unit Economics Dashboard."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.metrics import conversion,retention,ai_cost_per_active_user
def main(): print(conversion(120,1000),retention(300,500),ai_cost_per_active_user(250,500))

if __name__=='__main__': main()
