var date_value = new Date($("#select_layer").find('option:selected').val());
var point_grp = L.layerGroup();
var map = L.map('map', {
    crs: L.CRS.EPSG4326,
    zoom: 1,
//    drawControl: true,
    fullscreenControl: true,
    timeDimension: true,
    timeDimensionOptions:{
    
			 times:"2002-04-16T00:00:00.000Z,2002-05-10T00:00:00.000Z,2002-08-16T12:00:00.000Z,2002-09-16T00:00:00.000Z,2002-10-16T12:00:00.000Z,2002-11-16T00:00:00.000Z,2002-12-16T12:00:00.000Z,2003-01-16T12:00:00.000Z,2003-02-15T00:00:00.000Z,2003-03-16T12:00:00.000Z,2003-04-16T00:00:00.000Z,2003-05-11T12:00:00.000Z,2003-07-16T12:00:00.000Z,2003-08-16T12:00:00.000Z,2003-09-16T00:00:00.000Z,2003-10-16T12:00:00.000Z,2003-11-16T00:00:00.000Z,2003-12-16T12:00:00.000Z,2004-01-07T12:00:00.000Z,2004-02-17T00:00:00.000Z,2004-03-16T12:00:00.000Z,2004-04-16T00:00:00.000Z,2004-05-16T12:00:00.000Z,2004-06-16T00:00:00.000Z,2004-07-16T12:00:00.000Z,2004-08-16T12:00:00.000Z,2004-09-16T00:00:00.000Z,2004-10-16T12:00:00.000Z,2004-11-16T00:00:00.000Z,2004-12-16T12:00:00.000Z,2005-01-16T12:00:00.000Z,2005-02-15T00:00:00.000Z,2005-03-16T12:00:00.000Z,2005-04-16T00:00:00.000Z,2005-05-16T12:00:00.000Z,2005-06-16T00:00:00.000Z,2005-07-16T12:00:00.000Z,2005-08-16T12:00:00.000Z,2005-09-16T00:00:00.000Z,2005-10-16T12:00:00.000Z,2005-11-16T00:00:00.000Z,2005-12-16T12:00:00.000Z,2006-01-16T12:00:00.000Z,2006-02-15T00:00:00.000Z,2006-03-16T12:00:00.000Z,2006-04-16T00:00:00.000Z,2006-05-16T12:00:00.000Z,2006-06-16T00:00:00.000Z,2006-07-16T12:00:00.000Z,2006-08-16T12:00:00.000Z,2006-09-16T00:00:00.000Z,2006-10-16T12:00:00.000Z,2006-11-16T00:00:00.000Z,2006-12-16T12:00:00.000Z,2007-01-16T12:00:00.000Z,2007-02-15T00:00:00.000Z,2007-03-16T12:00:00.000Z,2007-04-16T00:00:00.000Z,2007-05-16T12:00:00.000Z,2007-06-16T00:00:00.000Z,2007-07-16T12:00:00.000Z,2007-08-16T12:00:00.000Z,2007-09-16T00:00:00.000Z,2007-10-16T12:00:00.000Z,2007-11-16T00:00:00.000Z,2007-12-16T12:00:00.000Z,2008-01-16T12:00:00.000Z,2008-02-15T12:00:00.000Z,2008-03-16T12:00:00.000Z,2008-04-16T00:00:00.000Z,2008-05-16T12:00:00.000Z,2008-06-16T00:00:00.000Z,2008-07-16T12:00:00.000Z,2008-08-16T12:00:00.000Z,2008-09-16T00:00:00.000Z,2008-10-16T12:00:00.000Z,2008-11-16T00:00:00.000Z,2008-12-16T12:00:00.000Z,2009-01-16T12:00:00.000Z,2009-02-15T00:00:00.000Z,2009-03-16T12:00:00.000Z,2009-04-16T00:00:00.000Z,2009-05-16T12:00:00.000Z,2009-06-16T00:00:00.000Z,2009-07-16T12:00:00.000Z,2009-08-16T12:00:00.000Z,2009-09-16T00:00:00.000Z,2009-10-16T12:00:00.000Z,2009-11-16T00:00:00.000Z,2009-12-16T12:00:00.000Z,2010-01-16T12:00:00.000Z,2010-02-15T00:00:00.000Z,2010-03-16T12:00:00.000Z,2010-04-16T00:00:00.000Z,2010-05-16T12:00:00.000Z,2010-06-16T00:00:00.000Z,2010-07-16T12:00:00.000Z,2010-08-16T12:00:00.000Z,2010-09-16T00:00:00.000Z,2010-10-16T12:00:00.000Z,2010-11-16T00:00:00.000Z,2010-12-16T12:00:00.000Z,2011-02-18T12:00:00.000Z,2011-03-16T12:00:00.000Z,2011-04-16T00:00:00.000Z,2011-05-16T12:00:00.000Z,2011-07-19T12:00:00.000Z,2011-08-16T12:00:00.000Z,2011-09-16T00:00:00.000Z,2011-10-16T12:00:00.000Z,2011-11-01T12:00:00.000Z,2012-01-02T00:00:00.000Z,2012-01-16T12:00:00.000Z,2012-02-15T12:00:00.000Z,2012-03-16T12:00:00.000Z,2012-04-10T12:00:00.000Z,2012-06-16T00:00:00.000Z,2012-07-16T12:00:00.000Z,2012-08-16T12:00:00.000Z,2012-09-13T00:00:00.000Z,2012-11-20T00:00:00.000Z,2012-12-16T12:00:00.000Z,2013-01-16T12:00:00.000Z,2013-02-14T00:00:00.000Z,2013-04-21T12:00:00.000Z,2013-05-16T12:00:00.000Z,2013-06-16T00:00:00.000Z,2013-07-16T12:00:00.000Z,2013-10-16T12:00:00.000Z,2013-11-16T00:00:00.000Z,2013-12-16T12:00:00.000Z,2014-01-09T12:00:00.000Z,2014-03-17T12:00:00.000Z,2014-04-16T00:00:00.000Z,2014-05-16T12:00:00.000Z,2014-06-13T00:00:00.000Z,2014-08-16T12:00:00.000Z,2014-09-16T00:00:00.000Z,2014-10-16T12:00:00.000Z,2014-11-17T00:00:00.000Z,2015-01-22T12:00:00.000Z,2015-02-15T00:00:00.000Z,2015-03-16T12:00:00.000Z,2015-04-16T00:00:00.000Z,2015-04-27T00:00:00.000Z,2015-07-15T12:00:00.000Z,2015-08-16T12:00:00.000Z,2015-09-14T12:00:00.000Z,2015-12-23T00:00:00.000Z,2016-01-16T12:00:00.000Z,2016-02-14T00:00:00.000Z,2016-03-16T12:00:00.000Z,2016-05-20T12:00:00.000Z,2016-06-16T00:00:00.000Z,2016-07-15T12:00:00.000Z,2016-08-21T12:00:00.000Z",
             currentTime: Date.parse("2002-04-16T00:00:00.000Z"),
    },
    timeDimensionControl: true,
    timeDimensionControlOptions:{
                playerOptions:{
                        loop:true,
                        startover:true,
                }
    },
    center: [0.0, 0.0],
});

