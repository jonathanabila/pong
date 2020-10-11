if __name__ == "__main__":
    values = []
    while len(values) < 5:
        value = input("Digite um número inteiro para compor o vetor:")

        try:
            value = int(value)
        except ValueError:
            print("O valor deve ser um número inteiro!")
        else:
            values.append(value)

    print(f"O vetor é: {values}")
