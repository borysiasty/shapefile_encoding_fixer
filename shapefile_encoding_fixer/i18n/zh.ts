<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE TS>
<TS version="2.1" language="zh_CN" sourcelanguage="en">
<context>
    <name>EncodingFixerDialog</name>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="135"/>
        <source>NOTE: With this tool you can set or clear attribute table encoding &lt;u&gt;declaration&lt;/u&gt; for Shapefiles. It doesn&apos;t change the real data encoding though.</source>
        <translation>注意：使用此工具，您可以为Shapefile设置或清除属性表编码&lt;u&gt;声明&lt;/u&gt;。但它并没有改变真正的数据编码。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="392"/>
        <source>Shapefile Encoding Fixer</source>
        <translation>Shapefile 编码修复</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="228"/>
        <source>ERROR: Cannot find the DBF file</source>
        <translation>错误：找不到DBF文件</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="238"/>
        <source>ERROR: Cannot open the DBF file</source>
        <translation>错误信息：无法打开DBF文件</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="241"/>
        <source>NOT SET</source>
        <translation>不要设置</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="247"/>
        <source>UNKNOWN</source>
        <translation>未知</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="264"/>
        <source>NONE</source>
        <translation>空</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="281"/>
        <source>Clearing LDID byte and removing CPG file will disable encoding autodetection. Exactly like in older QGIS versions, you will be able to use the drop-down list in the Add Vector Layer window to choose the layer encoding.</source>
        <translation>清除LDID字节并删除CPG文件将禁用编码自动检测。与旧的QGIS版本完全相同，您可以使用“添加矢量图层”窗口中的下拉列表来选择图层编码。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="288"/>
        <source>The LDID byte of dbf file declares the codepage of attribute table. Please note the LDID byte doesn&apos;t support other encodings, especially UTF-8. Setting LDID byte will automatically remove the concurrent CPG file, if exists.</source>
        <translation>dbf文件的LDID字节声明属性表的代码页。请注意，LDID字节不支持其他编码，尤其是UTF-8。设置LDID字节将自动删除并发CPG文件（如果存在）。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="295"/>
        <source>CPG is a small additional file for Shapefile. It&apos;s an alternative for LDID byte, and it supports much more encodings. Creating CPG file will automatically clear the concurrent LDID byte, if set. If you can&apos;t find your encoding, please &lt;a href=&apos;http://hub.qgis.org/projects/shpencodingfixer/issues&apos;&gt;request it&lt;/a&gt;.</source>
        <translation>CPG是 Shapefile 的一个小附加文件。它是LDID字节的替代方案，它支持更多的编码。如果设置，创建CPG文件将自动清除并存的LDID字节。如果找不到您的编码，请&lt;a href=&apos;http://hub.qgis.org/projects/shpencodingfixer/issues&apos;&gt;请求&lt;/a&gt;。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="301"/>
        <source>Select file</source>
        <translation>选择文件</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="324"/>
        <source>The layer is in editing mode. You have to save changes and close the editing mode first.</source>
        <translation>图层处于编辑模式。您必须先保存更改并关闭编辑模式。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="358"/>
        <source>Oooops, I can&apos;t reload the modified layer :(</source>
        <translation>哦哦， 我不能修改layer信息</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="378"/>
        <source>Can&apos;t write to the DBF file. Check permissions.</source>
        <translation>不能写DBF文件，请检查权限。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="392"/>
        <source>Can&apos;t write to the CPG file. Check permissions.</source>
        <translation>不能写CPG文件，请检查权限。</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="243"/>
        <source>Unclear: either current ANSI or ISO-8859-1. &lt;u&gt;Usually this is the culprit.&lt;/u&gt;</source>
        <translation type="obsolete">Niejasne: albo bieżąca strona kodowa, albo ISO-9959-1.&lt;u&gt;Zwykle to jest winowajca.&lt;/u&gt;</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="243"/>
        <source>Either current ANSI or ISO-8859-1. &lt;u&gt;Usually this is the culprit.&lt;/u&gt;</source>
        <translation>无论是当前的ANSI还是ISO-8859-1。 &lt;u&gt;通常这是罪魁祸首。&lt;/u&gt;</translation>
    </message>
</context>
<context>
    <name>EncodingFixerDialogBase</name>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="30"/>
        <source>Fix Shapefile Encoding</source>
        <translation>修复 Shapefile 编码</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="51"/>
        <source>Shapefile</source>
        <translation>Shapefile</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="61"/>
        <source>Layer info</source>
        <translation>图层信息</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="67"/>
        <source>Dbf File:</source>
        <translation>Dbf 文件：</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="74"/>
        <source>LDID byte:</source>
        <translation>LDID 字节：</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="120"/>
        <source>--</source>
        <translation>--</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="94"/>
        <source>CPG file:</source>
        <translation>CPG文件：</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="136"/>
        <source>...</source>
        <translation>...</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="190"/>
        <source>Description placeholder...</source>
        <translation>描述信息...</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="212"/>
        <source>Set LDID</source>
        <translation>设置LDID</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="244"/>
        <source>SET CPG file</source>
        <translation>设置CPG文件</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="305"/>
        <source>Clear LDID and delete CPG file</source>
        <translation>清楚LDID和删除CPG文件</translation>
    </message>
    <message>
        <location filename="../dlgencodingfixerbase.ui" line="162"/>
        <source>Fix encoding declaration</source>
        <translation>修复编码声明</translation>
    </message>
</context>
<context>
    <name>EncodingFixerPlugin</name>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="432"/>
        <source>&amp;Shapefile Encoding Fixer</source>
        <translation>&amp;Shapefile 编码修复</translation>
    </message>
    <message>
        <location filename="../encoding_fixer_plugin.py" line="424"/>
        <source>Fix Shapefile Encoding</source>
        <translation>修复 Shapefile 编码</translation>
    </message>
</context>
</TS>
