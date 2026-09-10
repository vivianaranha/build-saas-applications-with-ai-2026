"""Project 10: RAG Knowledge Workspace."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
import json
from pathlib import Path
from ai_saas.retrieval import retrieve
def main():
 docs=json.loads((Path(__file__).resolve().parents[2]/"data/knowledge.json").read_text());print(retrieve("refund policy",docs,tenant="t1"))

if __name__=='__main__': main()
