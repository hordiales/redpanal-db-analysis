#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 
Recorre un directorio y convierte todos los archivos de audio a formato wav
Genera un reporte de los archivos generados en converted_files_to_wav.json
Usa ffmpeg
"""

import os
import sys
import subprocess

import logging
import json

EXT_FILTER = ['.mp3','.ogg','.wav','.wma','.m4a']

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)  

Usage = "./convert_all_files_to_wav.py [FILES_DIR] [WAVES_DIR]"

def main():  
    if len(sys.argv) < 3:
        print("\nBad amount of input arguments\n\t", Usage, "\n")
        print(Usage)
        sys.exit(1)

    try:
        files_dir = sys.argv[1] 
        waves_dir = sys.argv[2] 

        if not os.path.exists(files_dir):                         
            raise IOError("There is no sound directory")

        error_count = 0
        db_files = dict()
        i = 1
        for subdir, dirs, files in os.walk(files_dir):
            for f in files:
                if not os.path.splitext(f)[1] in EXT_FILTER:
                    continue
                tag_dir = subdir
                input_filename = f
                audio_input = subdir+'/'+f
                try:
                    print(( "\n*** Processing %s\n"%f ))
                    subprocess.call("ffmpeg -i \"%s\" \"%s\""%(audio_input,waves_dir+str(i)+'_'+os.path.splitext(f)[0]+'.wav'), shell=True)

                    db_files[i] = audio_input
                    i+=1
                except Exception as e:
                    print(logger.exception(e))
                    error_count += 1 
                    continue

                with open("converted_files_to_wav.json", "w") as write_file:
                    json.dump(db_files, write_file)
        print(("Errors: %i"%error_count))
        # sys.exit( -error_count )
        sys.exit( 0 )
    except Exception as e:
        logger.exception(e)
        exit(1)

if __name__ == '__main__': 
    main()
