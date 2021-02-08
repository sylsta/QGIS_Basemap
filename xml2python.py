from typing import List
from xml.dom import minidom

if (__name__) == "__main__":
    outputFile ="pycode4qgis.py"
    dataTypes = ["wms", "wfs", "xyz"]
    outputFileContent: List[str] = []
    outputFileContent.append('sources=[]')

    for dataType in dataTypes:
        xmldoc = minidom.parse('QGIS_%s.xml' % (dataType.upper()))
        itemList = xmldoc.getElementsByTagName(dataType)
        if dataType == "xyz": # Exception dont la resource est nommée dans QGIS_XYZ.xml
            itemList = xmldoc.getElementsByTagName(dataType+"tiles")

        sourceList = []

        sourceAttributes = {
            "name": "ERROR",
            "url": "unknown url",
            "referer": "",
            "username": "",
            "password": "",
            "authconfig": "",
            "ignoreGetMapURI": "false",
            "ignoreAxisOrientation": "false",
            "invertAxisOrientation": "false",
            "ignoreGetFeatureInfoURI": "false",
            "smoothPixmapTransform": "false",
            "version": "auto",
            "pagingenabled": "",
            "maxnumfeatures": "",
            "dpiMode": "",
            "zmax": "",
            "zmin": "",
            "tilePixelRatio": "0"
        }

        for item in itemList:
            itemsDetails = []
            itemsDetails.append('connections-%s' % dataType)
            for key, value in sourceAttributes.items():

                try:
                    itemsDetails.append(item.attributes[key].value)
                except:
                    itemsDetails.append(value)
            sourceList.append(itemsDetails)

        for source in sourceList:
            # [sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]
            outputFileContent.append('sources.append(["%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s"])' % (source[0], source[1],
                                                                                             source[6], source[5],
                                                                                             source[3], source[2],
                                                                                             source[4], source[16],
                                                                                             source[17]))

    outputFileContent.append('for source in sources:')
    outputFileContent.append('    connectionType = source[0]')
    outputFileContent.append('    connectionName = source[1]')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])')
    outputFileContent.append('    QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])')
    outputFileContent.append('iface.reloadConnections()')
    with open(outputFile, 'w') as out_file:
        out_file.write('\n'.join(outputFileContent) + '\n')
