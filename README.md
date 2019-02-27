# Introducción

A partir de un dataset generado a partir de la extracción de características (features) de la base de datos de sonidos de [RedPanal](https://redpanal.org), un sitio colaborativo que almacena y reproduce a demanda sonidos compartidos con licencias del tipo [Creative Commons](https://creativecommons.org/), se busca extraer conocimiento sobre la composición de la base de datos utilizando diferentes algoritmos de Machine Learning.

Para extraer features de los archivos de sonido se utilizo el [Audio Commons Extractor](https://github.com/AudioCommons/ac-audio-extractor) que genera para cada sonido un archivo JSON con diferentes valores como: duración, tonalidad, rango dinámico, volumen, si es el sonido es "loopeable o no", si se trata de un "evento único" o no, entre otros.

Originalmente la idea era analizar aquellos cuya duración era menor a 5 segundos, ya que a priori se pensaba que de los mismos se podía extraer mejor información, ya que su contenido no varia tanto en el tiempo, pero se descartó, ya que se encontró que el dataset elegido contaba con muy pocas instancias de este tipo.

## Dependencias

Consultar [Dependencias.md](Dependencias.md)    

# Vista General

![](img/análisis-general.png)

# Agradecimientos

A toda la comunidad RedPanal.org y en especial a [Xavier Gonzalez](https://github.com/xavierign) por el feedback.

# Índice

Para más detalles, consultar los archivos .ipynb (jupyter notebooks). También se pueden ver online y navegar a través de los siguientes links:

* [0 - Introducción y construcción del Dataset](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/dd5a9d930883ffeebe2ca82cc7d7bd25c41dfe2c/notebooks/0%20-%20Introducción%20y%20construcción%20del%20Dataset.ipynb)
* [1 - Visualización y clustering](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/dd5a9d930883ffeebe2ca82cc7d7bd25c41dfe2c/notebooks/1%20-%20Visualizaci%C3%B3n%20y%20clustering.ipynb)
* [2a - Regresión Logística y análisis del dataset con R](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/dd5a9d930883ffeebe2ca82cc7d7bd25c41dfe2c/notebooks/2a%20-%20Regresi%C3%B3n%20Log%C3%ADstica%20y%20an%C3%A1lisis%20del%20dataset%20con%20R.ipynb)
* [2b - Predicción usando variables dicotómicas - regresión](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/dd5a9d930883ffeebe2ca82cc7d7bd25c41dfe2c/notebooks/2b%20-%20Predicci%C3%B3n%20usando%20variables%20dicot%C3%B3micas%20-%20regresi%C3%B3n.ipynb)
* [3 - Reducción de la dimensionalidad SVD y PCA](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/dd5a9d930883ffeebe2ca82cc7d7bd25c41dfe2c/notebooks/3%20-%20Reducci%C3%B3n%20de%20la%20dimensionalidad%20SVD%20y%20PCA.ipynb)
* [4 - Conclusión parcial (primera parte)](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/4%20-%20Conclusión%20parcial.ipynb)
* [5 - Reducción de la dimensionalidad con t-SNE](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/5%20-%20Reducción%20de%20la%20dimensionalidad%20con%20t-sne.ipynb)
* [6 - DatasetParticionado - Predicción usando variables dicotómicas - regresión](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/6%20-%20DatasetParticionado%20-%20Predicción%20usando%20variables%20dicotómicas%20-%20regresión.ipynb)
* [7 - DatasetParticionado PCA y t-SNE](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/7%20-%20DatasetParticionado%20PCA%20y%20t-sne.ipynb)
* [8 - Redes Neuronales GAN y reconstrucción de fase](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/8%20-%20Redes%20Neuronales%20GAN%20y%20reconstrucción%20de%20fase.ipynb)
* [9 - Conclusión final](https://nbviewer.jupyter.org/github/hordiales/redpanal-db-analysis/blob/master/notebooks/9%20-%20Conclusión%20final.ipynb)

