from pathlib import Path
import json, csv # pt1

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

# -----------------------------
# PARTE 0
# -----------------------------
def read_leads():
    return _load()

def create_lead(lead_dict):
    leads = _load()
    leads.append(lead_dict)
    _save(leads)

# -----------------------------
# PARTE 4.1 - criar
# -----------------------------
def export_csv(path=None):
    """Exporta os leads para CSV. Retorna o caminho do arquivo."""
    path = Path(path) if path else (DATA_DIR / "leads.csv")
    leads = _load()
    try:
        with path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=["name","company","email","stage","created"])
            w.writeheader()
            for row in leads:
                w.writerow(row)
        return path
    except PermissionError:
        # caso o arquivo esteja aberto em outro programa, por exemplo
        return None
