from typing import List
from xml.dom import minidom

if (__name__) == "__main__":
    output_file: str = "pycode4qgis.py"
    dataTypes: List[str] = []
    header: List[str] = []
    file_content: List[str] = []
    footer: List[str] = []

    dataTypes = ["wms", "wfs", "xyz"]
    header.append('# new list of online Web Service sources')
    header.append('sources=[]')
    header.append('')
    file_content.append('# append online Web Service sources')
    for dataType in dataTypes:
        sourceList = []
        file_content.append('# QGIS_%s.xml' % (dataType.upper()))
        xmldoc = minidom.parse('QGIS_%s.xml' % (dataType.upper()))
        itemList = xmldoc.getElementsByTagName(dataType)
        if dataType == "xyz": # Exception dont la resource est nommée dans QGIS_XYZ.xml
            itemList = xmldoc.getElementsByTagName(dataType+"tiles")

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
            file_content.append('sources.append(["%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s"])' % (source[0], source[1],
                                                                                                           source[6], source[5],
                                                                                                           source[3], source[2],
                                                                                                           source[4], source[16],
                                                                                                           source[17]))

    footer = ['', '# Add sources to browser',
              'for source in sources:',
              '   connectionType = source[0]',
              '   connectionName = source[1]',
              '   QSettings().setValue("qgis_code/%s/%s/authcfg" % (connectionType, connectionName), source[2])',
              '   QSettings().setValue("qgis_code/%s/%s/password" % (connectionType, connectionName), source[3])',
              '   QSettings().setValue("qgis_code/%s/%s/referer" % (connectionType, connectionName), source[4])',
              '   QSettings().setValue("qgis_code/%s/%s/url" % (connectionType, connectionName), source[5])',
              '   QSettings().setValue("qgis_code/%s/%s/username" % (connectionType, connectionName), source[6])',
              '   QSettings().setValue("qgis_code/%s/%s/zmax" % (connectionType, connectionName), source[7])',
              '   QSettings().setValue("qgis_code/%s/%s/zmin" % (connectionType, connectionName), source[8])',
              '',
              '# Update GUI',
              'iface.reloadConnections()',
              '']


    with open(output_file, 'w') as out_file:
        out_file.write('\n'.join(header) + '\n')
        out_file.write('\n'.join(file_content) + '\n')
        out_file.write('\n'.join(footer) + '\n')
