r_cv = 0.2; //radius of control sphere, meters
r_n = 0.00025; //radius of needle probe, meters
l_n = 0.1; //length of needle probe, meters
rot_angle = Pi/4; //angle of rotation of needle probe, radians

l_c_cv = 0.03; //characteristic length of mesh near sphere
l_c_n = 0.000125; //characteristic length of mesh near needle

//Pts that define the sphere

Point(1) = {0, 0, 0, l_c_cv};
Point(2) = {r_cv, 0, 0, l_c_cv};
Point(3) = {0, r_cv, 0, l_c_cv};
Point(4) = {0, 0, r_cv, l_c_cv};
Point(5) = {-r_cv, 0, 0, l_c_cv};
Point(6) = {0, -r_cv, 0, l_c_cv};
Point(7) = {0, 0, -r_cv, l_c_cv};

//xy plane
Circle(8) = {2,1,3};
Circle(9) = {3,1,5};
Circle(10) = {5,1,6};
Circle(11) = {6,1,2};

//yz plane
Circle(12) = {3,1,4};
Circle(13) = {4,1,6};
Circle(14) = {6,1,7};
Circle(15) = {7,1,3};

//zx plane
Circle(16) = {4,1,2};
Circle(17) = {2,1,7};
Circle(18) = {7,1,5};
Circle(19) = {5,1,4};

//Makes the surfaces. thx gui
Line Loop(20) = {8, 12, 16};
Ruled Surface(21) = {20};
Line Loop(22) = {15, -8, 17};
Ruled Surface(23) = {22};
Line Loop(24) = {18, -9, -15};
Ruled Surface(25) = {24};
Line Loop(26) = {19, -12, 9};
Ruled Surface(27) = {26};
Line Loop(28) = {13, -10, 19};
Ruled Surface(29) = {28};
Line Loop(30) = {10, 14, 18};
Ruled Surface(31) = {30};
Line Loop(32) = {17, -14, 11};
Ruled Surface(33) = {32};
Line Loop(34) = {11, -16, 13};
Ruled Surface(35) = {34};

//also thx gui. Defines the volume.
Surface Loop(36) = {21, 23, 25, 31, 29, 35, 33, 27};
Volume(37) = {36}; //<----------------------------------------Ctrl Volume

//Pts to define the needle
//Need to refine this model but will stick to solid steel assumption for now
Point(39) = {-l_n/2, 0, 0, l_c_n};
Point(40) = {-l_n/2, r_n, 0, l_c_n};
Point(41) = {-l_n/2, 0, r_n, l_c_n};
Point(42) = {-l_n/2, -r_n, 0, l_c_n};
Point(43) = {-l_n/2, 0, -r_n, l_c_n};

Circle(43) = {40,39,41};
Circle(44) = {41,39,42};
Circle(45) = {42,39,43};
Circle(46) = {43,39,40};

Line Loop(47) = {43, 44, 45, 46};
Plane Surface(48) = {47};
Extrude {l_n, 0, 0} {
  Surface{48};
}

Surface Loop(71) = {57, 48, 61, 65, 69, 70};
Volume(72) = {71}; //<----------------------------------------Needle volume

//Rotates needle
Rotate {{0, 1, 0}, {0, 0, 0}, rot_angle} {
  Volume{72};
}

// I'm not sure what a Physical Volume is, but it sounds important.
Physical Volume(73) = {37};
Physical Volume(74) = {72};
