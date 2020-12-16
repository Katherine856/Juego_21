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

Creamos una carpeta llamada features dentro del proyecto y dentro de esta, cada uno de los archivos pertenecientes a los features del programa

![feacture1](https://user-images.githubusercontent.com/54810355/102298389-09730100-3f1f-11eb-8a90-9b038e608bdd.PNG)

Ahora, teniendo en cuenta la anterior información procedemos a establecer nuestro feature

![feacture2](https://user-images.githubusercontent.com/54810355/102298817-d5e4a680-3f1f-11eb-9eca-264f88782347.PNG)

## Creacion step



## Ejecución
