# -*- coding: utf-8 -*-

import os

from qgis.PyQt.QtCore import (
    Qt,
    QDir,
    QFile,
    QIODevice,
    QFileInfo,
    QLocale,
    QTranslator,
    QCoreApplication
)
from qgis.PyQt.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QMessageBox,
    QAction
)
from qgis.PyQt import uic

from qgis.core import (
    QgsSettings,
    QgsProject,
    QgsVectorLayer
)

from shapefile_encoding_fixer.gui.gui_utils import GuiUtils

FORM_CLASS, _ = uic.loadUiType(GuiUtils.get_ui_file_path('dlgencodingfixerbase.ui'))

allLdids = {
    1: ['437', 'US MS-DOS'],
    2: ['850', 'International MS-DOS'],
    3: ['1252', 'Windows ANSI Latin I'],
    4: ['10000', 'Standard Macintosh'],
    8: ['865', 'Danish OEM'],
    9: ['437', 'Dutch OEM'],
    10: ['850', 'Dutch OEM'],
    11: ['437', 'Finnish OEM'],
    13: ['437', 'French OEM'],
    14: ['850', 'French OEM'],
    15: ['437', 'German OEM'],
    16: ['850', 'German OEM'],
    17: ['437', 'Italian OEM'],
    18: ['850', 'Italian OEM'],
    19: ['932', 'Japanese Shift-JIS'],
    20: ['850', 'Spanish OEM'],
    21: ['437', 'Swedish OEM'],
    22: ['850', 'Swedish OEM'],
    23: ['865', 'Norwegian OEM'],
    24: ['437', 'Spanish OEM'],
    25: ['437', 'English OEM (Great Britain)'],
    26: ['850', 'English OEM (Great Britain)'],
    27: ['437', 'English OEM (US)'],
    28: ['863', 'French OEM (Canada)'],
    29: ['850', 'French OEM'],
    31: ['852', 'Czech OEM'],
    34: ['852', 'Hungarian OEM'],
    35: ['852', 'Polish OEM'],
    36: ['860', 'Portuguese OEM'],
    37: ['850', 'Portuguese OEM'],
    38: ['866', 'Russian OEM'],
    55: ['850', 'English OEM (US)'],
    64: ['852', 'Romanian OEM'],
    77: ['936', 'Chinese GBK (PRC)'],
    78: ['949', 'Korean (ANSI/OEM)'],
    79: ['950', 'Chinese Big5 (Taiwan)'],
    80: ['874', 'Thai (ANSI/OEM)'],
    87: ['Current ANSI CP', 'ANSI'],
    88: ['1252', 'Western European ANSI'],
    89: ['1252', 'Spanish ANSI'],
    100: ['852', 'Eastern European MS-DOS'],
    101: ['866', 'Russian MS-DOS'],
    102: ['865', 'Nordic MS-DOS'],
    103: ['861', 'Icelandic MS-DOS'],
    104: ['895', 'Kamenicky (Czech) MS-DOS'],
    105: ['620', 'Mazovia (Polish) MS-DOS'],
    106: ['737', 'Greek MS-DOS (437G)'],
    107: ['857', 'Turkish MS-DOS'],
    108: ['863', 'French-Canadian MS-DOS'],
    120: ['950', 'Taiwan Big 5'],
    121: ['949', 'Hangul (Wansung)'],
    122: ['936', 'PRC GBK'],
    123: ['932', 'Japanese Shift-JIS'],
    124: ['874', 'Thai Windows/MS–DOS'],
    134: ['737', 'Greek OEM'],
    135: ['852', 'Slovenian OEM'],
    136: ['857', 'Turkish OEM'],
    150: ['10007', 'Russian Macintosh'],
    151: ['10029', 'Eastern European Macintosh'],
    152: ['10006', 'Greek Macintosh'],
    200: ['1250', 'Eastern European Windows'],
    201: ['1251', 'Russian Windows'],
    202: ['1254', 'Turkish Windows'],
    203: ['1253', 'Greek Windows'],
    204: ['1257', 'Baltic Windows']
}

