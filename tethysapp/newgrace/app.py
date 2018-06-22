from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class Newgrace(TethysAppBase):
    """
    Tethys app class for Newgrace.
    """

    name = 'GRACE 2.0'
    index = 'newgrace:home'
    icon = 'newgrace/images/logo.jpg'
    package = 'newgrace'
    root_url = 'newgrace'
    color = '#222222'
    description = 'The GRACE application is a visualization tool for GRACE global satellite data. It also provides visualization for global surface water, soil moisture, and groundwater data.'
    tags = '&quot;Hydrology&quot;, &quot;Groundwater&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='newgrace',
                controller='newgrace.controllers.home'
            ),
            UrlMap(
                name='global-map',
                url='global-map',
                controller='newgrace.controllers.global_map'
            ),
            UrlMap(
                name='region',
                url='region',
                controller='newgrace.controllers.region'
            ),
            UrlMap(
                name='add-region',
                url='add-region',
                controller='newgrace.controllers.add_region'
            ),
            UrlMap(name='add-region-ajax',
                   url='newgrace/add-region/submit',
                   controller='newgrace.ajax_controllers.region_add'
            ),
            UrlMap(
                name='add-thredds-server',
                url='add-thredds-server',
                controller='newgrace.controllers.add_thredds_server'
            ),
            UrlMap(name='add-thredds-server-ajax',
                   url='newgrace/add-thredds-server/submit',
                   controller='newgrace.ajax_controllers.thredds_server_add'
            ),
            UrlMap(name='update-thredds-servers-ajax',
                   url='newgrace/manage-thredds-servers/submit',
                   controller='newgrace.ajax_controllers.thredds_server_update'
            ),
            UrlMap(name='delete-thredds-server-ajax',
                   url='newgrace/manage-thredds-servers/delete',
                   controller='newgrace.ajax_controllers.thredds_server_delete'
            ),
            UrlMap(
                name='manage-regions',
                url='manage-regions',
                controller='newgrace.controllers.manage_regions'
            ),
            UrlMap(name='manage-regions-table',
                   url='newgrace/manage-regions/table',
                   controller='newgrace.controllers.manage_regions_table'
            ),
            UrlMap(name='delete-regions-ajax',
                   url='newgrace/manage-regions/delete',
                   controller='newgrace.ajax_controllers.region_delete'
            ),
            UrlMap(
                name='manage-thredds-servers',
                url='manage-thredds-servers',
                controller='newgrace.controllers.manage_thredds_servers'
            ),
            UrlMap(name='manage-thredds-servers-table',
                   url='newgrace/manage-thredds-servers/table',
                   controller='newgrace.controllers.manage_thredds_servers_table'
            ),
            UrlMap(name='api_get_point_values',
                   url='newgrace/api/GetPointValues',
                   controller='newgrace.api.api_get_point_values'),
        )

        return url_maps

    def persistent_store_settings(self):

        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='grace_db',
                description='For storing Region and Thredds metadata',
                required=True,
                initializer='newgrace.model.init_grace_db',
                spatial=False,
            ),
        )

        return ps_settings
