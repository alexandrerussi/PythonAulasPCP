def max_grade_per_student(pairs):
    result = {}
    for name, grade in pairs:
        if name not in result or grade > result[name]:
            result[name] = grade
    return result

dados = [('Ana',7.0), ('João',6.5), ('Ana',8.5), ('João',7.2), ('Mia',9.0)]
print(max_grade_per_student(dados))