availableLdids = [
    [200, 'cp1250', 'Eastern European Windows'],
    [201, 'cp1251', 'Russian Windows'],
    [88, 'cp1252', 'Western European ANSI'],
    [203, 'cp1253', 'Greek Windows'],
    [202, 'cp1254', 'Turkish Windows'],
    [204, 'cp1257', 'Baltic Windows'],
    [19, '932', 'Japanese Shift-JIS']
]

allCpgs = [
    ['UTF-8', 'UTF-8'],
    ['88591', 'ISO-8859-1 Western European'],
    ['88592', 'ISO-8859-2 Eastern European'],
    ['88593', 'ISO-8859-3 Southern European'],
    ['88594', 'ISO-8859-4 Baltic'],
    ['88595', 'ISO-8859-5 Cyrillic'],
    ['88596', 'ISO-8859-6 Arabic'],
    ['88597', 'ISO-8859-7 Greek'],
    ['88598', 'ISO-8859-8 Hebrew'],
    ['88599', 'ISO-8859-9 Turkish'],
    ['885910', 'ISO-8859-10 Nordic'],
    ['885913', 'ISO-8859-13 Baltic Rim'],
    ['885915', 'ISO-8859-15 Western European'],
    ['1250', 'Eastern European Windows CP1250'],
    ['1251', 'Cyrillic Windows CP1251'],
    ['1252', 'Latin 1 Windows CP1252'],
    ['1253', 'Greek Windows CP-1253'],
    ['1254', 'Turkish Windows CP-1254'],
    ['1255', 'Hebrew Windows CP-1255'],
    ['1256', 'Arabic Windows CP-1256'],
    ['1257', 'Baltic Windows CP-1257'],
    ['1258', 'Vietnam Windows CP-1258'],
    ['SJIS', 'Japanese Shift-JIS'],
    ['Big5', 'Big5'],
    ['GBK', 'GBK']
]

availableCpgs = allCpgs


