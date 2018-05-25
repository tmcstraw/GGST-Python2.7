from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button, SelectInput

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    save_button = Button(
        display_text='',
        name='save-button',
        icon='glyphicon glyphicon-floppy-disk',
        style='success',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Save'
        }
    )

    edit_button = Button(
        display_text='',
        name='edit-button',
        icon='glyphicon glyphicon-edit',
        style='warning',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Edit'
        }
    )

    remove_button = Button(
        display_text='',
        name='remove-button',
        icon='glyphicon glyphicon-remove',
        style='danger',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Remove'
        }
    )

    previous_button = Button(
        display_text='Previous',
        name='previous-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Previous'
        }
    )

    next_button = Button(
        display_text='Next',
        name='next-button',
        attributes={
            'data-toggle':'tooltip',
            'data-placement':'top',
            'title':'Next'
        }
    )

    context = {
        'save_button': save_button,
        'edit_button': edit_button,
        'remove_button': remove_button,
        'previous_button': previous_button,
        'next_button': next_button
    }

    return render(request, 'newgrace/home.html', context)

@login_required()
def global_map(request):
    """
    Controller for the app home page.
    """
    select_storage_type = SelectInput(display_text='Select Storage Component',
                                      name='select_storage_type',
                                      multiple=False,
                                      options=[('',''),('Total Water Storage (GRACE)',
                                                "http://localhost:8080/thredds/wms/testAll/grace/GRC_tot.25scaled.nc"), (
                                               'Surface Water Storage (GLDAS)',
                                               "http://localhost:8080/thredds/wms/testAll/grace/GRC_SW.nc"), (
                                               'Soil Moisture Storage (GLDAS)',
                                               "http://localhost:8080/thredds/wms/testAll/grace/GRC_Soil_Moisture_Total_Anomaly.nc"),
                                               ('Groundwater Storage (Calculated)',
                                                "http://localhost:8080/thredds/wms/testAll/grace/GRC_gwtest.nc")],
                                      initial=['']
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

    context = {
        "select_storage_type":select_storage_type,
        "select_legend":select_legend

    }

    return render(request, 'newgrace/global_map.html', context)

@login_required()
def region(request):
    """
    Controller for the app home page.
    """
    select_region = SelectInput(display_text='Select Region',
                                    name='select_region',
                                    multiple=False,
                                    options=[('California',"California"),('Nepal',"Nepal"),('Texas',"Texas"),('La Plata',"LaPlata")]
                                )
    select_storage_type = SelectInput(display_text='Select Storage Component',
                                      name='select_storage_type',
                                      multiple=False,
                                      options=[('',''),('Total Water Storage (GRACE)',
                                                "GRC_tot.25scaled.nc"), (
                                               'Surface Water Storage (GLDAS)',
                                               "GRC_SW.nc"), (
                                               'Soil Moisture Storage (GLDAS)',
                                               "GRC_Soil_Moisture_Total_Anomaly.nc"),
                                               ('Groundwater Storage (Calculated)',
                                                "GRC_gwtest.nc")],
                                      initial=['']
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

    context = {
        "select_storage_type":select_storage_type,
        "select_legend":select_legend,
        "select_region":select_region
    }

    return render(request, 'newgrace/region.html', context)