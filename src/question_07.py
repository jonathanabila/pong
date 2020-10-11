def main():
    elements = []

    def _include():
        value = input("Digite o valor a ser inserido na lista: ")
        elements.append(value)

    def _show():
        print(f"Conteúdo atual da lista: {elements}")
        pass

    def _remove():
        value = input("Digite o valor a ser removido da lista: ")

        if value in elements:
            elements.remove(value)
            print("Elemento removido da lista!")
        else:
            print("O elemento não está presente na lista!")

    def _remove_all():
        del elements[:]
        print("Elementos removidos!")

    options = {"a": _show, "b": _include, "c": _remove, "d": _remove_all}
    while True:
        print()
        print("Selecione a opção desejada: ")
        print(
            "a. Mostrar a lista. \nb. Incluir elemento. \nc. Remover elemento. "
            "\nd. Apagar todos os elementos da lista."
        )
        print()
        option = input("Digite a opção desejada: ")

        if option.lower() not in options.keys():
            print("Opção inválida!")
            continue

        options[option]()


if __name__ == "__main__":
    main()
