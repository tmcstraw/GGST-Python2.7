import os
from .app import Newgrace as app

# thredds_url = 'http://127.0.0.1:9090/thredds/'

app_workspace = app.get_app_workspace()
app_wksp_path = os.path.join(app_workspace.path,'')
BASE_PATH = '/home/tethys/apps/GRACE2/tethysapp/newgrace/workspaces/app_workspace/'

SHELL_DIR = BASE_PATH+'shell/'

GLOBAL_NETCDF_DIR = '/home/tethys/Thredds/grace/'

SHAPE_DIR = BASE_PATH+'shape/'

