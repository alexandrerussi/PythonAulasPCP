from stages import model_lead
import repo

def add_leads():
    name = input("Nome: ").strip()
    company = input("Empresa: ").strip()
    email = input("E-mail: ").strip()
    if not name or not email or "@" not in email:
        print("Nome e e-mail válido são obrigatórios.")
        return

    repo.create_lead(model_lead(name, company, email))

    print("✔ Lead adicionado!")

# -----------------------------
# PARTE 0
# -----------------------------
def list_leads():
    leads = repo.read_leads()
    if not leads:
        print("Nenhum lead ainda.")
        return
    print("\n# | Nome                 | Empresa            | E-mail")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in enumerate(leads):
        print(f"{i:02d}| {l['name']:<20} | {l['company']:<17} | {l['email']:<21}")

# -----------------------------
# PARTE 3
# -----------------------------
def search_flow():
    q = input("Buscar por: ").strip().lower()
    if not q:
        print("Consulta vazia.")
        return
    leads = repo.read_leads()
    results = []
    for i, l in enumerate(leads):
        blob = f"{l['name']} {l['company']} {l['email']}".lower()
        if q in blob:
            results.append((i, l))
    if not results:
        print("Nada encontrado.")
        return
    print("\n# | Nome                 | Empresa            | E-mail")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in results:
        print(f"{i:02d}| {l['name']:<20} | {l['company']:<17} | {l['email']:<21}")

# -----------------------------
# PARTE 4 -- criar vazio e dps exportar da função
# -----------------------------
def export_leads():
    path = repo.export_csv()
    if path is None:
        print("Não consegui escrever o CSV. Feche o arquivo se estiver aberto e tente novamente.")
    else:
        print(f"✔ Exportado para: {path}")

# -----------------------------
# PARTE 2 - criar search_flow primeiro, dps export_leads
# -----------------------------
def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            add_leads()
        elif op == "2":
            list_leads()
        elif op == "3":
            search_flow()      # <-- novo
        elif op == "4":
            export_leads()      # <-- novo
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

# -----------------------------
# PARTE 1 -- colocar buscar e csv
# -----------------------------
def print_menu():
    print("\nMini CRM de Leads — Aula 2 (Adicionar/Listar/Buscar/CSV)")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[3] Buscar (nome/empresa/e-mail)")
    print("[4] Exportar CSV")
    print("[0] Sair")


if __name__ == "__main__":
    main()
