from datetime import date

STAGES = ["novo"]  # por enquanto só marcamos como "novo" nessa aula

def model_lead(name, company, email):
    """Cria um lead como dicionário simples."""
    return {
        "name": name,
        "company": company,
        "email": email,
        "stage": "novo",
        "created": date.today().isoformat(),
    }
