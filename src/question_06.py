if __name__ == "__main__":
    sentences = []

    while True:
        sentence = input("Digite uma frase: ")

        if sentence.lower() == "sair":
            break

        sentences.append(sentence)

    i_occurrences = sum(["eu" in i.lower() for i in sentences])

    print(f"A palavra 'eu' apareceu em {i_occurrences} frases.")
