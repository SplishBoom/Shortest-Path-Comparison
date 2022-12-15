import os

def connect_pathes(*pathes):
    return os.path.join(*pathes)

SAFE_CACHED_FOLDERS = ["App", "Constants", "Utilities"]
SAFE_UNNECESSARY_FOLDERS = ["Temp"]
SAFE_PRE_EXISTING_CHECKLIST = ["Data Export", "Temp"]

STORE_DATA_OUTPUT_PATH = "Data Export"
STORE_TEMP_OUTPUT_PATH = "Temp"

VISUAL_DJIKSTRA_SVG_OUTPUT_PATH = connect_pathes(STORE_TEMP_OUTPUT_PATH , "Djikstra.svg")
VISUAL_ASTAR_SVG_OUTPUT_PATH = connect_pathes(STORE_TEMP_OUTPUT_PATH , "AStar.svg")
VISUAL_DJIKSTRA_PNG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "Djikstra.png")
VISUAL_ASTAR_PNG_OUTPUT_PATH = connect_pathes(STORE_DATA_OUTPUT_PATH , "AStar.png")