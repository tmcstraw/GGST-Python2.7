
//function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
   		var mystring=this.responseText;
    	var stringvariable=this.responseText;
        var variable="lwe_thickness"
        length=variable.length;
        var pos=stringvariable.lastIndexOf(variable);
        pos=pos+6+length;
        var pos2=stringvariable.lastIndexOf("time");
        pos2=pos2-1;
    	stringvariable=stringvariable.slice(pos,(pos2));
        var variablearray = JSON.parse("[" + stringvariable + "]");
      pos2=pos2+11;
      var timestring=mystring.slice(pos2);
      var timearray=JSON.parse("["+timestring+"]");

      //time conversion
      var oneday=24*60*60*1000;
      var UTCconversion=7*60*60*1000;
      var startdate= new Date(2002,0,01).getTime();
      var length = timearray.length;
      for (var i=0; i<length; i++){
      	timearray[i]=startdate+timearray[i]*oneday-UTCconversion;
        timearray[i]=new Date(timearray[i]).toISOString();
      }
      //end time conversion

                var data = new Array(length);
                var this_time = new Date();
                var this_data = null;
                for (var i = 0; i < length; i++) {
                    this_time = timearray[i];
                    this_data = variablearray[i];
                    if (isNaN(this_data))
                        this_data = null;
                    data[i] = [this_time,this_data];
                    }


// High Charts time
var output=new Date(testTimeLayer._timeDimension.getCurrentTime());
    console.log(output);
Highcharts.stockChart('chart', {
        legend: {
                enabled: true
        },

        chart: {
                zoomType: 'x'
        },
        rangeSelector: {
                selected: 'All',
                buttons: [{

                    type: 'all',
                    text: 'All'
                }]
        },

        title: {
            text: 'Liquid Water Equivalent Thickness (cm)'
        },

        series: [{
            name: 'Liquid Water Equivalent Thickness (cm)',
            data: data,
            type: 'area',
            threshold: null,
            tooltip: {
                valueDecimals: 2
            },
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },

            }
        }]
    });//end of High Charts stuff

       }//for the if statement
  }; // for the onreadystatechange
  xhttp.open("GET", "http://localhost:8080/thredds/dodsC/testAll/grace/Nepal/NepalTotalAnomaly.nc.ascii?", true);
  xhttp.send();
//}

