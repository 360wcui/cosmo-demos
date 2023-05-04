# -*- coding:utf-8; mode:python; mode:auto-fill; fill-column:79; -*-

## @file      script.py
## @brief     Cosmographia script for Geostationary Orbit scene.
## @author    A. Gonzalez <alfonso.gonzalez@nablazerolabs.com>
## @copyright (C) 2021 Nabla Zero Labs

import cosmoscripting

cosmo  = cosmoscripting.Cosmo()
bodies = [ 'Sun', 'Earth', 'Moon', 'Cape Canaveral', '998', '996', '997' ]

########################################
# Initial setup
# 2021 MAR 03 22:10:35.000
cosmo.showFullScreen()
cosmo.setTime( '2021-12-26 14:00:10 UTC' )
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
cosmo.showTrajectory( 'Cape Canaveral' )
# cosmo.showTrajectory( '996' )
# cosmo.showTrajectory( '997' )
# cosmo.showTrajectory( '998' )
cosmo.showTrajectory( 'Moon' )

cosmo.setCentralObject( 'Earth' )
cosmo.selectObject( 'Earth' )
cosmo.setCameraToInertialFrame()
cosmo.setCameraPosition( [ -19904.398788, -6191.286492, 8402.380904 ] )
cosmo.setCameraOrientation( [ -0.717461, -0.411346, 0.379296, 0.414944 ] )
cosmo.showLabels()

########################################
# Begin scene

cosmo.fadeIn( 1 )
cosmo.setTimeRate( 4 )
cosmo.circleCenterRight( 360.0, 240)
cosmo.wait( 2 )
# cosmo.showDirectionVector( 'Earth', 'Cape Canaveral' )
cosmo.wait( 1 )
# cosmo.wait( 5 )
cosmo.wait( 20 )
cosmo.moveAwayFromCenter( 10000, 3 ).wait( 1 )
cosmo.wait( 20 )



cosmo.pause()
