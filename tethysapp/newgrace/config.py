import os
from .app import Newgrace as app


app_workspace = app.get_app_workspace()
app_wksp_path = os.path.join(app_workspace.path,'')
# BASE_PATH = '/Users/travismcstraw/tethysdev/NewGRACE/tethysapp/newgrace/workspaces/app_workspace/'

BASE_PATH = app_wksp_path

thredds_url= app.get_custom_setting("Thredds wms URL")

SHELL_DIR = BASE_PATH+'shell/'

GLOBAL_NETCDF_DIR = app.get_custom_setting("Local Thredds Folder Path")

SHAPE_DIR = BASE_PATH+'shape/'

