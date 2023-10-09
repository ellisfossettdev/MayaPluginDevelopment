# ---------------------------------------- Maya City Generator Plug In ----------------------------------------#

import maya.cmds as cmds                                                            # imports mayas command library as the varaible cmds

# ---------------------------------------- Create Building 1 (Cubed) ---------------------------------------- #

def createBuilding():                                                               # define createBuilding as a method
    buildingBase = cmds.polyCube(w = 10, h = 30, d = 10, ch=0, n = "building")      # create a cube called building with the height of 30 and width of 10 as the varaible buildingBase 
    cmds.move(0, 15, 0, buildingBase)                                               # move building base up by 15 so  it is level with ground grid
    frontDoor = cmds.polyCube(w = 2, h = 3, d = .25,ch=0, n = "b1_door")            # create a cube called bl_door with the height of 3 and width of 12 as the varaible front door
    cmds.move(0, 1.5, 5, frontDoor)                                                 # move door up by 15 so  it is level with ground grid
    
    floor_H = 0.25                                                                  # create variable for floor height called floor_H and set at 0.25
    floor_Dis = 10                                                                  # create variable for floor distance called floorDis and set at 10
    cubeBuilding_Grp = []                                                           # create empty list called cubeBuilding_Grp
    
    for i in range(4):                                                              # create for loop to count to 4
        floor = cmds.polyCube(w = 11, h = floor_H, d = 11, ch = 0, n = "buildFloor_#")[0]
        cmds.move(0,floor_Dis*i,0,floor)                                            # move each floor in the y direction using the floor_dis variable multiplied by i
        cubeBuilding_Grp.append(floor)                                              # append the list with each floor
        
    cmds.select(buildingBase, frontDoor, cubeBuilding_Grp)                          # select each element of the building
    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1)                            # whilst objects are still selected freeze the transformation

    cubeBuilding_Grp = cmds.group(n = "CubeBuilding_Grp")                           # add selected objects to a group called CubeBuilding_Grp

# ---------------------------------------- Creating Building 2 (Cylinder) ---------------------------------------- #

def createBuilding2():                                                              # define createBuilding as a method
    buildingBase = cmds.polyCylinder(r = 10, h = 30, ch=0, n = "buildingcy")        # create a cylinder called buildingcy as the varaible buildingBase 
    cmds.move(0, 15, 0, buildingBase)                                               # move buildingcy up by 15 so  it is level with ground grid
    frontDoor = cmds.polyCube(w = 2, h = 3, d = .25,ch=0, n = "b2_door")            # create a cube called b2_door with the height of 3 and width of 12 as the varaible front door
    cmds.move(0, 1.5, 10, frontDoor)                                                # move door up by 15 so  it is level with ground grid
    
    floor_H = 0.25                                                                  # create variable for floor height called floor_H and set at 0.25
    floor_Dis = 10                                                                  # create variable for floor distance called floorDis and set at 10
    cylinderBuilding_Grp = []                                                       # create empty list called cylinderBuilding_Grp
    
    for i in range(4):                                                              # create for loop to count to 4
        floor = cmds.polyCylinder(r = 11, h = floor_H, ch = 0, n = "buildFloor_#")[0]
        cmds.move(0,floor_Dis*i,0,floor)                                            # move each floor in the y direction using the floor_dis variable multiplied by i
        cylinderBuilding_Grp.append(floor)                                          # append the list and with the each floor
        
    cmds.select(buildingBase, frontDoor, cylinderBuilding_Grp)                      # select each element of the building
    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1)                            # whilst objects are still selected freeze the transformation

    cylinderBuilding_Grp = cmds.group(n = "cylinderBuilding_Grp")                   # add selected objects to a group called cylinderBuilding_Grp
        
# ---------------------------------------- Creating Car ---------------------------------------- #

