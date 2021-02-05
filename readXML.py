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

        dictAttributs = {
            "name": "unknown name",
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
            for key, value in dictAttributs.items():

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
