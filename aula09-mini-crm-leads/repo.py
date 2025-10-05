# =====================================
# PARTE 3 - criar repo
# =====================================

from pathlib import Path
import json

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(exist_ok=True)
DB_PATH = DATA_DIR / "leads.json"

def _load():
    if not DB_PATH.exists():
        return []
    try:
        return json.loads(DB_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        # se corromper, começa vazio (decisão didática para agora)
        return []

def _save(leads):
    DB_PATH.write_text(json.dumps(leads, ensure_ascii=False, indent=2), encoding="utf-8")

def list_leads():
    return _load()

def add_lead(lead_dict):
    leads = _load()
    leads.append(lead_dict)
    _save(leads)
