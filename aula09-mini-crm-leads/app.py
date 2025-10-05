# =====================================
# PARTE 2
# =====================================
from stages import new_lead

#parte 3 import
import repo

def add_flow():
    name = input("Nome: ").strip()
    company = input("Empresa: ").strip()
    email = input("E-mail: ").strip()
    if not name or not email or "@" not in email:
        print("Nome e e-mail válido são obrigatórios.")
        return
    # print((name,company,email))
    print(new_lead(name, company, email)) # AQUI CRIA O STAGES.PY

    # =====================================
    # PARTE 3 - criar repo
    # =====================================
    repo.add_lead(new_lead(name, company, email))

    print("✔ Lead adicionado!")

# =====================================
# PARTE 4 - listar
# =====================================
def list_flow():
    leads = repo.list_leads()
    if not leads:
        print("Nenhum lead ainda.")
        return
    print("\n# | Nome                 | Empresa            | E-mail")
    print("--+----------------------+-------------------+-----------------------")
    for i, l in enumerate(leads):
        print(f"{i:02d}| {l['name']:<20} | {l['company']:<17} | {l['email']:<21}")

# =====================================
# PARTE 1
# =====================================
def main():
    while True:
        print_menu()
        op = input("Escolha: ").strip()
        if op == "1":
            add_flow()
        elif op == "2":
            list_flow()
        elif op == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

def print_menu():
    print("\nMini CRM de Leads — Aula 1 (Adicionar/Listar)")
    print("[1] Adicionar lead")
    print("[2] Listar leads")
    print("[0] Sair")

# def add_flow():
#     print("✔ Lead adicionado!")

# def list_flow():
#     print("listar")

if __name__ == "__main__":
    main()


