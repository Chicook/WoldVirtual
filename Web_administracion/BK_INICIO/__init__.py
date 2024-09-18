# BK_INICIO/__init__.py

import os
import subprocess

def mostrar_menu():
    print("Menú de Secciones:")
        for i in range(1, 6):
                print(f"Sección {i}")

                def iniciar_seccion(seccion):
                    seccion_path = f"secciones/seccion_{seccion}"
                        lenguajes = ["python", "angular", "csharp", "cpp", "react", "typescript", "javascript", "html", "css"]
                            
                                for lenguaje in lenguajes:
                                        path = os.path.join(seccion_path, lenguaje)
                                                if lenguaje == "python":
                                                            subprocess.run(["python", os.path.join(path, "app.py")])
                                                                    elif lenguaje == "angular":
                                                                                subprocess.run(["ng", "serve"], cwd=path)
                                                                                        elif lenguaje == "csharp":
                                                                                                    subprocess.run(["dotnet", "run"], cwd=path)
                                                                                                            elif lenguaje == "cpp":
                                                                                                                        subprocess.run(["g++", os.path.join(path, "main.cpp"), "-o", "main"], cwd=path)
                                                                                                                                    subprocess.run(["./main"], cwd=path)
                                                                                                                                            elif lenguaje == "react":
                                                                                                                                                        subprocess.run(["npm", "start"], cwd=path)
                                                                                                                                                                elif lenguaje == "typescript":
                                                                                                                                                                            subprocess.run(["tsc", os.path.join(path, "main.ts")], cwd=path)
                                                                                                                                                                                    elif lenguaje == "javascript":
                                                                                                                                                                                                subprocess.run(["node", os.path.join(path, "main.js")], cwd=path)
                                                                                                                                                                                                        elif lenguaje == "html":
                                                                                                                                                                                                                    print(f"Abre {os.path.join(path, 'index.html')} en tu navegador.")
                                                                                                                                                                                                                            elif lenguaje == "css":
                                                                                                                                                                                                                                        print(f"Abre {os.path.join(path, 'styles.css')} en tu navegador.")

                                                                                                                                                                                                                                        if __name__ == "__main__":
                                                                                                                                                                                                                                            mostrar_menu()
                                                                                                                                                                                                                                                seccion = input("Selecciona una sección (1-5): ")
                                                                                                                                                                                                                                                    iniciar_seccion(seccion)
                                                                                                                                                                                                                                            