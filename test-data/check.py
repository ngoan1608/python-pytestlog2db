from heapq import merge
from lxml import etree


file_name = "C:/MyData/4.RobotFramework/Robot-ws/Github/python-pytestlog2db/test-data/output.xml"
file_name_2 = "C:/MyData/4.RobotFramework/Robot-ws/Github/python-genpackagedoc/pytest/logfiles/PyTestLog.xml"

def parse_xml(file):
   oParser = etree.XMLParser(dtd_validation=False)
   oTree = etree.parse(file_name, oParser)

   testsuites = oTree.getroot()

   for testsuite in testsuites.iter("testsuite"):
      print (testsuite.attrib)

      for testcase in testsuite.iter("testcase"):
         print(testcase.attrib)
         bPassed = True
         sTraceback = ""
         for item in testcase.iterchildren():
            print(item)
            if item.tag == "failure":
               bPassed = False
               sTraceback = item.text
         if bPassed:
            print (f"Testcase {testcase.get('name')} is Passed")
         else:
            print (f"Testcase {testcase.get('name')} is Failed")
            print (f"Traceback: {sTraceback}")

def merge_xml(*files):
   oMergedTree = None
   start_time  = "starttime"
   end_time    = "endtime"

   for item in files:
      if oMergedTree == None:
         oMergedTree = etree.parse(item).getroot()
      else:
         oAdditionalTree = etree.parse(item)
         for oSutie in oAdditionalTree.getroot().getiterator("testsuite"):
            oMergedTree.append(oSutie)

   oMergedTree.attrib['starttime'] = start_time
   oMergedTree.attrib['endtime'] = end_time
   return oMergedTree

# merged_file = merge_xml(file_name, file_name_2)
# print(etree.tostring(merged_file))


class MyModel():
   def __init__(self, name, age, school="HCMUT", job="dev"):
      self.name = name
      self._age = age
      self.school = school
      self.job = job

   @property
   def age(self):
      return self._age

   @age.setter
   def age(self, val):
      if val < 20:
         print("age less than 20")
         self._age = 20
      else:
         self._age = val

me = MyModel("Ngoan", 30)
print(me.name)
print(me.age)
print(me.school)
print(me.job)

me.age = 10
print(me.age)

me.age = 30
print(me.age)