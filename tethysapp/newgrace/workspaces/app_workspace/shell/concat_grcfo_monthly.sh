#!/bin/bash

# $1 = GLOBAL_NETCDF_DIR


cd $1

ncrcat GRD-3_???????-???????_GRFO_UTCSR_BA01_0600_LND_v01.nc grcfo_csr_monthly.nc

ncremap -i grcfo_csr_monthly.nc -d GRC_csr_tot.nc -o GRCFO2_csr_total.nc

ncrcat GRD-3_???????-???????_GRFO_GFZOP_BA01_0600_LND_v01.nc grcfo_gfz_monthly.nc

ncremap -i grcfo_gfz_monthly.nc -d GRC_csr_tot.nc -o GRCFO_gfz_total.nc

ncrcat GRD-3_???????-???????_GRFO_JPLEM_BA01_0600_LND_v01.nc grcfo_jpl_monthly.nc

ncremap -i grcfo_jpl_monthly.nc -d GRC_csr_tot.nc -o GRCFO_jpl_total.nc

ncks -C -O -x -v area,gw,lat_bnds,lon_bnds GRCFO_jpl_tot.nc GRCFO_jpl_tot.nc

ncks -C -O -x -v area,gw,lat_bnds,lon_bnds GRCFO_csr_tot.nc GRCFO_csr_tot.nc

ncks -C -O -x -v area,gw,lat_bnds,lon_bnds GRCFO_gfz_tot.nc GRCFO_gfz_tot.nc


#ncatted -O -a _FillValue,lwe_thickness,o,d,-99999.0 GRC_jpl_tot.nc

#ncatted -O -a _FillValue,soil,o,d,-99999.0 anomaly.nc
#ncatted -O -a _FillValue,sw,o,d,-99999.0 anomaly.nc

#ncatted -O -a missing_value,soil,d,, anomaly.nc
#ncatted -O -a missing_value,sw,d,, anomaly.nc

#ncatted -O -a standard_name,soil,d,, anomaly.nc
#ncatted -O -a standard_name,sw,d,, anomaly.nc

#ncatted -O -a vmax,soil,d,, anomaly.nc
#ncatted -O -a vmax,sw,d,, anomaly.nc

#ncatted -O -a vmin,soil,d,, anomaly.nc
#ncatted -O -a vmin,sw,d,, anomaly.nc

#ncatted -O -a _ChunkSizes,,d,, anomaly.nc
#ncatted -O -a _ChunkSizes,,d,, anomaly.nc

#ncatted -O -a units,soil,o,c,cm anomaly.nc
#ncatted -O -a units,sw,o,c,cm anomaly.nc

#ncatted -O -a cell_methods,soil,d,, anomaly.nc
#ncatted -O -a cell_methods,sw,d,, anomaly.nc

#ncatted -O -a cell_measures,soil,c,c,area:area anomaly.nc
#ncatted -O -a cell_measures,sw,c,c,area:area anomaly.nc

#ncap2 -O -s "lat=double(lat)" anomaly.nc anomaly.nc
#ncap2 -O -s "lon=double(lon)" anomaly.nc anomaly.nc

#ncks -O -v lwe_thickness --msa -d lon,0.0,180.0 -d lon,-180.0,-0.125 GRC_jpl_tot.nc GRC_jpl_tot.nc
#ncap2 -O -s "where(lon<0) lon=lon+360" GRC_jpl_tot.nc GRC_jpl_tot.nc

#ncks -O -v soil,sw --msa -d lon,0.0,180.0 -d lon,-180.0,-0.125 anomaly.nc anomaly.nc
#ncap2 -O -s "where(lon<0) lon=lon+360" anomaly.nc anomaly.nc


#ncks -A -v lat,lon,time GRC_jpl_tot.nc anomaly.nc
#ncks -C -O -x -v time_bnds anomaly.nc anomaly.nc


#ncks -C -O -v lat,lon,time,soil anomaly.nc GRC_jpl_soil.nc
#ncrename -O -v soil,lwe_thickness GRC_jpl_soil.nc


#ncks -C -O -v lat,lon,time,sw anomaly.nc GRC_jpl_sw.nc
#ncrename -O -v sw,lwe_thickness GRC_jpl_sw.nc


#ncdiff -O GRC_jpl_tot.nc GRC_jpl_sw.nc GRC_jpl_gw1.nc
#ncdiff -O GRC_jpl_gw1.nc GRC_jpl_soil.nc GRC_jpl_gw.nc

#rm GRC_jpl_gw1.nc
#rm PET0.RegridWeightGen.Log
#rm anomaly.nc







