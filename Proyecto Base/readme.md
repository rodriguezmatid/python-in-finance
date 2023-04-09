# Finanzas desde Python

## Detalle de carpetas

```clases```

Contiene los handouts y trabajos realizados en clase.


```data```

Contendrá los datasets que utilizaremos.


```ps```

Carpeta donde alojar los Problem Sets Resueltos.

<br/>

## Detalles de archivos

```readme.md```

Este archivo. (Formato Markdown)


```requirements.txt```

Incluye los paquetes de Anaconda requeridos para el curso.

</br>

## Creando un entorno de Anaconda dedicado

```
conda activate base

conda create -n finpy_310 python=3.10
conda activate finpy_310

conda config --env --add channels conda-forge
conda config --env --set channel_priority strict

conda install --file requirements.txt
```
