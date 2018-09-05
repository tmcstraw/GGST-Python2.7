from datetime import *
import time
import sys
import os, shutil
from ftplib import FTP
import logging
import numpy as np
from itertools import groupby
import tempfile, shutil, sys
import calendar
from netCDF4 import Dataset
from config import GLOBAL_NETCDF_DIR, SHELL_DIR
from django.http import JsonResponse, HttpResponse, Http404


def downloadFile(grace_data_dir):

    ftp = FTP("podaac-ftp.jpl.nasa.gov")
    ftp.login()
    ftp.cwd("/allData/tellus/L3/land_mass/RL05/netcdf/")

    files = ftp.nlst()
    jpl_file_name = "GRC_jpl_tot_test.nc"
    csr_file_name = "GRC_csr_tot_test.nc"
    gfz_file_name = "GRC_gfz_tot_test.nc"
    scale_file_name = "CLM4_scale_factor_test.nc"


    if not os.path.exists(grace_data_dir):
        os.makedirs(grace_data_dir)

    jpl_grace_file_path = os.path.join(grace_data_dir, jpl_file_name)
    csr_grace_file_path = os.path.join(grace_data_dir, csr_file_name)
    gfz_grace_file_path = os.path.join(grace_data_dir, gfz_file_name)
    scale_grace_file_path = os.path.join(grace_data_dir, scale_file_name)

    for filename in files:
        if filename.startswith("GRCTellus.JPL") and filename.endswith(".nc"):
            local_filename = os.path.join(grace_data_dir, jpl_file_name)
            local_file = open(local_filename, 'wb')
            print "Downloading JPL GRACE file..."
            ftp.retrbinary('RETR ' + filename, local_file.write)

            local_file.close()


        if filename.startswith("GRCTellus.CSR") and filename.endswith(".nc"):
            local_filename = os.path.join(grace_data_dir, csr_file_name)
            local_file = open(local_filename, 'wb')
            print "Downloading CSR GRACE file..."
            ftp.retrbinary('RETR ' + filename, local_file.write)

            local_file.close()

        if filename.startswith("GRCTellus.GFZ") and filename.endswith(".nc"):
            local_filename = os.path.join(grace_data_dir, gfz_file_name)
            local_file = open(local_filename, 'wb')
            print "Downloading GFZ GRACE file..."
            ftp.retrbinary('RETR ' + filename, local_file.write)

            local_file.close()

        if filename.startswith("CLM4") and filename.endswith(".nc"):
            local_filename = os.path.join(grace_data_dir, scale_file_name)
            local_file = open(local_filename, 'wb')
            print "Downloading Scale Factor GRACE file..."
            ftp.retrbinary('RETR ' + filename, local_file.write)

            local_file.close()

    return jpl_grace_file_path, csr_grace_file_path, gfz_grace_file_path, scale_grace_file_path


def write_gldas_text_file():
    grace_date_st = []
    grace_nc = GLOBAL_NETCDF_DIR + 'temp/'+'GRC_jpl_tot_test.nc'

    start_date = '01/01/2002:00:00'
    nc_fid = Dataset(grace_nc, 'r') #Reading the netcdf file
    nc_var = nc_fid.variables # Get netcdf Variables
    nc_var.keys() #Getting Variable Keys

    time = nc_var['time'][:]

    date_str = datetime.strptime(start_date, "%m/%d/%Y:%H:%M") #Start date String

    f = open(GLOBAL_NETCDF_DIR+"temp/GLDASlinks.txt", 'w')

    for timestep, v in enumerate(time):
        current_time_step = nc_var['lwe_thickness'][timestep, :, :]  # Getting the Index of the current timestep

        end_date = date_str + timedelta(days=float(v)) # Actual Human readable date of timestep

        ts_file_name = end_date.strftime("%Y%m%d.%H%M") #Change the date string to match text link download format
        ts_display = end_date.strftime("%Y %B %d")
        year = end_date.strftime("%Y")
        num_days = end_date.timetuple().tm_yday
        if 10 <= num_days < 100:
            num_days = '0'+str(num_days)
        elif num_days < 10:
            num_days = '00'+str(num_days)
        else:
            num_days = str(num_days)

        grace_date_st.append([ts_display, ts_file_name])
        f.write("http://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FGLDAS%2FGLDAS_NOAH025_3H.2.1%2F"+year+"%2F"+num_days+"%2FGLDAS_NOAH025_3H.A"+ts_file_name+".021.nc4&FORMAT=bmM0Lw&BBOX=-60%2C-180%2C90%2C180&LABEL=GLDAS_NOAH025_3H.A"+ts_file_name+".021.nc4.SUB.nc4&SHORTNAME=GLDAS_NOAH025_3H&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=2.1&VARIABLES=CanopInt_inst%2CQs_acc%2CQsb_acc%2CQsm_acc%2CRootMoist_inst%2CSoilMoi0_10cm_inst%2CSoilMoi10_40cm_inst%2CSoilMoi100_200cm_inst%2CSoilMoi40_100cm_inst%2CSWE_inst"+"\n")
    f.close()

    return grace_date_st


def download_gldas_data():
    os.system(SHELL_DIR+'gldas_download.sh '+GLOBAL_NETCDF_DIR+'temp/'+' gracedata1 '+'GRACEData1 '+'GLDASlinks.txt')

    return JsonResponse({"success": "success"})


def download_monthly_gldas_data():
    os.system(SHELL_DIR+'monthly_gldas_download.sh '+GLOBAL_NETCDF_DIR+'temp/'+' gracedata1 '+'GRACEData1')

    return JsonResponse({"success": "success"})
