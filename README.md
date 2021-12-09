# Aplicacion_deep_learning

## Fase 1 - Toma de datos.
<p>La información ha sido recolectada a partir del información obtenida por los Wireless Lan Controller de Cisco ubicados en el edificio del CTI en ESPOL. A través de un proceso que por intervalos va pidiendo información con el comando:

    > show client summary username

Este comando se realiza cada 30 segundos y proporciona la siguiente información:</p>

<center>

|       MAC Address       | AP Name |   Status   | Username |
|:-----------------------:|:-------:|:----------:|:--------:|
| 3c:61:05:\*\*:\*\*:\*\* |  Domo_1 | Associated |  mjordan |
| 30:07:4d:\*\*:\*\*:\*\* |  Domo_2 | Associated | stpcurry |

</center>

Antes de realizar el comando a traves de ssh se toma la fecha y hora de la workstation donde esta trabajando el proceso. Esta información se junta a la obtenida anteriormente y se guarda en un archivo txt con el siguiente formato:

```
Fecha de censo,Hora de censo,Lista de clientes separado por comas (",")
```
Un ejemplo es el siguiente:

```
17/10/2021,23:23:39,00:23:4e:**:**:** Domo_1      Associated   mjordan,3c:61:05:**:**:** Domo_1      Associated   stpcurry
```
Esta informacion se encuentra en los siguientes archivos: 

    > report.txt (WLC 1)
    > report2.txt (WLC 2)

## Fase 2 - Creación de Dataset
A partir de los archivos se ha realizado el análisis de esta información usando el lenguaje de programación Python. A partir de su lectura y limpieza de información basura. Se ha generado una fila por cada instancia de cliente con su respectiva fecha y hora de censo. El código usado se encuentra en el archivo:

    > dataset_creation.py

Para su posterior analisis, se ha guardado esta información en un archivo csv:

    > dataset.csv

Su estructura es la siguiente: 
```
Fecha y Hora de censo,Nombre de usuario,MAC Address, Access Point
```

Como ejemplo tenemos:

|   |       DateTime      |    Username      |     MacAddress    | AccessPoint  |
|:-:|:-------------------:|:----------------:|:-----------------:|:------------:|
| 1 | 2021-10-17 23:23:39 | caril.martinez   | 9c:b6:d0:10:22:6d | Domo_Teleco2 |
| 2 | 2021-10-17 23:23:39 | fernando.campana | ac:af:b9:33:65:e8 | Domo_Teleco1 |


Datetime: Muestra la fecha y hora que se realizo el registro.
Username: Muestra el nombre de usuario de la persona que estaba autenticada en ese momento en ese dispositivo
MacAddress: Muestra la MacAddress del dispositivo conectado a la red.
AccessPoint: Indica a que Access Point estaba conectado ese dispositivo.

## Fase 3 - Creación de modelo
Una vez creado los archivos, seguiremos el análisis de estos para encontrar asociaciones entre el username y la Mac Address de los dispositivos. Esto se lo realizara a traves de una tecnica de aprendizaje maquina no supervisado, que permite la asociación de elementos a partir del analisis de datos. Mas especificamente usaremos el algoritmo apriori que a partir de conjuntos de datos, determina reglas de asociación entre los datos que nosotros le entregemos.

Una vez realizado el análisis la regla de asociación se mostraran de la siguiente manera:

```
Rule: A -> B
Support: 0.061261754770382544
Confidence: 0.02017712042362823
Lift: 8.885613845321796
```

## Algoritmo Apriori
Este algoritmo fue desarrollado por R. Agrawal y R. Srikant en 1994 para poder encontrar conjuntos de item frecuentes dentro de un dataset para crear reglas de asociaciones. [1] [2]

Esta es una tecnica muy usada dentro de la mineria de datos para encontrar relaciones desconocidas, produciendo resultados que pueden ser usados en toma de decisiones o predicciones. Una de sus deventajas es el tiempo que toma en procesar toda la información del dataset.[2]

Al finalizar el analisis se mostrara la siguiente información:

```
Rule: A -> B
Support: 0.061261754770382544
Confidence: 0.02017712042362823
Lift: 8.885613845321796
```

### Rule: 

    Regla de asociación A -> B

### Support: 
Porcentaje de conjuntos donde la regla fue verdadera (Frecuencia donde A estaba asociada a B)

Con esta medida podemos definir que elementos se tomaran en cuenta y cuales no para nuestras reglas de asociación.

Cuando realizamos nuestro algoritmo este nos pide un valor minimo de soporte para que un elemento lo consideremos frecuente o no.

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Support = \frac{freq(A,B)}{N}" title="Support Equation" />

Confidence: Porcentaje en el que la regla es verdadera, solo cuando el elemento A ocurre. (Que tan seguido A y B aparecen juntos basado en el numero de ocurrencias de A) 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Confidence = \frac{freq(A,B)}{freq(A)}" title="Support Equation" />

### Lift:
Mide cuan mas frecuente A es encontrada con B en comparación a cuando no esta B.

Permite identificar reglas engañosas. Esta funciona como la fortaleza de una regla.

Su formula se describe de la siguiente manera: 

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Lift = \frac{Support(A,B)}{Support(A)xSupport(B)}" title="Support Equation" />

O tambien se la escribe en terminos de la confianza:

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Lift = \frac{Confidence(A,B)}{Support(B)}" title="Support Equation" />

Si el soporte de B es mayor a la confianza de la regla, entonces esa regla es engañosa y debe ser descartada.

# Referencias
[1] GeeksforGeeks. 2021. Apriori Algorithm - GeeksforGeeks. [online] Available at: <https://www.geeksforgeeks.org/apriori-algorithm/> [Accessed 3 November 2021].

[2] Y.-K. Woon, W.-K. Ng, y A. Das, «Fast online dynamic association rule mining», en Proceedings of the Second International Conference on Web Information Systems Engineering, dic. 2001, vol. 1, pp. 278-287 vol.1. doi: 10.1109/WISE.2001.996489.


[3] M. Al-Maolegi en B. Arkok, “An improved Apriori algorithm for association rules”, arXiv preprint arXiv:1403. 3948, 2014. 