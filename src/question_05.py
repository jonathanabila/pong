if __name__ == "__main__":
    students = []

    while True:
        name = input("Digite o nome do aluno: ")

        if name.lower() == "sair":
            break

        height = input("Digite a altura do aluno: ")

        try:
            height = float(height)
        except ValueError:
            print("A altura deve ser um número real!")
        else:
            students.append((name, height))

    average_height = sum([i[1] for i in students]) / len(students)

    for student in students:
        if student[1] > average_height:
            print(f"O aluno {student[0]} é mais alto que a média dos demais alunos.")
