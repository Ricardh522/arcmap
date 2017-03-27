import arcpy
from arcpy import mapping
import json
import os
import sys

#Test values
# mapfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/fixtures/webmap.json")
template = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests/templates/RTAA.mxd")
# file = open(mapfile, 'r')
# webmap = file.read()


class MXDConvert:
    def __init__(self, json, layout, format):
        self.webmap = json
        self.layout = layout
        self.format = format
        pass

    def process_template(self):

        result = mapping.ConvertWebMapToMapDocument(self.webmap, template)
        mxd = result.mapDocument

        outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output/WebMapMXD.pdf")
        mapping.ExportToPDF(mxd, outfile)
        out_bytes = open(outfile, 'rb')
        return out_bytes.read()

if __name__ == "__main__":
    webmap = sys.argv[1]
    layout = sys.argv[2]
    format = sys.argv[3]
    conv = MXDConvert(webmap, layout, format)
    print(conv.process_template())

"""
This is the django view to use for this tool


@api_view(['POST'])
# @renderer_classes((JSONPRenderer,))
@authentication_classes((AllowAny,))
@ensure_csrf_cookie
def print_mxd(request, format=None):
    v = system_paths()
    arcmap_path = v["arcmap_path"]
    mxd_script = v["mxd_script"]

    username = get_username(request)
    data = request.POST
    webmap = data['Web_Map_as_JSON']
    out_folder = os.path.join(MEDIA_ROOT, username)
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    os.chdir(out_folder)

    temp_file = open('webmap.json', 'w')
    temp_file.write(webmap)
    temp_file.close()

    format = data['Format']
    layout_template = data['Layout_Template']

    args = [arcmap_path, mxd_script, '-username', username, '-media', MEDIA_ROOT, '-layout', layout_template, '-format', format]
    proc = subprocess.Popen(args, executable=arcmap_path, stderr=PIPE, stdout=PIPE)
    out, err = proc.communicate()

    response = Response()
    # This format must be identical to the DataFile object returned by the esri print examples
    host = request.META["HTTP_HOST"]

    if host == "127.0.0.1:8080":
        protocol = "http"
    else:
        protocol = "https"

    url = "{}://{}/media/{}/{}".format(protocol, request.META["HTTP_HOST"], username, "layout.pdf")

    response.data = {
        "messages": [],
        "results": [{
            "value": {
                "url": url
            },
            "paramName": "Output_File",
            "dataType": "GPDataFile"
        }]
    }
    return response
"""