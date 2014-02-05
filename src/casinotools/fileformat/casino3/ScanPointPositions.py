#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2054 $"
__svnDate__ = "$Date: 2010-10-08 16:32:39 -0400 (Fri, 08 Oct 2010) $"
__svnId__ = "$Id: ScanPointPositions.py 2054 2010-10-08 20:32:39Z hdemers $"

# Standard library modules.
import os
import logging

# Third party modules.

# Local modules.
import casinoTools.FileFormat.casino3.FileReaderWriterTools as FileReaderWriterTools

# Globals and constants variables.

class ScanPointPositions(FileReaderWriterTools.FileReaderWriterTools):
    def __init__(self):
        self.reset()
        
    def reset(self):
        self._positions = []
        
        self._startPosition = 0
        self._endPosition = 0
        self._filePathname = ""
        self._fileDescriptor = 0
    
    def getNumberPoints(self):
        return len(self._positions)
    
    def addPosition(self, point):
        self._positions.append(point)
        
    def getPositions(self):
        return self._positions
    
    def read(self, file):
        assert file.mode == 'rb'
        self._startPosition = file.tell()
        self._filePathname = file.name
        self._fileDescriptor = file.fileno()
        logging.debug("File position at the start of %s.%s: %i", self.__class__.__name__, "read", self._startPosition)
        
        # Move backward to read the previous tag, which indicate indirectly the start of this section.
        currentPosition = file.tell()
        if currentPosition > 16:
            file.seek(-16, os.SEEK_CUR)
            
        tagID = "*SIM_OPT_END%"
        if self.findTag(file, tagID):
            self.reset()
            
            self._startPosition = file.tell()
            self._filePathname = file.name
            self._fileDescriptor = file.fileno()
            logging.debug("File position at the start of %s.%s: %i", self.__class__.__name__, "read", self._startPosition)
            numberPoints = self.readInt(file)
            
            for dummy in xrange(numberPoints):
                x = self.readDouble(file)
                y = self.readDouble(file)
                z = self.readDouble(file)
                
                points = (x, y, z)
                
                self.addPosition(points)
                
        self._endPosition = file.tell()
        logging.debug("File position at the end of %s.%s: %i", self.__class__.__name__, "read", self._endPosition)
        
        return None
    
    def export(self, exportFile):
        # todo: implement the export method.
        pass
    
if __name__ == '__main__':    #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