//var drawnItems = new L.FeatureGroup();
//map.addLayer(drawnItems);
//var drawPluginOptions = {
//    position: 'topleft',
//    draw: {
//        polygon: false,
//        polyline: false,
//        circle: false,
//        rectangle: false,
//        },
//    edit: {
//        featureGroup: drawnItems,
//        remove: false
//    }
//}
//var drawControl = new L.Control.Draw(drawPluginOptions).addTo(map);
////map.addControl(drawControl);
//
//var drawnItems = new L.FeatureGroup().addTo(map);
////map.addLayer(drawnItems);
//
//map.on('draw:created', function(e) {
//    var type = e.layerType,
//        layer = e.layer;
//
//    if (type === 'marker') {
//        layer.bindPopup('A popup!');
//        }
//    drawnItems.addLayer(layer);
//});

var wmsLayer = L.tileLayer.wms('https://demo.boundlessgeo.com/geoserver/ows?', {
    layers: 'nasa:bluemarble'
}).addTo(map);

//var date_value = $("#select_layer").find('option:selected').val();
var signal_process = $("#select_signal_process").find('option:selected').val();
var storage_type = $("#select_storage_type").find('option:selected').val();
var testWMS="https://tethys.byu.edu/thredds/wms/testAll/grace/GRC_"+signal_process+"_"+storage_type+".nc"
var testLayer = L.tileLayer.wms(testWMS, {
    layers: 'grace',
    layers:'lwe_thickness',
    format: 'image/png',
    transparent: true,
    opacity:0.7,
    style: 'boxfill/sst_36',
    colorscalerange:'-50,50',
    attribution: '<a href="https://www.pik-potsdam.de/">PIK</a>'
});



