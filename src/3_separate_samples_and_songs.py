#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 
Recorre un directorio con archivos jsons con descriptores MIR y los separa en canciones y samples.
El criterio para esta división es tomar como samples o muestras, aquellos archivos con una duración inferior a los 3 segundos

"""

import os
import sys

import logging
import json

EXT_FILTER = ['.json']
SAMPLE_SEC_REFERENCE = 5 # lower than (in seconds)
SONG_SEC_REFERENCE = 30 # greater than (in seconds)

# CONFIG (add ending '/')
JSON_SONGS_DIR = "./json-songs/"
JSON_SAMPLES_DIR = "./json-songs/"

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)  

Usage = "./.py [JSON_DIR]"
def main():  
    if len(sys.argv) < 2:
        print("\nBad amount of input arguments\n\t", Usage, "\n")
        print(Usage)
        sys.exit(1)

    try:
        files_dir = sys.argv[1]
        # TODO if JSON_SONGS_DIR or JSON_SAMES_DIR does not exist, create them

        if not os.path.exists(files_dir):                         
            raise IOError("There is no sound directory")

        error_count = 0
        for subdir, dirs, files in os.walk(files_dir):
            for f in files:
                if not os.path.splitext(f)[1] in EXT_FILTER:
                    continue
                tag_dir = subdir
                input_filename = f
                json_file = subdir+'/'+f

                try:
                    # print(( "\n*** Json MIR analysis %s\n"%f ))
                    data = json.load( open(json_file,'r') )

                    # Samples detection
                    if float(data["ac:signalDuration"]) < SAMPLE_SEC_REFERENCE:
                        # print( f, data["ac:signalDuration"], " it's a sample")
                        pass
                    # Songs detection
                    elif float(data["ac:signalDuration"]) > SONG_SEC_REFERENCE:
                        print( f, data["ac:signalDuration"], " it's a song")
                        with open(JSON_SONGS_DIR+f, "w") as write_file:
                            json.dump(data, write_file)
                    # Residual files: not song neither samples
                    else:
                        pass

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
