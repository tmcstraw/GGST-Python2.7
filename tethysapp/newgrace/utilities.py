import fiona
from netCDF4 import Dataset
import os
from datetime import datetime,timedelta
import calendar
import numpy as np
import tempfile, shutil,sys
import gdal
import ogr
import osr
import requests
import json
import functools
import shapely.geometry #Need this to find the bounds of a given geometry
import shapely.ops
import geojson
import pyproj
from pyproj import Proj, transform


def get_global_dates():
    grace_layer_options = []
    grace_nc = '/Users/travismcstraw/thredds_data/thredds/public/testdata/grace/GRC_jpl_tot.nc'
    # for file in os.listdir(GLOBAL_DIR):
    #     if file.startswith('GRC') and file.endswith('.nc'):
    #         grace_nc = GLOBAL_DIR + file

    start_date = '01/01/2002'

    nc_fid = Dataset(grace_nc, 'r')  # Reading the netcdf file
    nc_var = nc_fid.variables  # Get the netCDF variables
    nc_var.keys()  # Getting variable keys

    time = nc_var['time'][:]

    date_str = datetime.strptime(start_date, "%m/%d/%Y")  # Start Date string.

    for timestep, v in enumerate(time):
        current_time_step = nc_var['lwe_thickness'][timestep, :, :]  # Getting the index of the current timestep

        end_date = date_str + timedelta(days=float(v))  # Actual human readable date of the timestep

        ts_file_name = end_date.strftime("%Y_%m_%d")  # Changing the date string format
        ts_display = end_date.strftime("%Y %B %d")
        grace_layer_options.append([ts_display,ts_file_name])

    return grace_layer_options


def user_permission_test(user):
    return user.is_superuser or user.is_staff


def get_global_plot_api(pt_coords,start_date,end_date,GLOBAL_NC):

    graph_json = {}

    ts_plot = []

    nc_file = GLOBAL_NC
    coords = pt_coords.split(',')
    stn_lat = float(coords[1])
    stn_lon = float(coords[0])

    nc_fid = Dataset(nc_file, 'r')
    nc_var = nc_fid.variables  # Get the netCDF variables
    nc_var.keys()  # Getting variable keys

    time = nc_var['time'][:]
    start_date = '2002-01-01'
    date_str = datetime.strptime(start_date, "%Y-%m-%d")  # Start Date string.
    lat = nc_var['lat'][:]
    lon = nc_var['lon'][:]

    for timestep, v in enumerate(time):
        current_time_step = nc_var['lwe_thickness'][timestep, :, :]  # Getting the index of the current timestep

        actual_date = date_str + timedelta(days=float(v))  # Actual human readable date of the timestep


        data = nc_var['lwe_thickness'][timestep, :, :]

        lon_idx = (np.abs(lon - stn_lon)).argmin()
        lat_idx = (np.abs(lat - stn_lat)).argmin()

        value = data[lat_idx, lon_idx]

        time_stamp = calendar.timegm(actual_date.utctimetuple()) * 1000
        if start_date < unicode(actual_date) < end_date:
            ts_plot.append([time_stamp, round(float(value), 3)])
            ts_plot.sort()

    graph_json["values"] = ts_plot
    graph_json["point"] = [round(stn_lat, 2), round(stn_lon, 2)]
    graph_json = json.dumps(graph_json)
    return graph_json

def get_plot_ts(GLOBAL_DIR,signal_type,storage_type):
    return_obj = {}
    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        region_id = info.get('region-info')
        pt_coords = request.POST['point-lat-lon']

        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()

        region = session.query(Region).get(region_id)
        display_name = region.display_name
        region_store = ''.join(display_name.split()).lower()

        FILE_DIR = os.path.join(GLOBAL_DIR, '')

        region_dir = os.path.join(FILE_DIR + region_store, '')

        nc_file = os.path.join(region_dir+region_store+"_"+signal_type+"_"+storage_type+".nc")

        if pt_coords:
            graph = get_pt_region(pt_coords,nc_file)
            graph = json.loads(graph)
            return_obj["values"] = graph["values"]
            return_obj["location"] = graph["point"]

        return_obj["success"] = "success"


    return (return_obj)

def get_pt_region(pt_coords,nc_file):

    graph_json = {}
    ts_plot = []

    coords = pt_coords.split(',')
    stn_lat = float(coords[1])
    stn_lon = float(coords[0])

    nc_fid = Dataset(nc_file, 'r')
    nc_var = nc_fid.variables  # Get the netCDF variables
    nc_var.keys()  # Getting variable keys

    time = nc_var['time'][:]
    start_date = '01/01/2002'
    date_str = datetime.strptime(start_date, "%m/%d/%Y")  # Start Date string.
    lat = nc_var['lat'][:]
    lon = nc_var['lon'][:]

    for timestep, v in enumerate(time):
        current_time_step = nc_var['lwe_thickness'][timestep, :, :]  # Getting the index of the current timestep

        end_date = date_str + timedelta(days=float(v))  # Actual human readable date of the timestep

        data = nc_var['lwe_thickness'][timestep, :, :]

        lon_idx = (np.abs(lon - stn_lon)).argmin()
        lat_idx = (np.abs(lat - stn_lat)).argmin()

        value = data[lat_idx, lon_idx]

        time_stamp = calendar.timegm(end_date.utctimetuple()) * 1000

        ts_plot.append([time_stamp, round(float(value), 3)])
        ts_plot.sort()

    graph_json["values"] = ts_plot
    graph_json["point"] = [round(stn_lat, 2), round(stn_lon, 2)]
    graph_json = json.dumps(graph_json)


    return graph_json