var testTimeLayer = L.timeDimension.layer.wms.timeseries(testLayer, {
//	proxy: proxy,
	updateTimeDimension: true,
    name: "Liquid Water Equivalent Thickness",
    units: "cm",
    enableNewMarkers: true
});
testTimeLayer.addTo(map);
    var testLegend = L.control({
    position: 'topright'
    });


function updateWMS(){

    map.removeLayer(testTimeLayer);
    var type=$("#select_legend").find('option:selected').val();
    var signal_process = $("#select_signal_process").find('option:selected').val();
    var storage_type = $("#select_storage_type").find('option:selected').val();
    var testWMS="https://tethys.byu.edu/thredds/wms/testAll/grace/GRC_"+signal_process+"_"+storage_type+".nc"
    var date_value = new Date($("#select_layer").find('option:selected').val());
    var colormin = $("#col_min").val();
    var colormax = $("#col_max").val();
    var opac = $("#opacity_val").val();


    teststyle='boxfill/'+type;
    testLayer = L.tileLayer.wms(testWMS, {
        layers:'lwe_thickness',
        format: 'image/png',
        transparent: true,
        opacity:opac,
        styles: teststyle,
        colorscalerange:colormin+','+colormax,
        attribution: '<a href="https://www.pik-potsdam.de/">PIK</a>'
    });


    testTimeLayer = L.timeDimension.layer.wms.timeseries(testLayer, {
	    //proxy: proxy,
	    updateTimeDimension: true,
    	name: "Liquid Water Equivalent Thickness (cm)",
    	units: "cm",
    	enableNewMarkers: true,
    });



    testTimeLayer.addTo(map);
    testLegend.onAdd= function(map) {

        var src=testWMS+"?REQUEST=GetLegendGraphic&LAYER=lwe_thickness&PALETTE="+type+"&COLORSCALERANGE="+colormin+","+colormax;
        var div = L.DomUtil.create('div', 'info legend');
        div.innerHTML +=
            '<img src="' + src + '" alt="legend">';
        return div;
    };
    testLegend.addTo(map);
    map.timeDimension.setCurrentTime(date_value);
};

function pointPlot(){
    L.TimeDimension.Layer.WMS.prototype.onAdd.call(this, map);
};


function getInstructions() {
    var x = document.getElementById("ts-instructions");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
};




