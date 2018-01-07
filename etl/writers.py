
class RecordWriter(object):

   def write(self, record):
      pass

   def __enter__(self):
      import io
      self.fp = io.open(self.location, mode="w", encoding="utf-8") 
      return self
      
   def __exit__(self, type, value, traceback):
      self.fp.close()
      

class JsonWriter(RecordWriter):
   
   def __init__(self, location):
      self.location = location
      
   def write(self, record):
      import json
      self.fp.write(unicode(json.dumps(record)+"\n"))
      
class CSVWriter(RecordWriter):
   
   def __init__(self, location, write_header=True):
      self.location = location
      self.need_header = write_header      
      self.header = None
      
   def write(self, record):
      import unicodecsv as csv
      import StringIO
      
      if not self.header:
         self.header = list(record.keys())
         
      if self.need_header:
         iout = StringIO.StringIO()
         csv.writer(iout).writerow(self.header)
         self.fp.write(unicode(iout.getvalue()))         
         self.need_header=False
      
      iout = StringIO.StringIO()
      csv.DictWriter(iout, record.keys()).writerow(record)
      self.fp.write(unicode(iout.getvalue()))

