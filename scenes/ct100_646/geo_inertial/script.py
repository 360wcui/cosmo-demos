# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Geostationary Orbit scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'GEO Spacecraft', '998', '996', '997' ]

########################################
# Initial setup
# 2021 MAR 03 22:10:35.000
cosmo.showFullScreen()
cosmo.pause()
cosmo.setTime( '2021-12-26 00:00:00 UTC' )
cosmo.hideAllObjects()
cosmo.hideToolBar()
cosmo.hideSpiceMessages()
cosmo.hideEcliptic()
cosmo.hideCenterIndicator()
cosmo.hideLabels()
cosmo.hidePlanetOrbits()

for body in bodies:
	cosmo.showObject( body )
# cosmo.wait( 10)
cosmo.showTrajectory( 'GEO Spacecraft' )
# cosmo.showTrajectory( '996' )
# cosmo.showTrajectory( '997' )
# cosmo.showTrajectory( '998' )
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'Earth' )
cosmo.selectObject( 'Earth' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ 16486.129309, -3942.242309, 9283.124232 ] )
cosmo.setCameraOrientation( [ -0.669684, -0.403500, -0.311482, -0.540084 ] )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.wait( 2 )
cosmo.showDirectionVector( 'Earth', 'GEO Spacecraft' )
cosmo.wait( 1 )
cosmo.setTimeRate( 600 )
cosmo.unpause()
cosmo.wait( 5 )
cosmo.circleCenterUp( 75, 5 )
cosmo.wait( 5 )

cosmo.pause()
