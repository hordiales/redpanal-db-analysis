# Introducción

# Armar Dataset

### Paso 1

Convertir todos los archivos de audio a un mismo formato estándar como WAV 16bits y 44.1kHz

    ./convert_all_files_to_wav.py [FILES_DIR]


### Paso 2: Calcular features/descriptores MIR

    ./files_mir_analysis.py [FILES_DIR]

Flags: -smt
  -t, --timbral-models  include descriptors computed from timbral models
  -m, --music-pieces    include descriptors designed for music pieces
  -s, --music-samples   include descriptors designed for music samples

Formato del json (linked data): + info en https://json-ld.org/
JSON_MIR_FORMAT = 'jsonld' # json compatible con Audio Commons Ontology
The Audio Feature Ontology is a Semantic Web ontology that is designed to serve a dual purpose:


sino -f json --> json standard (SIN ontología de web semántica)

single_event: Whether the audio file contains one single audio event or more than one (true or false). This computation is based on the loudness of the signal and does not do any frequency analysis.

    if compute_timbral_models:
        if is_single_event(audiofile):
            ac_timbral_models(audiofile, ac_descriptors)
        else:
            logger.debug('{0}: skipping computation of timbral models as audio is not single event'.format(audiofile))

Source code: https://github.com/AudioCommons/ac-audio-extractor
Reference:  https://www.audiocommons.org/2018/07/15/audio-commons-audio-extractor.html

### Paso 3: 


# Dependencias

python3
ffmpeg
docker

El extractor con docker, se puede correr nativo (como alternativa a docker)
Referencia: https://www.audiocommons.org/2018/07/15/audio-commons-audio-extractor.html