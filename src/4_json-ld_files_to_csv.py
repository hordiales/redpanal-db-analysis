#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

""" 
Recorre un directorio con archivos jsons con descriptores MIR y
filtra los valores de interés y los convierte en un archivo en formato .csv

Estructura del .csv:

    Duration, Loudness, LogAttackTime, Tempo, Tempo.confidence, TemporalCentroid, Pitch, Pitch.confidence, Key, Key.confidence, Loop?


Warning: Key es Categoria (G, G major, etc)

"""

import os
import sys

import logging
import json

EXT_FILTER = ['.json']
OUTPUT_CSV_FILE = 'snd-dataset-from-json-ld.csv'

CSV_TYPE = 'R' # read with: data <- read.table("Rsnd-dataset.csv", header=TRUE, sep=",", comment.char = "$")
# CSV_TYPE = 'sklearn'

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
        if CSV_TYPE=='R':
            csv_file = open('R'+OUTPUT_CSV_FILE, "w")
        else:
            csv_file = open(OUTPUT_CSV_FILE, "w")

        # Warning: Key es Categoria (G, G major, etc)
        if CSV_TYPE=='R':
            csv_file.write( """"Duration","Loudness","LogAttackTime","Tempo","Tempo.confidence","TemporalCentroid","Pitch","Pitch.confidence","Key","Key.confidence","Loop"\n""" )
        else:
            #WARNING: separate with ',' without spaces! (pandas compatibility)
            csv_file.write( "Duration,Loudness,LogAttackTime,Tempo,Tempo.confidence,TemporalCentroid,Pitch,Pitch.confidence,Key,Key.confidence,Loop\n")

        for subdir, dirs, files in os.walk(files_dir):
            for f in files:
                if not os.path.splitext(f)[1] in EXT_FILTER:
                    continue
                tag_dir = subdir
                input_filename = f
                json_file = subdir+'/'+f
                try:
                    data = json.load( open(json_file,'r') )

                    new_line = ""
                    new_line += str(data["ac:signalDuration"]) + ','
                    # print(data["ac:signalAudioFeature"])
                    features = dict()
                    for item in data["ac:signalAudioFeature"]:
                        if item["@type"]=="afv:Loudness":
                            features['Loudness'] = str( item["afo:value"] )
                        elif item["@type"]=="afv:LogAttackTime":
                            features['LogAttackTime'] = str( item["afo:value"] )
                        elif item["@type"]=="afv:Tempo":
                            features['Tempo'] = str( item["afo:value"] )
                            features['Tempo.confidence'] = str( item["afo:confidence"] )
                        elif item["@type"]=="afv:TemporalCentroid":
                            features['TemporalCentroid'] = str( item["afo:value"] )
                        elif item["@type"]=="afv:Pitch":
                            features['Pitch'] = str( item["afo:value"] )
                            features['Pitch.confidence'] = str( item["afo:confidence"] )
                        elif item["@type"]=="afv:Key":
                            features['Key'] = str( item["afo:value"] )
                            features['Key.confidence'] = str( item["afo:confidence"] )
                        elif item["@type"]=="afv:Loop":
                            features['Loop'] = str( item["afo:value"] )

                    # Duration, Loudness, LogAttackTime, Tempo, Tempo.confidence, TemporalCentroid, Pitch, Pitch.confidence, Key, Key.confidence, Loop?
                    # Warning: Key es Categoria (G, G major, etc)
                    # print(features)
                    new_line += features['Loudness']+','
                    new_line += features['LogAttackTime']+','
                    new_line += features['Tempo']+','
                    new_line += features['Tempo.confidence']+','
                    new_line += features['TemporalCentroid']+','
                    new_line += features['Pitch']+','
                    new_line += features['Pitch.confidence']+','
                    new_line += features['Key']+','
                    new_line += features['Key.confidence']+','
                    new_line += features['Loop']

                    csv_file.write( new_line + '\n' )

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
