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
OUTPUT_CSV_FILE = 'snd-dataset-from-plain-json.csv'

# CSV_TYPE = 'R' # read with: data <- read.table("Rsnd-dataset.csv", header=TRUE, sep=",", comment.char = "$")
CSV_TYPE = 'sklearn'

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
            csv_file.write( """"Duration","Loudness","LogAttackTime","Tempo","Tempo.confidence","TemporalCentroid","Pitch","Pitch.confidence","Key","Key.confidence","Loop","SingleEvent","Loop","Tonality","Tonality.confidence","DynamicRange","Note.midi","Note.frequency","Note.confidence","Genre","Mood"\n""" )
        else:
            #WARNING: separate with ',' without spaces! (pandas compatibility)
            csv_file.write( "Duration,Loudness,LogAttackTime,Tempo,Tempo.confidence,TemporalCentroid,SingleEvent,Loop,Tonality,Tonality.confidence,DynamicRange,Note.midi,Note.frequency,Note.confidence,Genre,Mood\n") 

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

                    # Duration, Loudness, LogAttackTime, Tempo, Tempo.confidence, TemporalCentroid,
                    # SingleEvent, Loop, Tonality, TonalityConfidence, DynamicRange, NoteMIDI, NoteFrequency, NoteConfidence, Genre, Mood   
                    # Warning: Tonality es Categoria (G, G major, etc), como Key en el otro json
                    new_line += str(data["duration"]) + ','
                    new_line += str(data['loudness'])+','
                    new_line += str(data['log_attack_time'])+','
                    new_line += str(data['tempo'])+','
                    new_line += str(data['tempo_confidence'])+','
                    new_line += str(data['temporal_centroid'])+','
                    # hasta acá igual al otro json (compatible)
                    new_line += str(data['single_event'])+','
                    new_line += str(data['loop'])+','
                    new_line += str(data['tonality'])+','
                    new_line += str(data['tonality_confidence'])+','
                    new_line += str(data['dynamic_range'])+','
                    new_line += str(data['note_midi'])+','
                    new_line += str(data['note_frequency'])+','
                    new_line += str(data['note_confidence'])+','
                    new_line += str(data['genre'])+','
                    new_line += str(data['mood'])

                    if data['single_event']==True:
                        print("Single event! " + f)
                        more_data = dict()

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
