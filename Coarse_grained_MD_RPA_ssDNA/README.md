# Code for Running Simulations

## Requirements

1. In order to run Coarse-grained simulation with ssDNA, ssDNA+RPA first a apprpriate topology is created from a given structure file (in PDB format)
2. The topology is created with an in-house Perl script, and contains the parameters for interactions (e.g. bond, angle, dihedral, contacts, repulsion), and also the coordinates.
3. Perl script: generateMDInput.pl
   Preference file: generateMDInput.prefs
   Input PDB: example.pdb
   Output dat file: example.dat
   Additional stacking interactions added using: additional_stacks.pl
   
## Running simulation

1. The src folder contains all the FORTRAN and C codes required for running simulation.
2. MDmake_compile compiles all the required codes in the src folder along with the MD.com
3. The compiled versions are kept in the bin directory
4. After compilation, the simulation is run using the MDWrapper.pl program
5. MDWrapper.pl require the MDWrapper.prefs and MDWrapper.prefs.schema