import arcpy
from arcpy import mapping
import json
import os

mapfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/fixtures/webmap.json")
template = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/templates/RTAA.mxd")

file = open(mapfile, 'r')
webmap = file.read()

result = mapping.ConvertWebMapToMapDocument(webmap, template)
mxd = result.mapDocument

outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output/WebMapMXD.pdf")
mapping.ExportToPDF(mxd, outfile)
