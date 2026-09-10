"""Project 07: RBAC & Tenant Isolation API."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.tenancy import can,same_tenant
def main(): print(can("admin","delete"),same_tenant("t1","t2","admin"))

if __name__=='__main__': main()
