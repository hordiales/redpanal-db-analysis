# Dependencias

python3
ffmpeg
docker

### Python

Dependencias de python, instalar con pip o conda.

    pip install matplotlib sklearn numpy pandas statsmodels
    pip install seaborn # extra colors
    pip install ipykernel # jupyter python kernel

### Audio Commons Extractor

Vía docker o nativo.

     docker pull mtgupf/ac-audio-extractor:v2

Referencia: https://www.audiocommons.org/2018/07/15/audio-commons-audio-extractor.html

### (alternativa) Con conda

    conda install jupyter
    conda install -c r r-irkernel=0.7 # kernel R para jupyter
    conda install statsmodels # etc