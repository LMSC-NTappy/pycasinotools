#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Hendrix Demers (hendrix.demers@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Hendrix Demers"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = "$Revision: 2834 $"
__svnDate__ = "$Date: 2012-08-14 08:52:07 -0400 (Tue, 14 Aug 2012) $"
__svnId__ = "$Id: GenerateSimFile.py 2834 2012-08-14 12:52:07Z hdemers $"

# Standard library modules.

# Third party modules.

# Local modules.
import casinoTools.FileFormat.casino2.File as File
#import casinoTools.FileFormat.casino2.SimulationOptions as SimulationOptions
from casinoTools.FileFormat.casino2.SimulationOptions import DIRECTION_COSINES_SOUM, CROSS_SECTION_MOTT_JOY, CROSS_SECTION_MOTT_RUTHERFORD

# Globals and constants variables.
#DIRECTION_COSINES_SOUM = SimulationOptions.DIRECTION_COSINES_SOUM

class GenerateSimFile(object):
    def __init__(self, templateFilepath):
        self._templateFilepath = templateFilepath
        self._optionSimulationData = self._extractOptionSimulationData(self._templateFilepath)

    def _extractOptionSimulationData(self, filepath):
        file = File.File()
        file.readFromFilepath(filepath)

        return file.getOptionSimulationData()

    def getOptionSimulationData(self):
        return self._optionSimulationData

    def setNumberElectrons(self, numberElectrons):
        self._optionSimulationData.getSimulationOptions().setNumberElectrons(numberElectrons)

    def setIncidentEnergy_keV(self, energy_keV):
        self._optionSimulationData.getSimulationOptions().setIncidentEnergy_keV(energy_keV)

    def setTOA_deg(self, toa_deg):
        self._optionSimulationData.getSimulationOptions().setTOA_deg(toa_deg)

    def setBeamAngle_deg(self, beamAngle_deg):
        self._optionSimulationData.getSimulationOptions().setBeamAngle_deg(beamAngle_deg)

    def addElements(self, symbols, weightFractions=None):
        self._removeAllElements()

        if weightFractions == None:
            weightFractions = []

        if len(weightFractions) == len(symbols)-1:
            lastWeightFraction = 1.0 - sum(weightFractions)
            weightFractions.append(lastWeightFraction)

        assert len(weightFractions) == len(symbols)

        for symbol, weightFraction in zip(symbols, weightFractions):
            self._addElement(symbol, weightFraction)

        self._optionSimulationData.getRegionOptions().getRegion(0).update()

    def _removeAllElements(self):
        self._optionSimulationData.getRegionOptions().getRegion(0).removeAllElements()

    def _addElement(self, symbol, weightFraction=1.0):
        numberXRayLayers = self._optionSimulationData.getSimulationOptions().getNumberXRayLayers()
        self._optionSimulationData.getRegionOptions().getRegion(0).addElement(symbol, weightFraction, numberXRayLayers)

    def save(self, filepath):
        file = File.File()
        file.setOptionSimulationData(self._optionSimulationData)
        file.write(filepath)

    def setDirectionCosines(self, directionCosinesModel):
        self._optionSimulationData.getSimulationOptions().setDirectionCosines(directionCosinesModel)

    def setElectronElasticCrossSection(self, crossSectionModel):
        self._optionSimulationData.getSimulationOptions().setTotalElectronElasticCrossSection(crossSectionModel)
        self._optionSimulationData.getSimulationOptions().setPartialElectronElasticCrossSection(crossSectionModel)
        
    def setIonizationCrossSection(self, crossSectionModel):
        self._optionSimulationData.getSimulationOptions().setIonizationCrossSectionType(crossSectionModel)
        
    def setIonizationPotential(self, model):
        self._optionSimulationData.getSimulationOptions().setIonizationPotentialType(model)
        
if __name__ == '__main__':    #pragma: no cover
    import DrixUtilities.Runner as Runner
    Runner.Runner().run(runFunction=None)
