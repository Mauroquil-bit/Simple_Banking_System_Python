# Sistema Bancario Simple en Python

<img width="353" alt="image" src="https://github.com/Mauroquil-bit/Simple_Banking_System_Python/assets/75552002/b5546381-7288-460a-a5cf-d94629e48894">



Este es el proyecto "Sistema Bancario Simple en Python" que he realizado personalmente.

En la era actual, donde todo se digitaliza, el dinero no es la excepción. Hoy en día, la mayoría de las personas poseen tarjetas de crédito que nos ahorran tiempo y energía, protegiéndonos del estrés innecesario. Las tarjetas facilitan nuestra vida de diversas maneras, desde evitarnos llevar una billetera llena de efectivo hasta ofrecernos protección al consumidor. En este proyecto, desarrollarás un sistema bancario simple con base de datos.

## Aprende más

Este proyecto es parte de los desafíos de programación ofrecidos por [Hyperskill](https://hyperskill.org/projects/109). Puedes obtener más información y seguir los pasos para implementar tu propio sistema visitando el [enlace del proyecto](https://hyperskill.org/projects/109).

## Características

* Creación de una cuenta bancaria con un número único y un PIN.
* Iniciar sesión en el sistema bancario utilizando el número de cuenta y el PIN.
* Verificación de saldo de cuenta.
* Realizar depósitos y retiros.
* Registro de todas las transacciones en una base de datos.

## Tecnologías Utilizadas

* Python
* SQLite

## Instalación y Uso

Antes de comenzar, asegúrate de tener Python instalado en tu sistema. Este proyecto fue desarrollado utilizando Python 3.8.

### Requisitos previos

Para ejecutar este proyecto necesitarás:

- Python 3.x
- pip (gestor de paquetes de Python)
- SQLite3

### Configuración del entorno

Recomendamos crear un entorno virtual para gestionar las dependencias:

```bash
python -m venv env
source env/bin/activate  # En Windows usa `env\Scripts\activate`
```

## Curiosidades: ¿Cómo es el Algoritmo de Luhn?

El Algoritmo de Luhn, también conocido como "fórmula de Luhn", "modulus 10" o "mod 10 algorithm", es un método simple de suma de verificación utilizado para validar una variedad de números de identificación, principalmente números de tarjetas de crédito. Fue desarrollado por Hans Peter Luhn, un científico de IBM.

### ¿Cómo funciona?

Piensa en el Algoritmo de Luhn como un vigilante que verifica la legitimidad de los números de una tarjeta de crédito antes de que se procese una transacción. Aquí te explico cómo:

- **Comienza desde el final**: Empieza con el último dígito de un número y muévete hacia atrás (de derecha a izquierda).

- **Alterna y multiplica**: Multiplica cada segundo dígito por dos. Si este producto es mayor que 9 (por ejemplo, 8 * 2 = 16), súmale los dígitos (1 + 6 = 7) para obtener un único dígito.

- **Suma todo**: Suma todos los dígitos, tanto los modificados como los que no.

- **El gran final**: Si el total de la suma es un múltiplo de 10 (es decir, si es divisible por 10 sin dejar residuo), entonces el número es válido según el Algoritmo de Luhn.

Este proceso ayuda a confirmar que el número de tarjeta de crédito es potencialmente válido y no una serie aleatoria de dígitos.

## Contribuir

Si deseas contribuir a este proyecto, por favor haz un fork del repositorio y luego envía un pull request con tus mejoras.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más información.

## Autor

* **Mauricio Mercado** - *Trabajo Inicial* - [Perfil de Hyperskill](https://hyperskill.org/profile/415935286)

## Agradecimientos

* Agradecimientos a Hyperskill por proveer el esqueleto del proyecto.
* Agradecimientos a todos los que han contribuido al proyecto.


