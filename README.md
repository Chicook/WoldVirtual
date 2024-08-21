# Wold Virtual

## Descripción general

Wold Virtual es un proyecto de blockchain con múltiples funcionalidades. Incluye una criptomoneda llamada WoldcoinVirtual (WLCV) con un suministro máximo de 30,000,000.000 WLCV. El proyecto tiene como objetivo proporcionar una plataforma segura y eficiente para diversas aplicaciones basadas en blockchain.

## Características

- **Criptomoneda**: WoldcoinVirtual (WLCV) con un suministro máximo de 30,000,000.000 WLCV.
- **Comisiones**: Las comisiones variarán según la red conectada (por ejemplo, Ethereum, Binance Smart Chain, Polygon, etc.). Dentro del metaverso, se asignará una comisión de 0.001 WLCV al fondo de garantía de recompensas.
- **Formato de saldo**: El formato de saldo para el metaverso es "0,000".
- **Protocolo de recompensas**: Asegura que las recompensas nunca caigan por debajo del 50%.
- **Prueba de trabajo**: Una segunda capa de seguridad con prueba de trabajo utilizando tarjetas gráficas para renderizado en tiempo real y una mejor experiencia de usuario.

## Estructura del directorio

El repositorio está organizado en los siguientes directorios:

- **contracts**: Contiene contratos inteligentes en Solidity.
  - `Blokchain.sol`
  - `Blokchain2.sol`
- **scripts**: Contiene scripts en Python para varias funcionalidades.
  - `blockchain.py`
  - `BSMTV.py`
  - `BSnts.py`
- **csharp**: Contiene proyectos en C#.
  - `Editorvirtual.cs`

## Configuración y ejecución del código

### Requisitos previos

- Python 3.x
- Node.js
- Compilador de Solidity
- Web3.js
- Flask

### Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/Chicook/WoldVirtual.git
   cd WoldVirtual
   ```

2. Instala las dependencias de Python:
   ```bash
   pip install -r requirements.txt
   ```

3. Instala las dependencias de Node.js:
   ```bash
   npm install
   ```

### Ejecución del código

1. Inicia el servidor Flask:
   ```bash
   python scripts/blockchain.py
   ```

2. Despliega los contratos inteligentes:
   ```bash
   npx hardhat run scripts/deploy.js
   ```

3. Inicia el proyecto en C#:
   Abre el archivo `csharp/Editorvirtual.cs` en tu IDE de C# preferido y ejecuta el proyecto.

## Contribuyendo

Damos la bienvenida a contribuciones para mejorar Wold Virtual. Por favor, sigue estos pasos para contribuir:

1. Clona el repositorio.
2. Crea una nueva rama para tu característica o corrección de errores.
3. Haz commit de tus cambios y empuja la rama a tu fork.
4. Crea una pull request con una descripción detallada de tus cambios.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Contacto

Para cualquier pregunta o consulta, por favor contáctanos en [jaldvox@yahoo.es].

Para cargar la web de prueba necesitaras previamente hacer lo siguiente.

pip install flask-socketio
 psycopg2-binary
 flask

todo junto y asi se cargara la web de prueba.