def createCar():                                                                 # define createCar as a method
    car = cmds.polyCube(w = 3, h = 1, d = 8, ch=0, sd = 3, n = "car")[0]         # create cube with width of 3 height of 1 and depth of 8 with subdivisions set to 3
    cmds.move(0, 1.5, 0)                                                         # move building up 1.5 on Y axis
    cmds.polyExtrudeFacet(car + ".f[2]", ltz = 1.5, ls=(.9, .9, .9))             # extrude 2nd face and bring up on Y 1.5 and scale locally .9
    cmds.delete(ch = True)                                                       # clear construction history

    wheel1 = cmds.polyCylinder(r = 1, h = .5, ch=0, ax=(1,0,0), n = "wheel1")[0] # create cylinder with radius of 1 and height of .5 called wheel1
    cmds.move(1.7, 1, 2.6,wheel1)                                                # move cylinder in X 1.7, Y in 1 and Z 2.6
    wheel2 = cmds.polyCylinder(r = 1, h = .5, ch=0, ax=(1,0,0), n = "wheel2")[0] # create cylinder with radius of 1 and height of .5 called wheel2
    cmds.move(-1.7, 1, 2.6,wheel2)                                               # move cylinder in X -1.7, Y in 1 and Z 2.6
    wheel3 = cmds.polyCylinder(r = 1, h = .5, ch=0, ax=(1,0,0), n = "wheel3")[0] # create cylinder with radius of 1 and height of .5 called wheel3
    cmds.move(1.7, 1, -2.6,wheel3)                                               # move cylinder in X 1.7, Y in 1 and Z -2.6
    wheel4 = cmds.polyCylinder(r = 1, h = .5, ch=0, ax=(1,0,0), n = "wheel4")[0] # create cylinder with radius of 1 and height of .5 called wheel4
    cmds.move(-1.7, 1, -2.6,wheel4)                                              # move cylinder in X -1.7, Y in 1 and Z -2.6

    cmds.select(wheel1,wheel2,wheel3,wheel4,car)                                 # select each element of the car
    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1)                         # freeze transformations of selected objects

    wheel_Grp = cmds.group(wheel1, wheel2, wheel3, wheel4, n="Wheel_Grp")        # create a group from wheel objects
    car_Grp= cmds.group(car, wheel_Grp, n ="Car_Grp")                            # create a group from car and wheel objects
    
# ---------------------------------------- Creating Lamp Post ---------------------------------------- #

def createLampPost():                                                                           # define createLampPost as a method
    lampBase = cmds.polyCylinder(h = 3, r = 1, n = "lampBase", ch = 0)[0]                       # create a cylinder with heigh of 3 and radius of 1 called lampBase
    cmds.move(0, 1.5, 0, lampBase)                                                              # move lampBase up to above ground grid
    cmds.polyBevel(".f[21]", o = .2)                                                            # apply poly bevel to top face of lampBse offset of .2

    midSection = cmds.polyCylinder(h = 1, r = .5, n = "midSection", ch = 0)[0]                  # create a cylinder with heigh of 1 and radius of .5 midSection
    cmds.move(0, 3.4, 0, midSection)                                                            # move midSection up 3.4 in Y axis
    cmds.polyBevel(".f[21]", o = .1)                                                            # apply poly bevel to top face of lampBse offset of .1

    mainPole = cmds.polyCylinder(h = 20, r = .25, sa = 12, sh = 20, n = "mainPole", ch = 0)[0]  # create a cylinder with heigh of 20 and radius of .25 mainPole
    cmds.move(0, 13.5, 0, mainPole)                                                             # move midSection up 13.5 in Y axis

    bend_NL = cmds.nonLinear(mainPole, type = 'bend', curvature = 90)                           # create nonLinear bend with a curvature of 90 called bend_NL
    cmds.setAttr(bend_NL[0]+".lowBound", 0)                                                     # acess atribue of bend_NL "lowBound"
    cmds.delete(mainPole, ch = 1)                                                               # delete construction history of mainPole

    lampHead = cmds.polyCube(w = 4, h = 1.2, d = 2, n = "lampHead", ch = 0)[0]                  # create a cube with heigh of 1.2, width of 3 and depth of 2
    cmds.move(6.13, 19.7, 0, lampHead)                                                          # move lampHead up 6.13 in X axis 19.2 in Y axis
    cmds.polyBevel(".f[3]", o = .5)                                                             # apply poly bevel to bottom face of lampHead offset of .5

    cmds.select(lampBase, midSection, mainPole, lampHead)                                       # select all lamp components
    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1)                                        # freeze transformation for all lamp components
    cmds.delete(ch = True)                                                                      # clear construction history

    streetLight_Grp = cmds.group(n = "streetLight_Grp")                                         # group lamp components together as streetlight_Grp

