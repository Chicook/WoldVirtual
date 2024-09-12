from prb2 import explain_prb2
from prb3 import explain_prb3
from prb4 import explain_prb4
from prb5 import explain_prb5

def main():
    while True:
        print("Menú Principal")
        print("1. Sección prb2")
        print("2. Sección prb3")
        print("3. Sección prb4")
        print("4. Sección prb5")
        print("5. Validar Blockchain")
        print("6. Salir")
        choice = input("Seleccione una opción: ")

        if choice == '1':
            explain_prb2()
        elif choice == '2':
            explain_prb3()
        elif choice == '3':
            explain_prb4()
        elif choice == '4':
            explain_prb5()
        elif choice == '5':
            validate_blockchain()
        elif choice == '6':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
