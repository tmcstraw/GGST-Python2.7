import sys
import os.path
import fiona
import shapely.geometry
import rtree
import tempfile, shutil
from .app import Newgrace
from config import *
from django.http import JsonResponse, HttpResponse, Http404
from model import *


def subset2(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]




        # Convert Polygon to netcdf file format and subset netcdf files to region
        # os.system(SHELL_DIR+'grace2subset.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)

        # os.system(SHELL_DIR+'subset_initial.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting Region Bounds')
        # os.system(SHELL_DIR+'subset_jpl_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting JPL Total Storage')
        # os.system(SHELL_DIR+'subset_jpl_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting JPL Groundwater Storage')
        # os.system(SHELL_DIR+'subset_csr_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting CSR Total Storage')
        # os.system(SHELL_DIR+'subset_csr_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting CSR Groundwater Storage')
        # os.system(SHELL_DIR+'subset_gfz_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting GFZ Total Storage')
        # os.system(SHELL_DIR+'subset_gfz_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting GFZ Groundwater Storage')
        # os.system(SHELL_DIR+'subset_avg_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting AVG Total Storage')
        # os.system(SHELL_DIR+'subset_avg_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting AVG Groundwater Storage')
        # os.system(SHELL_DIR+'subset_sw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting Surface Water Storage')
        # os.system(SHELL_DIR+'subset_soil.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Subsetting Soil Moisture Storage')
        # os.system(SHELL_DIR+'file_cleanup.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        # print('Copying and moving files')


        # *******************************************************************************
        # Read polygon shapefile
        # *******************************************************************************

        print('Read polygon shapefile')
        gbyos_pol_lay = fiona.open(pol_shp, 'r')
        IS_pol_tot = len(gbyos_pol_lay)
        print(' - The number of polygon features is: ' + str(IS_pol_tot))

        # *******************************************************************************
        # Create spatial index for the bounds of each polygon feature
        # *******************************************************************************
        index = rtree.index.Index()
        shp_bounds = []

        def explode(coords):
            """Explode a GeoJSON geometry's coordinates object and yield coordinate tuples.
            As long as the input is conforming, the type of the geometry doesn't matter."""
            for e in coords:
                if isinstance(e, (float, int, long)):
                    yield coords
                    break
                else:
                    for f in explode(e):
                        yield f

        def bbox(f):
            x, y = zip(*list(explode(f['geometry']['coordinates'])))
            return min(x), min(y), max(x), max(y)

        for gbyos_pol_fea in gbyos_pol_lay:
            gbyos_pol_fid = int(gbyos_pol_fea['id'])
            # the first argument of index.insert has to be 'int', not 'long' or 'str'
            gbyos_pol_shy = shapely.geometry.shape(gbyos_pol_fea['geometry'])
            index.insert(gbyos_pol_fid, gbyos_pol_shy.bounds)
            shp_bounds.append(gbyos_pol_shy.bounds)
            bbox_val = bbox(gbyos_pol_fea)
            # creates an index between the feature ID and the bounds of that feature

        # *******************************************************************************
        # Add Region to Persistent Store DB
        # *******************************************************************************


        # Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        # session = Session()
        # region = Region(thredds_id=thredds_id,display_name=display_name, latlon_bbox=str(bbox_val))
        # session.add(region)
        # session.commit()
        # session.close()
        #
        # for the_file in os.listdir(SHP_DIR):
        #     file_path = os.path.join(SHP_DIR, the_file)
        #     try:
        #         if os.path.isfile(file_path):
        #             os.unlink(file_path)
        #         #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        #     except Exception as e:
        #         print(e)

        return JsonResponse({"success": "success"})


###############################################

def sub_initial(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]




        os.system(SHELL_DIR+'subset_initial.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting Region Bounds')

        return JsonResponse({"initial": "initial"})





