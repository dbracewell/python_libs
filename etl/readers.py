
class RecordReader(object):
   
   def records(self, in_file):
      pass
      

class CSVReader(RecordReader):
   
   def __init__(self, header=None):
      if header and isinstance(header, list):
         self.columns = header
         self.read_header = False
      elif header:
         self.read_header = True
         self.columns = None
      else:
         self.read_header = False
         self.columns = None
   
   def records(self, in_file):
      import unicodecsv as csv
      with open(in_file, 'rb') as csvfile:
         dialect = csv.Sniffer().sniff(csvfile.read(1024))
         csvfile.seek(0)

         reader = None
         if self.columns:
            reader = csv.DictReader(csvfile, fieldnames=self.columns, dialect=dialect)
         elif self.read_header:
            reader = csv.DictReader(csvfile, dialect=dialect)
         else:
            reader = csv.reader(csvfile, dialect=dialect)
            
         def convert(obj):
            if isinstance(obj, dict):
               return obj
            return dict( ("_c%s" % idx, v) for idx,v in enumerate(obj))

         for row in reader:
            if len(row) > 0:
               yield convert(row)
 
