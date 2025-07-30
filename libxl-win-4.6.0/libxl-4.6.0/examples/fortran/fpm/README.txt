To build and run the examples using the Fortran Package Manager fpm, edit the
appropriate .bat file in the fpm fploder to set the paths of fpm and gfortran
or Intel's setvars.bat. (Note that doskey can be used to alias the downloaded
fpm executable - see, for examples set_fpm.bat.)

Execute the appropriate .bat file.

In the resulting command window type:

fpm build

To run an example, eg invoice, type:

fpm run --example invoice

The .xlsx files created by the examples will be written to the fpm folder.
