"""Project 05: Tenant-Aware Data Layer."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.tenancy import same_tenant
def main(): print(same_tenant("t1","t2","member"),same_tenant("t1","t1","member"))

if __name__=='__main__': main()
