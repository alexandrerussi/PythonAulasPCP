def domain_count(emails):
    d = {}
    for e in emails:
        user, dom = e.split('@')
        d[dom] = d.get(dom, 0) + 1
    return d

emails = [  'ana@fiap.com.br','joao@fiap.com.br','maria@gmail.com','ana@fiap.com.br']
print(domain_count(emails))