# ---------------------------------------- Creating Traffic Lights ---------------------------------------- #

def createTrafficLight():                                                                            # define createTrafficLight as a method
    trafficBase = cmds.polyCylinder(h = 3, r = 1, n = "trafficBase", ch = 0)[0]                      # create a cylinder with heigh of 3 and radius of 1 called trafficBase
    cmds.move(0, 1.5, 0, trafficBase)                                                                # move trafficBase up to above ground grid
    cmds.polyBevel(".f[21]", o = .2)                                                                 # apply poly bevel to top face of trafficBase offset of .2

    trafficMidSection = cmds.polyCylinder(h = 1, r = .5, n = "trafficMidSection", ch = 0)[0]         # create a cylinder with heigh of 1 and radius of .5 trafficMidSection
    cmds.move(0, 3.4, 0, trafficMidSection)                                                          # move trafficMMidSection up 3.4 in Y axis
    cmds.polyBevel(".f[21]", o = .1)                                                                 # apply poly bevel to top face of trafficMidSection offset of .1

    trafficPole = cmds.polyCylinder(h = 10, r = .25, sa = 12, sh = 20, n = "trafficPole", ch = 0)[0] # create a cylinder with heigh of 10 and radius of .25 trafficPole
    cmds.move(0, 8.5, 0, trafficPole)                                                                # move trafficPole up 8.5 in Y axis

    trafficHead = cmds.polyCube(w = 2, h = 6, d = 2, n = "trafficHead", ch = 0)[0]                   # create a cube with width of 2, height of 6 and depth of 2
    cmds.move(0, 15, 0, trafficHead)                                                                 # move trafficPole up 15 in Y axis
    
    lightDis = 2                                                                                     # create variable for light distance called lightDis and set at 2
    trafficLights_Grp = []                                                                           # create empty list called trafficLights_Grp
    
    for i in range(3):                                                                               # create for loop to count to 3
        trafficLights = cmds.polyCylinder(h = 2.5, r = .8, n = "trafficLights_", ch = 0) [0]         # create a cylinder with heigh of 2.5 and radius of .8 trafficLights
        cmds.move(0,lightDis*i,0,trafficLights)                                                      # move each light in the y direction using the lightDis variable multiplied by i
        cmds.rotate( 0, 0, '90deg', r=True )                                                         # rotate light 90 degrees on Z axis 
        cmds.polyBevel(".f[20]", ".f[21]", o = .1)                                                   # apply poly bevel to end faces of trafficLights offset of .1
        trafficLights_Grp.append(trafficLights)                                                      # append the list with each traffic light
        
    cmds.move(0,13,0,trafficLights_Grp,r=1)                                                          # move trafficLights_Grp up 13 in relative Y axis
    
    cmds.select(trafficBase, trafficMidSection, trafficPole, trafficHead, trafficLights_Grp)         # select each element of the trafficLights
    cmds.makeIdentity(apply = True, t = 1, r = 1, s = 1)                                             # freeze transformation of selected objects
    cmds.delete(ch = True)                                                                           # clear construction history

    trafficLight_Grp = cmds.group(n = "traffictLight_Grp")                                           # group traffic light components together as trafficLight_Grp

# ---------------------------------------- Creating Road Tiles ---------------------------------------- #

