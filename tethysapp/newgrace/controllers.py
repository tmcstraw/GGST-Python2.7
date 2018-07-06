from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from tethys_sdk.gizmos import *
from .app import *
from model import *
from utilities import *

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    Session = Newgrace.get_persistent_store_database('grace_db',as_sessionmaker=True)
    session = Session()
    # Query DB for regions
    regions = session.query(Region).all()
    region_list = []

    for region in regions:
        region_list.append(("%s" % (region.display_name), region.id))

    session.close()
    if region_list:
        region_select = SelectInput(display_text='Select a Region',
                                    name='region-select',
                                    options=region_list, )
    else:
        region_select = None

    context = {
        "region_select": region_select, "regions_length": len(region_list), 'host': 'http://%s' % request.get_host()
    }

    return render(request, 'newgrace/home.html', context)

def api(request):

    context = {'host': 'http://%s' % request.get_host()}

    return render(request, 'grace/api.html', context)

@login_required()
def global_map(request):
    """
    Controller for the app home page.
    """


    grace_layer_options = get_global_dates()


    select_signal_process = SelectInput(display_text='Select Signal Processing Method',
                                    name = 'select_signal_process',
                                    multiple=False,
                                    options= [('JPL Solution', "jpl"), ('CSR Solution', "csr"), ('GFZ Solution', "gfz"), ('Ensemble Avg of JPL, CSR, & GFZ', "avg")],
                                    initial=['JPL Solution']
                                    )

    select_layer = SelectInput(display_text='Select a day',
                               name='select_layer',
                               multiple=False,
                               options=grace_layer_options, )

    select_storage_type = SelectInput(display_text='Select Storage Component',
                                      name='select_storage_type',
                                      multiple=False,
                                      options=[('Total Water Storage (GRACE)', "tot"),
                                               ('Surface Water Storage (GLDAS)', "sw"),
                                               ('Soil Moisture Storage (GLDAS)', "soil"),
                                               ('Groundwater Storage (Calculated)', "gw")
                                               ],
                                      initial=['Total Water Storage (GRACE)']
                                      )

    select_legend = SelectInput(display_text='Select Symbology',
                                      name='select_legend',
                                      multiple=False,
                                      options=[('Grace',"grace"),
                                               ('Blue-red',"bluered"),
                                               ('Red-blue', "redblue"),
                                               ('Rainbow', "rainbow"),
                                               ('Occam', "occam"),
                                               ('ncview',"ncview"),
                                               ('sst_36',"sst_36"),
                                               ('greyscale', "greyscale"),
                                               ('alg2', "alg2"),
                                               ('occam_pastel-30', "occam_pastel-30"),
                                               ('alg', "alg"),
                                               ('ferret', "ferret")
                                               ],
                                      initial=['']
                                      )

    context = {
        "select_storage_type":select_storage_type,
        "select_legend":select_legend,
        'select_layer':select_layer,
        "select_signal_process":select_signal_process
    }

    return render(request, 'newgrace/global_map.html', context)

@login_required()
def region(request):
    """
    Controller for the app home page.
    """
    context = {}

    info = request.GET

    region_id = info.get('region-select')
    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()

    region = session.query(Region).get(region_id)
    display_name = region.display_name

    bbox = [float(x) for x in region.latlon_bbox.strip("(").strip(")").split(',')]
    json.dumps(bbox)

    regions = session.query(Region).all()
    region_list = []

    for reg in regions:
        region_list.append(("%s" % (reg.display_name), reg.id))

    session.close()

    if region_list:
        select_region = SelectInput(display_text='Select a Region',
                                    name='region-select',
                                    multiple=False,
                                    options=[('California','california'),('Bangladesh','bangladesh')],
                                    )
    else:
        select_region = None


    grace_layer_options = get_global_dates()

    select_signal_process = SelectInput(display_text='Select Signal Processing Method',
                                    name = 'select_signal_process',
                                    multiple=False,
                                    options= [('JPL Solution', "jpl"), ('CSR Solution', "csr"), ('GFZ Solution', "gfz"), ('Ensemble Avg of JPL, CSR, & GFZ', "avg")],
                                    initial=['JPL Solution']
                                    )

    select_layer = SelectInput(display_text='Select a day',
                               name='select_layer',
                               multiple=False,
                               options=grace_layer_options, )
    select_storage_type = SelectInput(display_text='Select Storage Component',
                                      name='select_storage_type',
                                      multiple=False,
                                      options=[('Total Water Storage (GRACE)',"tot"),
                                               ('Surface Water Storage (GLDAS)',"sw"),
                                               ('Soil Moisture Storage (GLDAS)',"soil"),
                                               ('Groundwater Storage (Calculated)',"gw")],
                                      initial=['Total Water Storage (GRACE)']
                                      )
    select_legend = SelectInput(display_text='Select Symbology',
                                      name='select_legend',
                                      multiple=False,
                                      options=[('Grace',"grace"),('Blue-red',"bluered"),('Red-blue', "redblue"), ('Rainbow',
                                                          "rainbow"),
                                               (
                                                   'Occam',
                                                   "occam"), (
                                                   'ncview',
                                                   "ncview"),
                                               ('sst_36',
                                                "sst_36"),
                                               ('greyscale',"greyscale"),
                                               ('alg2',"alg2"),
                                               ('occam_pastel-30',"occam_pastel-30"),
                                               ('alg',"alg"),
                                               ('ferret',"ferret")
                                               ],
                                      initial=['']
                                      )


    if bbox[0] < 0 and bbox[2] < 0:
        map_center = [(int(bbox[1])+int(bbox[3])) / 2, ( (360+(int(bbox[0])))+(360+(int(bbox[2])))) / 2]
    else:
        map_center = [(int(bbox[1]) + int(bbox[3])) / 2, (int(bbox[0]) + int(bbox[2])) / 2]
    json.dumps(map_center)


    context = {"region_id":region_id,
               "display_name":display_name,
               "select_layer":select_layer,
               "bbox":bbox,
               "map_center":map_center,
               "select_signal_process":select_signal_process,
                "select_storage_type":select_storage_type,
                "select_legend":select_legend,
                "select_region":select_region
    }

    return render(request, 'newgrace/region.html', context)


