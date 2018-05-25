from tethys_sdk.base import TethysAppBase, url_map_maker


class Newgrace(TethysAppBase):
    """
    Tethys app class for Newgrace.
    """

    name = 'Newgrace'
    index = 'newgrace:home'
    icon = 'newgrace/images/logo.jpg'
    package = 'newgrace'
    root_url = 'newgrace'
    color = '#27AE60'
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
                name='global_map',
                url='global_map',
                controller='newgrace.controllers.global_map'
            ),
            UrlMap(
                name='region',
                url='region',
                controller='newgrace.controllers.region'
            ),
        )

        return url_maps
