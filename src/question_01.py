def main():
    my_list = []

    for i in range(6):
        my_list.append(i)

    print(f"Estado atual da minha lista: {my_list}")

    if 3 in my_list:
        my_list.pop(3)
    if 6 in my_list:
        my_list.pop(6)

    print(f"Após remover os elementos: {my_list}")

    print(f"Tamanho da minha lista: {len(my_list)}")

    my_list[-1] = 6
    print(f"Minha lista após modificar o último valor para 6: {my_list}")


if __name__ == "__main__":
    main()