class EncodingFixerDialog(QDialog, FORM_CLASS):
    def __init__(self, parent):
        QDialog.__init__(self)
        self.iface = parent
        self.setupUi(self)
        self.setWindowIcon(GuiUtils.get_icon('encoding_fixer.png'))
        self.lastDirectory = None
        self.shapefileName = None
        self.setWidgetsEnabled(False)
        self.generalInfoString = self.tr(
            "NOTE: With this tool you can set or clear attribute table encoding <u>declaration</u> for Shapefiles. It doesn't change the real data encoding though.")
        self.buttonBox.button(QDialogButtonBox.Apply).clicked.connect(self.run)
        self.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.runAndClose)

        settings = QgsSettings()

        self.file_widget.setFilter(self.tr('Shapefiles') + ' (*.shp *.SHP)')
        self.file_widget.setDialogTitle(self.tr('Input Shapefile'))
        self.file_widget.setDefaultRoot(settings.value("plugins/shapefile-encoding-fixer/last_directory", type=str))

        self.file_widget.fileChanged.connect(self.file_changed)

        self.radioClearLDID.toggled.connect(self.radioClearLDIDToggled)
        self.radioSetLDID.toggled.connect(self.radioSetLDIDToggled)
        self.radioSetCPG.toggled.connect(self.radioSetCPGToggled)

        # populate comboEncodingLDID
        index = 0
        for i in availableLdids:
            self.comboEncodingLDID.addItem('%s (%s %s)' % (hex(i[0]), i[1], i[2]), i[0])
            if hex(i[0]).upper() == settings.value('plugins/shapefile-encoding-fixer/last_ldid_encoding', '0xc8',
                                                   type=str).upper():
                index = self.comboEncodingLDID.count() - 1
        self.comboEncodingLDID.setCurrentIndex(index)
        # populate comboEncodingCPG
        index = 0
        for i in availableCpgs:
            self.comboEncodingCPG.addItem('%s (%s)' % (i[0], i[1]), i[0])
            if i[1].upper() == settings.value('plugins/shapefile-encoding-fixer/last_cpg_encoding', 'UTF-8',
                                              type=str).upper():
                index = self.comboEncodingCPG.count() - 1
        self.comboEncodingCPG.setCurrentIndex(index)
        lastMethod = settings.value('plugins/shapefile-encoding-fixer/last_method', 'ClearLDID', type=str)
        if lastMethod == 'SetLDID':
            self.radioSetLDID.setChecked(Qt.Checked)
        elif lastMethod == 'SetCPG':
            self.radioSetCPG.setChecked(Qt.Checked)
        else:
            self.radioClearLDID.setChecked(Qt.Checked)

    def setWidgetsEnabled(self, state):
        self.labelInfo1.setEnabled(state)
        self.labelInfo2.setEnabled(state)
        self.labelInfo3.setEnabled(state)
        self.labelFile.setEnabled(state)
        self.labelLDID.setEnabled(state)
        self.labelCPG.setEnabled(state)
        self.radioClearLDID.setEnabled(state)
        self.radioSetLDID.setEnabled(state)
        self.radioSetCPG.setEnabled(state)
        self.comboEncodingLDID.setEnabled(state and self.radioSetLDID.isChecked())
        self.comboEncodingCPG.setEnabled(state and self.radioSetCPG.isChecked())
        self.labelMethodDescription.setEnabled(state)
        self.buttonBox.button(QDialogButtonBox.Apply).setEnabled(state)
        self.buttonBox.button(QDialogButtonBox.Ok).setEnabled(state)

    def layerSource(self, layer):
        srcPath = layer.dataProvider().dataSourceUri().split('|')[0]
        # without this one line code in win xp, srcName return something wrong,see below (patch from Volkan Kepoglu - thanks!)
        srcPath = srcPath.replace("\\", "/")
        if not srcPath.upper().endswith('.SHP'):
            # if the path doesn't point to the shp file, maybe it is directory....
            qPath = QDir(srcPath)
            qPath.setNameFilters(['*.shp', '*.SHP'])
            if len(qPath.entryList()) == 1:  # there is exactly one shapefile inside
                srcName = qPath.entryList()[0]
                srcName = srcName[:-4]
                srcPath += '/' + srcName
            else:
                # QMessageBox.warning(self, self.tr("Shapefile Encoding Fixer"), self.tr("I cannot determine the layer source file: %1 !").arg(srcPath))
                #   don't display anything, just return false to reject this layer (because e.g. DBF tables are recognized as shapefiles)
                return None
        return srcPath

    def displayLayerInfo(self):
        self.labelLDID.setText('--')
        self.labelCPG.setText('--')
        fileName = self.shapefileName[:-4]
        # read LDID data
        if QFile(fileName + '.dbf').exists():
            dbfFileName = fileName + '.dbf'
        elif QFile(fileName + '.DBF').exists():
            dbfFileName = fileName + '.DBF'
        else:
            self.labelFile.setText(self.tr(u'ERROR: Cannot find the DBF file'))
            return False
        ldid = None
        dbfFile = QFile(dbfFileName)
        if dbfFile.open(QIODevice.ReadOnly):
            if dbfFile.seek(29):
                ldid = dbfFile.readData(1)
                ldid = ord(ldid)
            dbfFile.close()
        else:
            self.labelFile.setText(self.tr(u'ERROR: Cannot open the DBF file'))
            return False
        if not ldid:
            encoDesc = '(%s)' % self.tr(u'NOT SET')
        elif ldid == 87:
            encoDesc = '(%s)' % self.tr('Either current ANSI or ISO-8859-1. <u>Usually this is the culprit.</u>')
        elif ldid in allLdids:
            encoDesc = '(%s %s)' % (allLdids[ldid][0], allLdids[ldid][1])
        else:
            encoDesc = '(%s)' % self.tr(u'UNKNOWN')
        # read CPG data
        cpgFileName = ''
        cpg = ''
        if QFile(fileName + '.cpg').exists():
            cpgFileName = fileName + '.cpg'
        elif QFile(fileName + '.CPG').exists():
            cpgFileName = fileName + '.CPG'
        if cpgFileName:
            cpgFile = QFile(cpgFileName)
            if cpgFile.open(QIODevice.ReadOnly):
                cpg = cpgFile.readLineData(32)
                if cpg:
                    cpg = cpg.strip().decode('utf-8')
                cpgFile.close()
        # display info
        self.labelFile.setText(dbfFileName)
        self.labelLDID.setText('<b>%s</b> %s' % (hex(ldid), encoDesc))
        if cpg:
            print (cpg, type(cpg))
            cpgDict = dict(allCpgs)
            if cpg in cpgDict:
                cpgDesc = '<b>%s</b> (%s)' % (cpg, cpgDict[cpg])
            else:
                cpgDesc = '<b>%s</b>' % cpg
        else:
            cpgDesc = '<b>NONE</b>'
        self.labelCPG.setText(cpgDesc)
        return True  # no errors

    def file_changed(self, path):
        QgsSettings().setValue("plugins/shapefile-encoding-fixer/last_directory", QFileInfo(path).absoluteDir().path())
        self.shapefileName = path
        if self.displayLayerInfo():
            self.setWidgetsEnabled(True)
        else:
            self.setWidgetsEnabled(False)

    def radioClearLDIDToggled(self, state):
        if state:
            self.labelMethodDescription.setText(self.tr(
                "Clearing LDID byte and removing CPG file will disable encoding autodetection. Exactly like in older QGIS versions, you will be able to use the drop-down list in the Add Vector Layer window to choose the layer encoding.") + "<br/><br/>" + self.generalInfoString)

    def radioSetLDIDToggled(self, state):
        self.comboEncodingLDID.setEnabled(state and self.radioSetLDID.isEnabled())
        if state:
            self.labelMethodDescription.setText(self.tr(
                "The LDID byte of dbf file declares the codepage of attribute table. Please note the LDID byte doesn't support other encodings, especially UTF-8. Setting LDID byte will automatically remove the concurrent CPG file, if exists.") + "<br/><br/>" + self.generalInfoString)

    def radioSetCPGToggled(self, state):
        self.comboEncodingCPG.setEnabled(state and self.radioSetCPG.isEnabled())
        if state:
            self.labelMethodDescription.setText(self.tr(
                "CPG is a small additional file for Shapefile. It's an alternative for LDID byte, and it supports much more encodings. Creating CPG file will automatically clear the concurrent LDID byte, if set. If you can't find your encoding, please <a href='http://hub.qgis.org/projects/shpencodingfixer/issues'>request it</a>.") + "<br/><br/>" + self.generalInfoString)

    def runAndClose(self):
        self.run()
        self.accept()

    def run(self):
        if not self.shapefileName:
            return
        # find if the layer is loaded to QGIS
        layer = None
        layerName = False
        for i in range(self.iface.mapCanvas().layerCount()):
            if self.layerSource(self.iface.mapCanvas().layer(i)) == self.shapefileName:
                layer = self.iface.mapCanvas().layer(i)
                layerName = layer.name()
        if layer:
            if layer.isEditable():
                QMessageBox.warning(self, self.tr("Shapefile Encoding Fixer"), self.tr(
                    "The layer is in editing mode. You have to save changes and close the editing mode first."))
                return
            # save layer symbology
            QFile.remove(QDir.tempPath() + '/' + QFileInfo(self.shapefileName).baseName() + '.qml')
            layer.saveNamedStyle(QDir.tempPath() + '/' + QFileInfo(self.shapefileName).baseName() + '.qml')
            # remove layer
            QgsProject.instance().removeMapLayer(layer.id())
        # apply the fix and store last settings
        settings = QgsSettings()
        if self.radioSetLDID.isChecked():
            ldid = self.comboEncodingLDID.itemData(self.comboEncodingLDID.currentIndex())
            self.doSetLDID(ldid, True)
            lastMethod = 'SetLDID'
            settings.setValue('plugins/shapefile-encoding-fixer/last_ldid_encoding', hex(ldid))
        elif self.radioSetCPG.isChecked():
            enc = self.comboEncodingCPG.itemData(self.comboEncodingCPG.currentIndex())
            self.doSetCPG(enc, True)
            lastMethod = 'SetCPG'
            settings.setValue('plugins/shapefile-encoding-fixer/last_cpg_encoding', enc)
        else:  # radioClearLDID is checked
            self.doSetLDID(0, True)
            lastMethod = 'ClearLDID'
        settings.setValue('plugins/shapefile-encoding-fixer/last_method', lastMethod)

        # reload layer info
        self.displayLayerInfo()
        # reload layer and restore symbology (if was loaded previously)
        if layerName:
            newLayer = QgsVectorLayer(self.shapefileName, layerName, 'ogr')
            if not newLayer.isValid():
                QMessageBox.critical(self, self.tr("Shapefile Encoding Fixer"),
                                     self.tr("Oooops, I can't reload the modified layer :("))
                return
            if lastMethod != 'ClearLDID':
                # QGIS will try to set the provider encoding to that set in AddVectorLayer dialog. If ldid is not cleared, the only valid is UTF-8
                # WARNING: Not sure if it works properly. On one machine should be completely removed, but it doesn't work on another.
                newLayer.dataProvider().setEncoding('UTF-8')
            newLayer.loadNamedStyle(QDir.tempPath() + '/' + QFileInfo(self.shapefileName).baseName() + '.qml')
            QFile.remove(QDir.tempPath() + '/' + QFileInfo(self.shapefileName).baseName() + '.qml')
            QgsProject.instance().addMapLayers([newLayer])

    def doSetLDID(self, ldid, removeCPG=True):
        dbfFile = QFile(self.shapefileName[:-4] + '.dbf')
        if dbfFile.open(QIODevice.ReadWrite) and dbfFile.seek(29):
            hexLdid = hex(ldid)[2:] # Convert to hex string and drop the \x previx
            if len(hexLdid) == 1:
                # For ldid = 0, hex(ldid)[2:] = '0' while bytes.fromhex expects '00'
                hexLdid += '0'
            dbfFile.write(bytes.fromhex(hexLdid))
            dbfFile.close()
        else:
            QMessageBox.critical(self, self.tr("Shapefile Encoding Fixer"),
                                 self.tr(u"Can't write to the DBF file. Check permissions."))
            return
        if removeCPG:
            QFile(self.shapefileName[:-4] + '.cpg').remove()
            QFile(self.shapefileName[:-4] + '.CPG').remove()

    def doSetCPG(self, enc, clearLDID=True):
        cpgFile = QFile(self.shapefileName[:-4] + '.cpg')
        if cpgFile.open(QIODevice.WriteOnly):
            cpgFile.write(enc.encode('utf-8'))
            # QTextStream stream(&cpgFile)
            # stream << enc << endl; # "123"
            # 为写入文本的字符 - - endl表示换行 - - 理解就ok；
            cpgFile.close()
        else:
            QMessageBox.critical(self, self.tr("Shapefile Encoding Fixer"),
                                 self.tr(u"Can't write to the CPG file. Check permissions."))
            return
        if clearLDID:
            self.doSetLDID(0, removeCPG=False)  # loop danger


