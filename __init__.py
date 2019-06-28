# -*- coding: utf-8 -*-
# ***************************************************************************
# __init__.py  -  Shapefile Encoding Fixer for QGIS
# ---------------------
#     begin                : 2013-03-02
#     copyright            : (C) 2013 by Borys Jurgiel
#     email                : info at borysjurgiel dot pl
# ***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************

def classFactory(iface):
  from .encoding_fixer_plugin import EncodingFixerPlugin
  return EncodingFixerPlugin(iface)