L.TimeDimension.Layer.WMS.TimeSeries = L.TimeDimension.Layer.WMS.extend({

    initialize: function(layer, options) {
        this._markers = options.markers || [];
        this._markerColors = options.markerColors || ["#2f7ed8", "#0d233a", "#8bbc21", "#910000", "#1aadce", "#492970", "#f28f43", "#77a1e5", "#c42525", "#a6c96a"];
        this._name = options.name || "";
        this._defaultRangeSelector = options.defaultRangeSelector || 6;
        this._enableNewMarkers = options.enableNewMarkers || false;
        this._chartOptions = options.chartOptions || {};

        this._currentMarkerColor = 0;

        L.TimeDimension.Layer.WMS.prototype.initialize.call(this, layer, options);
        if (options.units) {
            this._units = options.units;
        } else {
            this._loadUnits();
        }
        this._circleLabelMarkers = [];
    },

    onAdd: function(map) {
        if (this._enableNewMarkers && this._enabledNewMarkers === undefined) {
            this._enabledNewMarkers = true;
            map.doubleClickZoom.disable();
            map.on('dblclick', (function(e) {

                // e.originalEvent.preventDefault();

                // option to remove chart for each new point clicked
//          if ($("#select_storage_type").find('option:selected').val()=="http://localhost:8080/thredds/wms/testAll/grace/GRC_tot.25scaled.nc"){

          if (this._chart){
              this._chart.destroy();
              delete this._chart;

          }
                // end option

                this.addPositionMarker({
                    position: [e.latlng.lat, e.latlng.lng]
                });

                return false;
            }).bind(this));


        }
	this._timeDimension = map.timeDimension;
        this._setDateRanges(); //I added this line
        if (this._dateRange !== undefined) {
            this._addMarkers();
        }
        return L.TimeDimension.Layer.WMS.prototype.onAdd.call(this, map);
    },

    eachLayer: function(method, context) {
        for (var i = 0, l = this._circleLabelMarkers.length; i < l; i++) {
            method.call(context, this._circleLabelMarkers[i]);
        }
        return L.TimeDimension.Layer.WMS.prototype.eachLayer.call(this, method, context);
    },

    onRemove: function(map){
        if (this._chart){
            this._chart.destroy();
            delete this._chart;
        }
        return L.TimeDimension.Layer.WMS.prototype.onRemove.call(this, map);
    },


    // we need to overwrite this function, which is called when the layer has availabletimes loaded,
    // in order to initialize dates ranges (current min-max and layer min-max date ranges) and after that
    // add the default markers to the map
    _updateTimeDimensionAvailableTimes: function() {
        L.TimeDimension.Layer.WMS.prototype._updateTimeDimensionAvailableTimes.call(this);
        if (this._dateRange === undefined) {
            this._setDateRanges();
            this._addMarkers();
        }
    },

    _getNextMarkerColor: function() {
        return this._markerColors[this._currentMarkerColor++ % this._markerColors.length];
    },

    _addMarkers: function() {
        for (var i = 0, l = this._markers.length; i < l; i++) {
            this.addPositionMarker(this._markers[i]);
        }
    },

    addPositionMarker: function(point) {
        if (!this._map) {
            return;
        }
        var point_grp = L.layerGroup().addTo(this._map)

        var color = this._getNextMarkerColor();
        var circle = L.circleMarker([point.position[0], point.position[1]], {
            color: '#FFFFFF',
            fillColor: color,
            fillOpacity: 0.8,
            radius: 5,
            weight: 2
        });
        point_grp.addLayer(circle)
//        }).addTo(this._map);

        var afterLoadData = function(color, data) {
            var serie = this._showData(color, data, point.name);
            var marker = L.timeDimension.layer.circleLabelMarker(circle, {
                serieId: serie,
                dataLayer: this._currentLayer,
                proxy: this._proxy
            })
            this._circleLabelMarkers.push(marker);
            marker.addTo(this._map);
            if (this._chart) {
                this._chart.hideLoading();
            }

        };
        if (this._chart) {
            this._chart.showLoading();
        }
        // display all four variables on the time series plot if the Total Water Storage is selected
        if(this._baseLayer.getURL()=="http://localhost:8080/thredds/wms/testAll/grace/GRC_tot.25scaled.nc"){
            this._loadData(circle.getLatLng(),1, afterLoadData.bind(this, "#000099")); //total
            this._loadData(circle.getLatLng(),2, afterLoadData.bind(this, "#02f2ff")); //surface
            this._loadData(circle.getLatLng(),3, afterLoadData.bind(this, "#007a10")); //soil moisture
            this._loadData(circle.getLatLng(),4, afterLoadData.bind(this, "#88523f")); //groundwater
        }
        else{
        this._loadData(circle.getLatLng(),0, afterLoadData.bind(this, color)); //regular
        }


    },

    _loadData: function(latlng,doall, callback) {
        var min = new Date(this._getNearestTime(this._currentDateRange.min.getTime()));
        var max = new Date(this._getNearestTime(this._currentDateRange.max.getTime()));

        var point = this._map.latLngToContainerPoint(latlng);
        if(doall==0){
            var url = this._baseLayer.getURL() + '?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84';
	    }
	    if(doall==1){
	    //total water
	        var url="http://localhost:8080/thredds/wms/testAll/grace/GRC_tot.25scaled.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	    }
	    if(doall==2){
	    //surface water
	        var url="http://localhost:8080/thredds/wms/testAll/grace/GRC_SW.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	        }
	    if(doall==3){
	        //soil moisture
	        var url="http://localhost:8080/thredds/wms/testAll/grace/GRC_Soil_Moisture_Total_Anomaly.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	    }
	    if(doall==4){
	        //groundwater
	        var url="http://localhost:8080/thredds/wms/testAll/grace/GRC_gwtest.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	        }
        url = url + '&LAYER=' + this._baseLayer.options.layers;
        url = url + '&QUERY_LAYERS=' + this._baseLayer.options.layers;
        url = url + '&X=' + point.x + '&Y=' + point.y + '&I=' + point.x + '&J=' + point.y;
        var size = this._map.getSize();
        url = url + '&BBox=' + this._map.getBounds().toBBoxString();
        url = url + '&WIDTH=' + size.x + '&HEIGHT=' + size.y;
        url = url + '&INFO_FORMAT=text/xml';
        var url_without_time = url;

        url = url + '&TIME=' + min.toISOString() + '/' + max.toISOString();

        if (this._proxy) url = this._proxy + '?url=' + encodeURIComponent(url);

        var oReq = new XMLHttpRequest();
        oReq.addEventListener("load", (function(xhr) {
            var data = xhr.currentTarget.responseXML;
            var result = {
                time: [],
                values: []
            };
            // Add min and max values to be able to get more data later
            if (this._currentDateRange.min > this._dateRange.min) {
                result.time.push(this._dateRange.min);
                result.values.push(null);
            }
            data.querySelectorAll('FeatureInfo').forEach(function(fi) {
                var this_time = fi.querySelector('time').textContent;
                var this_data = fi.querySelector('value').textContent;
                try {
                    this_data = parseFloat(this_data);
                } catch (e) {
                    this_data = null;
                }
                result.time.push(this_time);
                result.values.push(this_data);
            });

            if (this._currentDateRange.max < this._dateRange.max) {
                result.time.push(this._dateRange.max);
                result.values.push(null);
            }

            result.longitude = data.querySelector('longitude').textContent;
            try {
                result.longitude = parseFloat(result.longitude).toFixed(4);
            } catch (e) {}
            result.latitude = data.querySelector('latitude').textContent;
            try {
                result.latitude = parseFloat(result.latitude).toFixed(4);
            } catch (e) {}

            result.url = url_without_time;

            if (callback !== undefined) {
                callback(result);
            }
        }).bind(this));
        oReq.overrideMimeType('application/xml');
        oReq.open("GET", url);
        oReq.send();
    },

    _checkLoadNewData: function(min, max) {
        min = new Date(min);
        max = new Date(max);

        var afterLoadData = (function(serie, data) {
            if (data !== undefined)
                this._updateSerie(serie, data.time, data.values);
            this._chart.hideLoading();
        }).bind(this);
        var i, l, serie;

        min = new Date(this._getNearestTime(min.getTime()));
        max = new Date(this._getNearestTime(max.getTime()));

        if (min < this._currentDateRange.min) {
            var old_min = this._currentDateRange.min;
            this._currentDateRange.min = min;
            this._chart.showLoading();
            for (i = 0, l = this._chart.series.length; i < l; i++) {
                serie = this._chart.series[i];
                if (serie.name != "Navigator")
                    this._loadMoreData(serie.options.custom.url, min, old_min, afterLoadData.bind(this, serie));
            }
        }
        if (max > this._currentDateRange.max) {
            var old_max = this._currentDateRange.max;
            this._currentDateRange.max = max;
            this._chart.showLoading();
            for (i = 0, l = this._chart.series.length; i < l; i++) {
                serie = this._chart.series[i];
                if (serie.name != "Navigator")
                    this._loadMoreData(serie.options.custom.url, old_max, max, afterLoadData.bind(this, serie));
            }
        }
    },

    _setDateRanges: function() {
        if (!this._timeDimension) {
            return;
        }
        var times = this._timeDimension.getAvailableTimes();
        if (times.length == 0){
            return;
        }
        this._dateRange = {
            min: new Date(times[0]),
            max: new Date(times[times.length - 1])
        };
        var max = this._dateRange.max;
        // check if max is a valid date
        if (!max.getTime || isNaN(max.getTime())) {
            return;
        }
        var min = this._dateRange.min;

        if (min < this._dateRange.min) {
            min = this._dateRange.min;
        }

        this._currentDateRange = {
            min: min,
            max: max
        };
    },

    _loadUnits: function() {
        var url = this._baseLayer.getURL() + '?service=WMS&version=1.3.0&request=GetMetadata&item=layerDetails';
        url = url + '&layerName=' + this._baseLayer.options.layers;
        if (this._proxy) url = this._proxy + '?url=' + encodeURIComponent(url);
        var oReq = new XMLHttpRequest();
        oReq.addEventListener("load", (function(xhr) {
            var response = xhr.currentTarget.response;
            var data = JSON.parse(response);
            this._units = data.units;
        }).bind(this));
        oReq.open("GET", url);
        oReq.send();
    },

    _createChart: function() {
        var mapContainerParent = this._map.getContainer().parentNode;
        var chart_wrapper = mapContainerParent.querySelector('.chart-wrapper');
        if (!chart_wrapper) {
            var wrapper = document.createElement("div");
            wrapper.setAttribute("class", "chart-wrapper");
            mapContainerParent.appendChild(wrapper);
            chart_wrapper = mapContainerParent.querySelector('.chart-wrapper');
        }
        var chart_container = chart_wrapper.querySelector('.chart-' + this._baseLayer.options.layers);
        if (!chart_container) {
            var container = document.createElement("div");
            container.setAttribute("class", "chart chart-" + this._baseLayer.options.layers);
            chart_wrapper.appendChild(container);
            chart_container = chart_wrapper.querySelector('.chart-' + this._baseLayer.options.layers);
        }
        var options = {
            legend: {
                enabled: true
            },

            chart: {
                zoomType: 'x'
            },
            rangeSelector: {
                selected: this._defaultRangeSelector,
                buttons: [{

                    type: 'all',
                    text: 'All'
                }]
            },
            xAxis: {
                events: {
                    afterSetExtremes: (function(e) {
                        this._checkLoadNewData(e.min, e.max);
                    }).bind(this)
                },
                plotLines: [{
                    color: 'red',
                    dashStyle: 'solid',
                    value: new Date(this._timeDimension.getCurrentTime()),
                    width: 2,
                    id: 'pbCurrentTime'
                }]
            },
            title: {
                text: this._name
            },
            series: [],
            plotOptions: {
                series: {
                    cursor: 'pointer',
                    point: {
                        events: {
                            click: (function(event) {
                                var day = new Date(event.point.x);
                                this._timeDimension.setCurrentTime(day.getTime());
                            }).bind(this)
                        }
                    }
                }
            }
        };



        var combinedHighChartsOptions = {};
        for (var attrname in options) { combinedHighChartsOptions[attrname] = options[attrname]; }
        for (var attrname in this._chartOptions) { combinedHighChartsOptions[attrname] = this._chartOptions[attrname]; }

        this._chart = Highcharts.stockChart(chart_container, combinedHighChartsOptions);
        this._timeDimension.on('timeload', (function(data) {
            if (!this._chart){
                return;
            }
            this._chart.xAxis[0].removePlotBand("pbCurrentTime");
            this._chart.xAxis[0].addPlotLine({
                color: 'red',
                dashStyle: 'solid',
                value: new Date(this._timeDimension.getCurrentTime()),
                width: 2,
                id: 'pbCurrentTime'
            });
        }).bind(this));

        return this._chart;
    },

    _showData: function(color, data, positionName) {
        var position = data.latitude + ', ' + data.longitude;
        if (positionName !== undefined) {
            position = positionName;
        }
        return this._addSerie(data.time, data.values, position, data.url, color);
    },

    _addSerie: function(time, variableData, position, url, color) {
        var serie = this._createSerie(time, variableData, position, url, color);
        if (!this._chart){
            this._createChart();
        }
        this._chart.addSeries(serie);
        return serie.id;
    },

    _createSerie: function(time, variableData, position, url, color) {
        return {
            name: (function(){
                var name='';
                if (color=="#000099"){
                    name="Total Water Storage Anomaly (cm) at " + position;
                }
                else if(color=="#02f2ff"){
                    name="Surface Water Storage (cm) at " + position;
                }
                else if(color=="#007a10"){
                    name="Soil Moisture Storage Anomaly (cm) at " + position;
                }
                else if(color=="#88523f"){
                    name="Groundwater Storage Anomaly (cm) at " + position;
                }
                else{
                    name='Liquid Water Equivalent Thickness at ' + position;
                }
                return name;
                })(),
            //this._name + ' at ' + position,
            type: 'area',
            id: Math.random().toString(36).substring(7),
            color: color,
            data: (function() {
                var length = time.length;
                var data = new Array(length);
                var this_time = new Date();
                var this_data = null;
                for (var i = 0; i < length; i++) {
                    this_time = (new Date(time[i])).getTime();
                    this_data = variableData[i];
                    if (isNaN(this_data))
                        this_data = null;
                    data[i] = [this_time, this_data];
                }
                return data;

            })(),
            tooltip: {
                valueDecimals: 2,
                valueSuffix: ' ' + this._units,
                xDateFormat: '%A, %b %e, %Y',
                headerFormat: '<span style="font-size: 12px; font-weight:bold;">{point.key} (Click to visualize the map on this time)</span><br/>'
            },
            custom: {
                variable: this._name,
                position: position,
                url: url
            }
        };
    },


    _updateSerie: function(serie, time, variableData) {
        var length = time.length;
        var new_data = new Array(length);
        var this_time = new Date();
        var this_data = null;
        for (var i = 0; i < length; i++) {
            this_time = (new Date(time[i])).getTime();
            this_data = variableData[i];
            if (isNaN(this_data))
                this_data = null;
            new_data[i] = [this_time, this_data];
        }
        var old_data = serie.options.data;
        serie.options.data = old_data.concat(new_data).sort();
        serie.setData(serie.options.data);
    },

    _loadMoreData: function(url, mindate, maxdate, callback) {
        var min = new Date(this._getNearestTime(mindate.getTime()));
        var max = new Date(this._getNearestTime(maxdate.getTime()));
        url = url + '&TIME=' + min.toISOString() + '/' + max.toISOString();
        if (this._proxy) url = this._proxy + '?url=' + encodeURIComponent(url);

        var oReq = new XMLHttpRequest();
        oReq.addEventListener("load", (function(xhr) {
            var data = xhr.currentTarget.responseXML;
            var result = {
                time: [],
                values: []
            };
            data.querySelectorAll('FeatureInfo').forEach(function(fi) {
                var this_time = fi.querySelector('time').textContent;
                var this_data = fi.querySelector('value').textContent;
                try {
                    this_data = parseFloat(this_data);
                } catch (e) {
                    this_data = null;
                }
                result.time.push(this_time);
                result.values.push(this_data);
            });
            if (callback !== undefined) {
                callback(result);
            }
        }).bind(this));
        oReq.addEventListener("error", (function(xhr) {
            if (callback !== undefined) {
                var result = {
                    time: [],
                    values: []
                };
                callback(result);
            }
        }).bind(this));
        oReq.overrideMimeType('application/xml');
        oReq.open("GET", url);
        oReq.send();
    },

});

L.timeDimension.layer.wms.timeseries = function(layer, options) {
    return new L.TimeDimension.Layer.WMS.TimeSeries(layer, options);
};



$(function(){
    updateWMS();

    $("#select_signal_process").change(function(){
        updateWMS();
    }).change();

    $("#select_storage_type").change(function(){
        updateWMS();
    }).change;

    $("#select_layer").change(function(){
        updateWMS();
    }).change();

    $("#select_legend").change(function(){
        updateWMS();
    }).change;

});



