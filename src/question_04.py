VECTOR_SIZE = 2

if __name__ == "__main__":
    values = []
    while len(values) < VECTOR_SIZE + 1:
        value = input("Digite um número inteiro para compor o vetor:")

        try:
            value = int(value)
        except ValueError:
            print("O valor deve ser um número inteiro!")
        else:
            values.append(value)

    occurrences = values.count(0)
    print(f"A quantidade de ocorrências de 0 no vetor é igual a: {occurrences}")