def sub_jpl_tot(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR

        SHP_DIR = os.path.join(SHP_DIR, '')

        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_jpl_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting JPL Total Storage')


        return JsonResponse({"jpl_tot": "jpl_tot"})


def sub_jpl_gw(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_jpl_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting JPL Groundwater Storage')

        return JsonResponse({"jpl_gw": "jpl_gw"})





def sub_csr_tot(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_csr_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting CSR Total Water Storage')

        return JsonResponse({"csr_tot": "csr_tot"})

def sub_csr_gw(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_csr_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting CSR Groundwater Storage')

        return JsonResponse({"csr_gw": "csr_gw"})

def sub_gfz_tot(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_gfz_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting GFZ Total Water Storage')

        return JsonResponse({"gfz_tot": "gfz_tot"})

def sub_gfz_gw(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_gfz_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting GFZ Groundwater Storage')

        return JsonResponse({"gfz_gw": "gfz_gw"})

def sub_avg_tot(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_avg_tot.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting AVG Total Storage')

        return JsonResponse({"avg_tot": "avg_tot"})

def sub_avg_gw(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_avg_gw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting AVG Groundwater Storage')

        return JsonResponse({"avg_gw": "avg_gw"})






def sub_sw(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_sw.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting Surface Water Storage')

        return JsonResponse({"sw": "sw"})

def sub_soil(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'subset_soil.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Subsetting Soil Moisture Storage')

        return JsonResponse({"soil": "soil"})

def sub_file_cleanup(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR


        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        os.system(SHELL_DIR+'file_cleanup.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)
        print('Copying and moving files')

        return JsonResponse({"cleanup": "cleanup"})

def sub_update_ps(shapefile,region_name,GLOBAL_DIR,display_name,thredds_id):

        SHP_DIR = SHAPE_DIR

        SHP_DIR = os.path.join(SHP_DIR, '')

        temp_dir = tempfile.mkdtemp()
        for f in shapefile:
            f_name = f.name
            f_path = os.path.join(SHP_DIR, f_name)

            with open(f_path, 'wb') as f_local:
                f_local.write(f.read())

        for file in os.listdir(SHP_DIR):
            # Reading the shapefile only
            if file.endswith(".shp"):
                f_path = os.path.join(SHP_DIR, file)
                pol_shp = f_path
                pol_name = os.path.splitext(f_name)[0]


        # *******************************************************************************
        # Read polygon shapefile
        # *******************************************************************************

        print('Read polygon shapefile')
        gbyos_pol_lay = fiona.open(pol_shp, 'r')
        IS_pol_tot = len(gbyos_pol_lay)
        print(' - The number of polygon features is: ' + str(IS_pol_tot))

        # *******************************************************************************
        # Create spatial index for the bounds of each polygon feature
        # *******************************************************************************
        index = rtree.index.Index()
        shp_bounds = []

        def explode(coords):
            """Explode a GeoJSON geometry's coordinates object and yield coordinate tuples.
            As long as the input is conforming, the type of the geometry doesn't matter."""
            for e in coords:
                if isinstance(e, (float, int, long)):
                    yield coords
                    break
                else:
                    for f in explode(e):
                        yield f

        def bbox(f):
            x, y = zip(*list(explode(f['geometry']['coordinates'])))
            return min(x), min(y), max(x), max(y)

        for gbyos_pol_fea in gbyos_pol_lay:
            gbyos_pol_fid = int(gbyos_pol_fea['id'])
            # the first argument of index.insert has to be 'int', not 'long' or 'str'
            gbyos_pol_shy = shapely.geometry.shape(gbyos_pol_fea['geometry'])
            index.insert(gbyos_pol_fid, gbyos_pol_shy.bounds)
            shp_bounds.append(gbyos_pol_shy.bounds)
            bbox_val = bbox(gbyos_pol_fea)
            # creates an index between the feature ID and the bounds of that feature

        # *******************************************************************************
        # Add Region to Persistent Store DB
        # *******************************************************************************


        Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
        session = Session()
        region = Region(thredds_id=thredds_id,display_name=display_name, latlon_bbox=str(bbox_val))
        session.add(region)
        session.commit()
        session.close()

        for the_file in os.listdir(SHP_DIR):
            file_path = os.path.join(SHP_DIR, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                #elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

        return JsonResponse({"success": "success"})

