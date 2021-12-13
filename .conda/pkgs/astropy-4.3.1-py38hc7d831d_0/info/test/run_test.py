#  tests for astropy-4.3.1-py38hc7d831d_0 (this is a generated file);
print('===== testing package: astropy-4.3.1-py38hc7d831d_0 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
# import astropy._compiler
import astropy.cosmology.scalar_inv_efuncs
import astropy.io.ascii.cparser
import astropy.io.fits.compression
import astropy.io.votable.tablewriter
import astropy.modeling._projections
import astropy.timeseries.periodograms.lombscargle.implementations.cython_impl
import astropy.table._column_mixins
import astropy.table._np_utils
import astropy.utils._compiler
import astropy.utils.xml._iterparser
import astropy.wcs._wcs

# We run a subset of the tests which are the most likely to have
# issues because they rely on C extensions and bundled libraries

from astropy import test

# Do not include the io.ascii tests unless/until this issue is fixed:
# https://github.com/astropy/astropy/issues/9864
#
# They take more than two hours to run on some platforms!
# test(package='io.ascii')

test(package='time')
test(package='wcs')
test(package='convolution')#  --- run_test.py (end) ---

print('===== astropy-4.3.1-py38hc7d831d_0 OK =====');
print("import: 'astropy'")
import astropy

