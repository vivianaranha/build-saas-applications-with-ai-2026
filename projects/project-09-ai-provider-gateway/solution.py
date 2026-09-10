"""Project 09: AI Provider Gateway."""
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]/"src"))
from ai_saas.provider import MockProvider
def main(): print(MockProvider().generate("summarize this ticket"))

if __name__=='__main__': main()
