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

        print(SHP_DIR)
        print(GLOBAL_DIR)


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
        os.system(SHELL_DIR+'grace2subset.sh '+region_name+' '+GLOBAL_DIR+' '+pol_name+' '+pol_shp)


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



