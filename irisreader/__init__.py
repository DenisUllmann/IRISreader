from irisreader.file_hub import file_hub, ASTROPY_FILE_METHOD
from irisreader.iris_data_cube import iris_data_cube
from irisreader.sdo_data_cube import sdo_data_cube
from irisreader.raster_cube import raster_cube
from irisreader.sji_cube import sji_cube
from irisreader.aia_cube import aia_cube
from irisreader.get_lines import get_lines
from irisreader.has_line import has_line
from irisreader.observation import observation
from irisreader.observation import get_obs_path
from irisreader.obs_iterator import obs_iterator
from irisreader.config import config_template

# instantiate a configuration object
config = config_template()

# instantiate file hub object and make it global
file_hub = file_hub( ASTROPY_FILE_METHOD )

# format for warnings
import warnings
def warning_format(message, category, filename, lineno, file=None, line=None):
    return 'Warning: {} \n'.format( message )
    warnings.formatwarning = warning_format


