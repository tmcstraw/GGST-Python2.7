from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.csrf import csrf_exempt
from tethys_sdk.gizmos import *
from utilities import *
import json,time
from tethys_dataset_services.engines import GeoServerSpatialDatasetEngine
from sqlalchemy.orm.exc import ObjectDeletedError
from sqlalchemy.exc import IntegrityError
from model import *
import requests, urlparse
import shapely.geometry
import os
from config import *
from SHAZAAM import *
from geoserver.catalog import Catalog




@user_passes_test(user_permission_test)
def region_add(request):

    response = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        region_name = info.get('region_name')
        region_store = ''.join(region_name.split()).lower()
        thredds_id = info.get('thredds')

        shapefile = request.FILES.getlist('shapefile')

        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()


        thredds = session.query(Thredds).get(thredds_id)
        url,uname,pwd = thredds.url,thredds.username,thredds.password


        subset2(shapefile, region_store, GLOBAL_NETCDF_DIR, region_name,thredds_id)



        response = {"success":"success"}

        return JsonResponse(response)

@user_passes_test(user_permission_test)
def thredds_server_add(request):

    response = {}

    if request.is_ajax() and request.method == 'POST':
        info = request.POST

        thredds_name = info.get('thredds_name')
        thredds_url = info.get('thredds_url')
        thredds_username = info.get('thredds_username')
        thredds_password = info.get('thredds_password')

        try:
            # cat = Catalog(thredds_url, username=thredds_username, password=thredds_password,disable_ssl_certificate_validation=True)
            # layer_list = cat.get_layers()
            # if layer_list:
            Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
            session = Session()
            thredds_server = Thredds(name=thredds_name, url=thredds_url, username=thredds_username, password=thredds_password)
            session.add(thredds_server)
            session.commit()
            session.close()
            response = {"data": thredds_name, "success": "Success"}
        except Exception as e:
            print e
            response={"error":"Error processing the Thredds Server URL. Please check the url,username and password."}


        return JsonResponse(response)


@user_passes_test(user_permission_test)
def thredds_server_update(request):
    """
    Controller for updating a geoserver.
    """
    if request.is_ajax() and request.method == 'POST':
        # get/check information from AJAX request
        post_info = request.POST
        thredds_id = post_info.get('thredds_id')
        thredds_name = post_info.get('thredds_name')
        thredds_url = post_info.get('thredds_url')
        thredds_username = post_info.get('thredds_username')
        thredds_password = post_info.get('thredds_password')
        # check data
        if not thredds_id or not thredds_name or not thredds_url or not \
                thredds_username or not thredds_password:
            return JsonResponse({'error': "Missing input data."})
        # make sure id is id
        try:
            int(thredds_id)
        except ValueError:
            return JsonResponse({'error': 'Thredds Server id is faulty.'})

        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()

        thredds = session.query(Thredds).get(thredds_id)
        try:



            thredds.thredds_name = thredds_name
            thredds.thredds_url = thredds_url
            thredds.thredds_username = thredds_username
            thredds.thredds_password = thredds_password

            session.commit()
            session.close()
            return JsonResponse({'success': "Thredds Server sucessfully updated!"})
        except:
            return JsonResponse({'error': "A problem with your request exists."})


@user_passes_test(user_permission_test)
def thredds_server_delete(request):
    """
    Controller for deleting a geoserver.
    """
    if request.is_ajax() and request.method == 'POST':
        # get/check information from AJAX request
        post_info = request.POST
        thredds_id = post_info.get('thredds_id')

        # initialize session
        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()
        try:
            # delete geoserver
            try:
                thredds = session.query(Thredds).get(thredds_id)
            except ObjectDeletedError:
                session.close()
                return JsonResponse({'error': "The thredds server to delete does not exist."})
            session.delete(thredds)
            session.commit()
            session.close()
        except IntegrityError:
            session.close()
            return JsonResponse(
                {'error': "This thredds server is connected with a watershed! Must remove connection to delete."})
        return JsonResponse({'success': "Thredds Server sucessfully deleted!"})
    return JsonResponse({'error': "A problem with your request exists."})

@user_passes_test(user_permission_test)
def region_delete(request):
    """
    Controller for deleting a region.
    """
    if request.is_ajax() and request.method == 'POST':
        # get/check information from AJAX request
        post_info = request.POST
        region_id = post_info.get('region_id')

        # initialize session
        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()
        try:
            # delete region
            try:
                region = session.query(Region).get(region_id)
            except ObjectDeletedError:
                session.close()
                return JsonResponse({'error': "The geoserver to delete does not exist."})
            display_name = region.display_name
            region_store = ''.join(display_name.split()).lower()
            thredds_id = region.thredds_id
            thredds = session.query(Thredds).get(thredds_id)
            thredds_url = thredds.url
            uname = thredds.username
            pwd = thredds.password


            FILE_DIR = os.path.join(GLOBAL_NETCDF_DIR, '')

            region_dir = os.path.join(FILE_DIR + region_store, '')


            session.delete(region)
            session.commit()

            session.close()
        except IntegrityError:
            session.close()
            return JsonResponse(
                {'error': "This thredds is connected with a watershed! Must remove connection to delete."})
        finally:
        # Delete the temporary directory once the geojson string is created
            if region_dir is not None:
                if os.path.exists(region_dir):
                    shutil.rmtree(region_dir)
        return JsonResponse({'success': "Region sucessfully deleted!"})
    return JsonResponse({'error': "A problem with your request exists."})
