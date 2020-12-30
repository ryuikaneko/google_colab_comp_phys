# -*- coding: utf-8 -*-
"""itensor.ipynb

Automatically generated by Colaboratory.
"""

# Commented out IPython magic to ensure Python compatibility.
!git clone https://github.com/ITensor/ITensor
# %cd ITensor
### ITensor v3.1.2
!git checkout 0b12e3cae78f2e2dd7843ba743c1756256ab96c8
!sed \
 -e 's/PLATFORM=macos/#PLATFORM=macos/' \
 -e 's/BLAS_LAPACK_LIBFLAGS=-framework Accelerate/#BLAS_LAPACK_LIBFLAGS=-framework Accelerate/' \
 -e 's/#PLATFORM=lapack/PLATFORM=lapack/' \
 -e 's|#BLAS_LAPACK_LIBFLAGS=-lpthread -L/usr/lib -lblas -llapack|BLAS_LAPACK_LIBFLAGS=-lpthread -L/usr/lib -lblas -llapack|' \
 -e 's/DEBUGFLAGS=-DDEBUG -g -Wall -Wno-unknown-pragmas -pedantic/#DEBUGFLAGS=-DDEBUG -g -Wall -Wno-unknown-pragmas -pedantic/' \
 options.mk.sample > options.mk
!make
# %cd sample
!make
# %cd ../tutorial
!for i in ./??_* ./finiteT ; do cd $i ; make ; cd - ; done
# %cd ../sample
### run example codes
!./dmrg
!./mixedspin
!./dmrg_table
#!./dmrgj1j2 ### input j2 is required
!./exthubbard
!./trg
!./hubbard_2d
