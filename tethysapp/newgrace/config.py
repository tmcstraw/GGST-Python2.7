import os
from .app import Newgrace as app

# thredds_url = 'http://127.0.0.1:9090/thredds/'

app_workspace = app.get_app_workspace()
app_wksp_path = os.path.join(app_workspace.path,'')
BASE_PATH = '/Users/travismcstraw/tethysdev/NewGRACE/tethysapp/newgrace/workspaces/app_workspace/'

SHELL_DIR = BASE_PATH+'shell/'

GLOBAL_NETCDF_DIR = '/Users/travismcstraw/thredds_data/grace/'

SHAPE_DIR = BASE_PATH+'shape/'

