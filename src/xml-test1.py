from lxml import etree

xmlStr = '''

<ins_api>
  <type>cli_show</type>
  <version>1.2</version>
  <sid>eoc</sid>
  <outputs>
    <output>
      <body>
      <hostname>nxosv.cisco.com</hostname>
     </body>
      <input>show hostname</input>
      <msg>Success</msg>
      <code>200</code>
    </output>
  </outputs>
</ins_api>
'''

# json.loads() benzeri
xmlObj = etree.fromstring(xmlStr)
data = xmlObj.find(".//hostname")
data2 = xmlObj.find(".//input")

print(data.text)
print(data2.text)