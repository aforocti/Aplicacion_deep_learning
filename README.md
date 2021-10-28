# Aplicacion_deep_learning

## Fase 1 - Toma de datos.
<p>La información ha sido recolectada a partir del información obtenida por los Wireless Lan Controller de Cisco ubicados en el edificio del CTI en ESPOL. A través de un proceso que por intervalos va pidiendo información con el comando:

    > show client summary username

que proporciona la siguiente información:</p>

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
Fecha de censo,Hora de censo,Nombre de usuario,MAC Address, Access Point
```
## Fase 3 - Creación de modelo
