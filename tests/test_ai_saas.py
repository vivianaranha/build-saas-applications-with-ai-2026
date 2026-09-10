import sys,unittest
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]/"src"))
from ai_saas.tenancy import same_tenant,can
from ai_saas.plans import entitled,limit
from ai_saas.usage import UsageMeter
from ai_saas.idempotency import IdempotencyStore
from ai_saas.provider import MockProvider
from ai_saas.retrieval import retrieve
from ai_saas.agents import run_bounded_agent
from ai_saas.metrics import conversion,retention,ai_cost_per_active_user

class T(unittest.TestCase):
 def test_tenant(self): self.assertFalse(same_tenant("t1","t2","member"));self.assertTrue(same_tenant("t1","t2","platform_admin"))
 def test_role(self): self.assertTrue(can("admin","manage"));self.assertFalse(can("viewer","delete"))
 def test_entitlements(self): self.assertTrue(entitled("pro","agents"));self.assertFalse(entitled("starter","agents"));self.assertEqual(limit("starter","seats"),3)
 def test_usage(self):
  m=UsageMeter();self.assertEqual(m.add("t1","ai"),1);self.assertEqual(m.add("t1","ai",2),3);self.assertEqual(m.get("t1","ai"),3)
 def test_idempotency(self):
  s=IdempotencyStore();a=s.run("k",lambda:1);b=s.run("k",lambda:2);self.assertFalse(a["replayed"]);self.assertTrue(b["replayed"]);self.assertEqual(b["result"],1)
 def test_provider(self): self.assertIn("text",MockProvider().generate("hello"))
 def test_retrieval_isolation(self):
  docs=[{"tenant":"a","text":"refund policy"},{"tenant":"b","text":"refund policy secret"}]
  out=retrieve("refund",docs,tenant="a");self.assertTrue(out);self.assertTrue(all(x["tenant"]=="a" for x in out))
 def test_agent(self):
  self.assertEqual(run_bounded_agent("delete",{"lookup"})["status"],"blocked")
  self.assertEqual(run_bounded_agent("refund",{"refund"},True,False)["status"],"approval_required")
 def test_metrics(self):
  self.assertEqual(conversion(1,4),.25);self.assertEqual(retention(3,4),.75);self.assertEqual(ai_cost_per_active_user(10,5),2)
if __name__=="__main__": unittest.main()
