
/*
 * L.TimeDimension.Layer.WMS.TimeSeries: create timeseries for specific locations
 */

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
            var mk_point = $("#btn-place-point");

            mk_point.on('click', (function() {
            this._enabledNewMarkers = true;

            }));


            map.doubleClickZoom.disable();
            map.once('dblclick', (function(e) {



            e.originalEvent.preventDefault();


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

        var color = this._getNextMarkerColor();


        var circle = L.circleMarker([point.position[0], point.position[1]], {
            color: '#FFFFFF',
            fillColor: color,
            fillOpacity: 0.8,
            radius: 5,
            weight: 2
        });


            circle.addTo(this._map);


        circle.addTo(this._map);

        var get_ts = $("#btn-get-plot");
        get_ts.on('click',(function() {

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
        if(this._baseLayer.getURL()=="https://tethys.byu.edu:7000/thredds/wms/testAll/grace/GRC_tot.25scaled.nc"){
            this._loadData(circle.getLatLng(),1, afterLoadData.bind(this, "#000099")); //total
            this._loadData(circle.getLatLng(),2, afterLoadData.bind(this, "#02f2ff")); //surface
            this._loadData(circle.getLatLng(),3, afterLoadData.bind(this, "#007a10")); //soil moisture
            this._loadData(circle.getLatLng(),4, afterLoadData.bind(this, "#88523f")); //groundwater
        }
        else{
        this._loadData(circle.getLatLng(),0, afterLoadData.bind(this, color)); //regular
        }
        }).bind(this));


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
	        var url="https://tethys.byu.edu:7000/thredds/wms/testAll/grace/GRC_jpl_tot.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	    }
	    if(doall==2){
	    //surface water
	        var url="https://tethys.byu.edu:7000/thredds/wms/testAll/grace/GRC_jpl_sw.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	        }
	    if(doall==3){
	        //soil moisture
	        var url="https://tethys.byu.edu:7000/thredds/wms/testAll/grace/GRC_jpl_soil.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
	    }
	    if(doall==4){
	        //groundwater
	        var url="https://tethys.byu.edu:7000/thredds/wms/testAll/grace/GRC_jpl_gw.nc?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetFeatureInfo&CRS=CRS:84";
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



