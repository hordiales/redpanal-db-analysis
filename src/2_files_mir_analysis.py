#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 
Recorre un directorio con wavs y extrae descriptores MIR para todos los archivos de audio .wav

Utiliza docker, aunque podría hacerse instalando las dependencias de Essentia
    Ejemplo: docker run -it --rm -v `pwd`:/tmp mtgupf/ac-audio-extractor:v2 -i /tmp/audio.wav -o /tmp/analysis.json -smt
    Referencia: https://www.audiocommons.org/2018/07/15/audio-commons-audio-extractor.html

Flags: -smt
  -t, --timbral-models  include descriptors computed from timbral models
  -m, --music-pieces    include descriptors designed for music pieces
  -s, --music-samples   include descriptors designed for music samples
"""

import os
import sys
import subprocess

import logging
import json

#EXT_FILTER = ['.wav'] # only wavs
EXT_FILTER = ['.wav', '.mp3', '.m4a', '.ogg', '.oga', '.flac'] # preserver original format
JSON_MIR_FORMAT = 'json' # json basic format (plain)
#JSON_MIR_FORMAT = 'jsonld' # json compatible con Audio Commons Ontology


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)  

Usage = "./files_mir_analysis.py [FILES_DIR] [JSON_DIR]"
def main():  
    if len(sys.argv) < 3:
        print("\nBad amount of input arguments\n\t", Usage, "\n")
        print(Usage)
        sys.exit(1)

    try:
        files_dir = sys.argv[1] 
        JSON_FILES_DIR = sys.argv[2] 

        if not os.path.exists(files_dir):                         
            raise IOError("There is no sound directory")

        error_count = 0
        for subdir, dirs, files in os.walk(files_dir):
            for f in files:
                if not os.path.splitext(f)[1] in EXT_FILTER:
                    continue
                tag_dir = subdir
                input_filename = f
                audio_input = subdir+'/'+f

                try:
                    print(( "\n*** MIR extract %s\n"%f ))

                    subprocess.call("docker run -it --rm -v \"%s\":/tmp -v %s:/json mtgupf/ac-audio-extractor:v2 -i \"%s\" -o \"%s\" -smt -f %s"%(subdir, JSON_FILES_DIR, '/tmp/'+f, '/json/'+os.path.splitext(f)[0]+'.json',JSON_MIR_FORMAT), shell=True)

                except Exception as e:
                    print(logger.exception(e))
                    error_count += 1 
                    continue					                		                        

        print(("Errors: %i"%error_count))
        sys.exit( error_count )
    except Exception as e:
        logger.exception(e)
        exit(1)

if __name__ == '__main__': 
    main()