def createRoadTile():
    roadTile = cmds.polyPlane (w = 12, h = 12, n = "roadTile", ch = 0)[0]                    # create polyPlane with width and height of 12 called roadTile
    cmds.polyExtrudeFacet(roadTile + ".f[90]", ".f[80]", ".f[70]", ".f[60]",                 # select faces to extrude
    ".f[50]", ".f[40]", ".f[30]",".f[20]", ".f[10]", ".f[0]", ltz = .5, ls=(.9, .9, .9))     # extrude faces up .5 and scale by .9
    cmds.polyExtrudeFacet(roadTile + ".f[99]", ".f[89]", ".f[79]", ".f[69]", ".f[59]",       # select faces to extrude
    ".f[49]", ".f[39]",".f[29]", ".f[19]", ".f[9]", ltz = .5, ls=(.9, .9, .9))               # extrude faces up .5 and scale by .9
    cmds.delete(ch = True)                                                                   # clear construction history
    cmds.select(d = 1)                                                                       # deselect faces after extrude
    
    
def roadTitleCorner():
    roadTitleCorner = cmds.polyPlane (w = 12, h = 12, n = "roadTitleCorner", ch = 0)[0]       # create polyPlane with width and height of 12 called roadTileCorner
    cmds.polyExtrudeFacet(roadTitleCorner + ".f[99]", ".f[89]", ".f[79]", ".f[69]", ".f[59]", # select faces to extrude
     ".f[49]", ".f[39]",".f[29]", ".f[19]", ".f[9]", ltz = .5, ls=(.9, .9, .9))               # extrude faces up .5 and scale by .9
    cmds.polyExtrudeFacet(roadTitleCorner + ".f[90]", ".f[91]", ".f[92]", ".f[93]", ".f[94]", # select faces to extrude
    ".f[95]", ".f[96]",".f[97]", ".f[98]", ltz = .5, ls=(.9, .9, .9))                         # extrude faces up .5 and scale by .9
    cmds.delete(ch = True)                                                                    # clear construction history
    cmds.select(d = 1)                                                                        # deselect faces after extrude
    

# ---------------------------------------- Window ---------------------------------------- #

window = cmds.window(t = "CITY GENERATOR V1.1", s = 0, mxb = 0, widthHeight=(400, 525))     # create a new window with the title "city generator" and set the height to 400 by 500
cmds.columnLayout(adjustableColumn = True)                                                  # set column layout to adjustable to centre all of the UI elements
cmds.showWindow( window )                                                                   # show window to user

logoPath = cmds.internalVar(upd = True) + "icons/mainLogo.jpg"                              # create variable called logoPath and access iconds folder and image mainLogo.jpg
cmds.image(w = 400, h = 100, image = logoPath)                                              # set image size from path to 400 x 100
cmds.separator("", h = 20, style = "in")                                                    # create horiztonal seperator between main logo and buttons

# ---------------------------------------- Buttons ---------------------------------------- #

cmds.text(l = "Click on the buttons to add assets into your scene")                # create label with instructions on how to use plug in
cmds.text(l = "")                                                                  # Blank Space
cmds.button(label = "Create Building", h = 50, c = "createBuilding()")             # create a button with the label to create building using the method createBuilding():
cmds.button(label = "Create Building 2", h = 50, c = "createBuilding2()")          # create a button with the label to create building using the method createBuilding2()
cmds.button(label = "Create Car", h = 50, c = "createCar()")                       # create a button with the label to create car using the method createCar()       
cmds.button(label = "Create Street Light", h = 50, c = "createLampPost()")         # create a button with the label to create lamp post using the method createLampPost()
cmds.button(label = "Create Traffic Light", h = 50, c = "createTrafficLight()")    # create a button with the label to create traffic light using the method createtrafficLight()
cmds.button(label = "Create Road Tile", h = 50, c = "createRoadTile()")            # create a button with the label to create road tile using the method createroadTile()
cmds.button(label = "Create Road Tile Corner", h = 50, c = "roadTitleCorner()")    # create a button with the label to create road tile corner using the method createroadTileCorner()
cmds.showWindow( window )

cmds.text(l = "City Built by E.F (50304835)")                                      # label to show development credits
cmds.text(l='<a href="https://youtu.be/dshwFsNp30Y">Video Example</a>',hl=True)    #hyperlink to video demonstration