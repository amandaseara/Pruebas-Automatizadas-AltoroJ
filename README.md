# Pruebas-Automatizadas-AltoroJ
Practico 4 - Desarrollo de Software Seguro

Primera prueba:
En esta prueba se valida la correcta mitigacion de la vulnerabilidad de Inyección SQL en el Login de la aplicación AltoroJ. En el script se utiliza la biblioteca Request para invocar el Login con el Payload que permite la inyección encontrado en el practico 2 (' OR 1=1 --) y se verifica la respuesta del post, si la respuesta es válida significa que la vulnerabilidad está presente y se retorna exit code 1; en el caso de que la respuesta es invalida (ausencia de la vulnerabilidad) se retorna exit code 0.

Segunda prueba:
En esta prueba se valida la correcta mitigacion de la vulnerabilidad Cross Site Scripting en el Search de la aplicación AltoroJ. De manera similar a la primera prueba, se utiliza la biblioteca Request para invocar la función de búsqueda con el Payload que permite el Cross Site Scripting encontrado en el practico 2 ()
