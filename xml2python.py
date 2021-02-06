from xml.dom import minidom

if (__name__) == "__main__":
    dataTypes = ["wms", "wfs", "xyz"]
    print('sources=[]')
    for dataType in dataTypes:
        xmldoc = minidom.parse('QGIS_%s_original.xml' % (dataType.upper()))
        if dataType == "xyz":
            itemList = xmldoc.getElementsByTagName(dataType+"tiles")
        else:
            itemList = xmldoc.getElementsByTagName(dataType)
        resourceList = []

        sourcesAttributes = {
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
            for key, value in sourcesAttributes.items():

                try:
                    itemsDetails.append(item.attributes[key].value)
                except:
                    itemsDetails.append(value)
            resourceList.append(itemsDetails)

        for resource in resourceList:
            # [sourcetype, title, authconfig, password, referer, url, username, zmax, zmin]
            print('sources.append(["%s", "%s", "%s", "%s", "%s","%s", "%s", "%s", "%s"])' % (resource[0], resource[1],
                                                                                             resource[6], resource[5],
                                                                                             resource[3], resource[2],
                                                                                             resource[4], resource[16],
                                                                                             resource[17]))
""""
for source in sources:
   connectionType = source[0]
   connectionName = source[1]
   QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
   QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
   QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
   QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
   QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
   QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
   QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])

# Update GUI
iface.reloadConnections()
"""