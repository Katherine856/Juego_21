#  Tutorial de behave en python

## Descripción

El BDD es una técnica que surge a raíz del TDD (Test Driven Development). La esencia del TDD es que tenemos que escribir los tests antes que el propio código. BDD va un paso más allá, tenemos que hacer tests que sirvan para describir las especificaciones en un lenguaje que pueda editar un no-programador. La idea es que pueda haber alguien de producto, que defina las especificaciones y que a su vez son tests de aceptación.

El lenguaje más usado en BDD es Gherkin, cuya base son las sentencias Given, When y Then. Una de las implementaciones de Gherkin en Python más usadas es Behave. Con Given debemos añadir todos los pasos necesarios para llegar hasta el punto donde queremos realizar el test. En When realizamos un estímulo, lo que se prueba. Idealmente sería una única sentencia. Con Then comprobamos que el resultado del estímulo es el esperado.

Es BDD al estilo Python, utiliza pruebas escritas en lenguaje natural, respaldadas por código Python. Podemos decir que al igual que muchas otras herramientas BDD, es un clon de Cucumber pero para Python.

Al igual que las demás herramientas BDD, utiliza features donde creamos la test suite para verificar un requerimiento determinado. El archivo feature contiene escenarios donde definimos los pasos Given->When->Then para verificar los criterios de aceptación de la funcionalidad en desarrollo.

Entonces, vamos a tener muchos archivos features con criterios de aceptación que describen los comportamientos de la aplicación y una gran cantidad de código que ejercita la aplicación linkeado a los Given->When->Then que son llamados desde los escenarios en los features.

## Requisitos

Tener instalado python para usar pip

PIP es un acrónimo que significa "Paquetes de instalación PIP" o "Programa de instalación preferida". Es una utilidad de línea de comandos que le permite instalar, reinstalar o desinstalar paquetes PyPI con un comando simple y directo: "pip".

## Instalación 

Ejecutar en la consola el siguiente comando:

pip install behave

## Creación de feature

Feature: Indica el nombre de la funcionalidad que vamos a probar. Debe ser un título claro y explícito. Incluímos aquí una descripción en forma de historia de usuario: “Como [rol ] quiero [ característica ] para que [los beneficios]”. Sobre esta descripción empezaremos a construir nuestros escenarios de prueba.

Scenario: Describe cada escenario que vamos a probar.

Given: Provee contexto para el escenario en que se va a ejecutar el test, tales como punto donde se ejecuta el test, o prerequisitos en los datos. Incluye los pasos necesarios para poner al sistema en el estado que se desea probar.

When: Especifica el conjunto de acciones que lanzan el test. La interacción del usuario que acciona la funcionalidad que deseamos testear.

Then: Especifica el resultado esperado en el test. Observamos los cambios en el sistema y vemos si son los deseados.

Scenario online: se puede usar para ejecutar varios scenarios varias veces, con diferentes combinaciones de valores.

And: Se utiliza para añadir alguna condición más en alguno de los patrones Given, When o Then

But: Al igual que el And se utiliza en los patrones Given, When o Then, pero en este caso se utiliza como condición extra.

Background: Ocasionalmente, te encontrarás repitiendo los mismos GIVEN en muchos SCENARIO de una FEATURE.

Si es el caso, como se repite en cada escenario, esto es una indicación de que los patrones no son esenciales para describir los escenarios; Son detalles generales. Literalmente, puedes moverlos agrupándolos en un BACKGROUND.



Creamos una carpeta llamada features dentro del proyecto y dentro de esta, cada uno de los archivos pertenecientes a los features del programa

![feacture1](https://user-images.githubusercontent.com/54810355/102298389-09730100-3f1f-11eb-8a90-9b038e608bdd.PNG)

Ahora, teniendo en cuenta la anterior información procedemos a establecer nuestro feature

![feacture2](https://user-images.githubusercontent.com/54810355/102298817-d5e4a680-3f1f-11eb-9eca-264f88782347.PNG)

## Creacion step

Creamos una carpeta llamada steps dentro de features y dentro de esta, cada uno de los archivos pertenecientes a los steps del programa

![step1](https://user-images.githubusercontent.com/54810355/102300040-20ffb900-3f22-11eb-9e97-e6dcff2a7515.PNG)

Importamos behave y el metodo que vamos a utilizar para realizar la prueba

![step2](https://user-images.githubusercontent.com/54810355/102300041-21984f80-3f22-11eb-9a5a-025fec9dfb29.PNG)
![step3](https://user-images.githubusercontent.com/54810355/102300042-21984f80-3f22-11eb-9671-f299d26f60e0.PNG)
![step4](https://user-images.githubusercontent.com/54810355/102300044-2230e600-3f22-11eb-8206-88db9f1d66e0.PNG)
![step5](https://user-images.githubusercontent.com/54810355/102300046-2230e600-3f22-11eb-9afb-44e1ecc958c2.PNG)

## Ejecución