@user_passes_test(user_permission_test)
def add_region(request):

    region_name_input = TextInput(display_text='Region Display Name',
                                     name='region-name-input',
                                     placeholder='e.g.: Utah',
                                     icon_append='glyphicon glyphicon-home',
                                     ) #Input for the Region Display Name

    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()
    # Query DB for geoservers
    thredds_servers = session.query(Thredds).all()
    thredds_list = []
    for thredds in thredds_servers:
        thredds_list.append(( "%s (%s)" % (thredds.name, thredds.url),
                               thredds.id))

    session.close()
    if thredds_list:
        thredds_select = SelectInput(display_text='Select a Thredds server',
                                       name='thredds-select',
                                       options=thredds_list)
    else:
        thredds_select = None

    add_button = Button(display_text='Add Region',
                        icon='glyphicon glyphicon-plus',
                        style='success',
                        name='submit-add-region',
                        attributes={'id': 'submit-add-region'}, )  # Add region button

    context = {"region_name_input":region_name_input, "thredds_select":thredds_select,"add_button":add_button}

    return render(request, 'newgrace/add_region.html', context)


@user_passes_test(user_permission_test)
def add_thredds_server(request):
    """
        Controller for the app add_geoserver page.
    """

    thredds_name_input = TextInput(display_text='Thredds Server Name',
                                     name='thredds-name-input',
                                     placeholder='e.g.: BYU Thredds Server',
                                     icon_append='glyphicon glyphicon-tag', )

    thredds_url_input = TextInput(display_text='Thredds Server REST Url',
                                    name='thredds-url-input',
                                    placeholder='e.g.: http://localhost:9090/thredds/',
                                    icon_append='glyphicon glyphicon-cloud-download')

    thredds_username_input = TextInput(display_text='Thredds Server Username',
                                         name='thredds-username-input',
                                         placeholder='e.g.: admin',
                                         icon_append='glyphicon glyphicon-user', )

    add_button = Button(display_text='Add Thredds Server',
                        icon='glyphicon glyphicon-plus',
                        style='success',
                        name='submit-add-thredds-server',
                        attributes={'id': 'submit-add-thredds-server'}, )

    context = {
        'thredds_name_input': thredds_name_input,
        'thredds_url_input': thredds_url_input,
        'thredds_username_input': thredds_username_input,
        'add_button': add_button,
    }

    return render(request, 'newgrace/add_thredds_server.html', context)

@user_passes_test(user_permission_test)
def manage_regions(request):
    """
    Controller for the app manage_geoservers page.
    """
    #initialize session
    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()
    num_regions = session.query(Region).count()

    session.close()

    context = {
                'initial_page': 0,
                'num_regions': num_regions,
              }

    return render(request, 'newgrace/manage_regions.html', context)

@user_passes_test(user_permission_test)
def manage_regions_table(request):
    """
    Controller for the app manage_geoservers page.
    """
    #initialize session
    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()
    RESULTS_PER_PAGE = 5
    page = int(request.GET.get('page'))

    # Query DB for data store types
    regions = session.query(Region)\
                        .order_by(Region.display_name) \
                        .all()[(page * RESULTS_PER_PAGE):((page + 1)*RESULTS_PER_PAGE)]

    prev_button = Button(display_text='Previous',
                         name='prev_button',
                         attributes={'class':'nav_button'},)

    next_button = Button(display_text='Next',
                         name='next_button',
                         attributes={'class':'nav_button'},)

    context = {
                'prev_button' : prev_button,
                'next_button': next_button,
                'regions': regions,
              }

    session.close()

    return render(request, 'newgrace/manage_regions_table.html', context)

@user_passes_test(user_permission_test)
def manage_thredds_servers(request):
    """
    Controller for the app manage_geoservers page.
    """
    #initialize session
    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()
    num_thredds_servers = session.query(Thredds).count()
    session.close()

    context = {
                'initial_page': 0,
                'num_thredds_servers': num_thredds_servers,
              }

    return render(request, 'newgrace/manage_thredds_servers.html', context)

@user_passes_test(user_permission_test)
def manage_thredds_servers_table(request):
    """
    Controller for the app manage_geoservers page.
    """
    #initialize session
    Session = Newgrace.get_persistent_store_database('grace_db', as_sessionmaker=True)
    session = Session()
    RESULTS_PER_PAGE = 5
    page = int(request.GET.get('page'))

    # Query DB for data store types
    thredds_servers = session.query(Thredds)\
                        .order_by(Thredds.name, Thredds.url) \
                        .all()[(page * RESULTS_PER_PAGE):((page + 1)*RESULTS_PER_PAGE)]

    prev_button = Button(display_text='Previous',
                         name='prev_button',
                         attributes={'class':'nav_button'},)

    next_button = Button(display_text='Next',
                         name='next_button',
                         attributes={'class':'nav_button'},)

    context = {
                'prev_button' : prev_button,
                'next_button': next_button,
                'thredds_servers': thredds_servers,
              }

    session.close()

    return render(request, 'newgrace/manage_thredds_servers_table.html', context)