class EncodingFixerPlugin():
    def __init__(self, iface):
        self.iface = iface
        # i18n
        pluginPath = QFileInfo(os.path.realpath(__file__)).path()  # patch by Régis Haubourg
        if QgsSettings().value('locale/overrideFlag', type=bool):
            localeName = QgsSettings().value('locale/userLocale', '')[:2]
        else:
            localeName = QLocale.system().name()[:2]
        if QFileInfo(pluginPath).exists():
            self.localePath = pluginPath + "/i18n/" + localeName + ".qm"
            if QFileInfo(self.localePath).exists():
                self.translator = QTranslator()
                self.translator.load(self.localePath)
                QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        self.action = QAction(GuiUtils.get_icon("encoding_fixer.png"),
                              QCoreApplication.translate("EncodingFixerPlugin", u"Fix Shapefile Encoding"),
                              self.iface.mainWindow())
        self.iface.registerMainWindowAction(self.action, "Ctrl+Shift+E")
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(QCoreApplication.translate("EncodingFixerPlugin", "&Shapefile Encoding Fixer"),
                                   self.action)
        self.action.triggered.connect(self.run)

    def unload(self):
        self.iface.removePluginMenu(QCoreApplication.translate("EncodingFixerPlugin", "&Shapefile Encoding Fixer"),
                                    self.action)
        self.iface.removeToolBarIcon(self.action)
        self.iface.unregisterMainWindowAction(self.action)

    def run(self):
        dlg = EncodingFixerDialog(self.iface)
        dlg.exec_()
