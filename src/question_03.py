AMOUNT_OF_WORDS = 10

if __name__ == "__main__":
    values = []
    while len(values) < AMOUNT_OF_WORDS + 1:
        value = input("Digite uma palavra: ")
        values.append(value)

    values = [i[::-1] for i in values]
    print(f"O vetor invertido é: {values}")
