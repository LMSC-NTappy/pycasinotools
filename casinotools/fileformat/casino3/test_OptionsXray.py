#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Standard library modules.

# Third party modules.

# Local modules.
import casinotools.fileformat.casino3.OptionsXray as OptionsXray
import casinotools.fileformat.test_FileReaderWriterTools as test_FileReaderWriterTools

# Globals and constants variables.

class TestOptionsXray(test_FileReaderWriterTools.TestFileReaderWriterTools):

    def test_read(self):
        reader = OptionsXray.OptionsXray()
        file = open(self.filepathSim, 'rb')
        error = reader.read(file)

        self.assertEquals(None, error)
        self.assertEquals(30107002, reader._version)
        self.assertAlmostEquals(40.0, reader.TOA)
        self.assertAlmostEquals(0.0, reader.PhieRX)

        reader = OptionsXray.OptionsXray()
        file = open(self.filepathCas, 'rb')
        error = reader.read(file)

        self.assertEquals(None, error)
        self.assertEquals(30107002, reader._version)
        self.assertAlmostEquals(40.0, reader.TOA)
        self.assertAlmostEquals(0.0, reader.PhieRX)

        #self.fail("Test if the testcase is working.")

if __name__ == '__main__': #pragma: no cover
    import logging, nose
    logging.getLogger().setLevel(logging.DEBUG)
    nose.runmodule()