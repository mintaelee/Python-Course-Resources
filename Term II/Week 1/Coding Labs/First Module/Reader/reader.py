# import os
# from reader.compresssed import bzipped, gzipped

# extension_map = {
#     '.bz2': bzipped.oppener,
#     '.gz': gzipped.oppener,
# }

class Reader:
    def __init__(self, filename):
        # extension = os.path.splitext(filename)[1]
        # opener = extension_map.get(extension, open)
        self.filename = filename
        self.f = opener(filename, 'r+')
        #self.f = open(filename, 'rt')
        
    def close(self):
        self.f.close()
        
    def read(self):
       return self.f.read()