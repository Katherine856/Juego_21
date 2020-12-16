#  Tutorial de behave en python

## Descripción

El BDD es una técnica que surge a raíz del TDD (Test Driven Development). La esencia del TDD es que tenemos que escribir los tests antes que el propio código. BDD va un paso más allá, tenemos que hacer tests que sirvan para describir las especificaciones en un lenguaje que pueda editar un no-programador. La idea es que pueda haber alguien de producto, que defina las especificaciones y que a su vez son tests de aceptación.

El lenguaje más usado en BDD es Gherkin, cuya base son las sentencias Given, When y Then. Una de las implementaciones de Gherkin en Python más usadas es Behave. Con Given debemos añadir todos los pasos necesarios para llegar hasta el punto donde queremos realizar el test. En When realizamos un estímulo, lo que se prueba. Idealmente sería una única sentencia. Con Then comprobamos que el resultado del estímulo es el esperado.

Es BDD al estilo Python, utiliza pruebas escritas en lenguaje natural, respaldadas por código Python. Podemos decir que al igual que muchas otras herramientas BDD, es un clon de Cucumber pero para Python.

Al igual que las demás herramientas BDD, utiliza features donde creamos la test suite para verificar un requerimiento determinado. El archivo feature contiene escenarios donde definimos los pasos Given->When->Then para verificar los criterios de aceptación de la funcionalidad en desarrollo.

Entonces, vamos a tener muchos archivos features con criterios de aceptación que describen los comportamientos de la aplicación y una gran cantidad de código que ejercita la aplicación linkeado a los Given->When->Then que son llamados desde los escenarios en los features.

## Requisitos



## Instalación 


## Creación de feacture


## Creacion step
