r_cv = 0.2; //radius of control sphere, meters
r_n = 0.00025; //radius of needle probe, meters
l_n = 0.1; //length of needle probe, meters
rot_angle = Pi/4; //angle of rotation of needle probe, radians

//Pts to define the needle
//Need to refine this model but will stick to solid steel assumption for now
Point(39) = {-l_n/2, 0, 0};
Point(40) = {-l_n/2, r_n, 0};
Point(41) = {-l_n/2, 0, r_n};
Point(42) = {-l_n/2, -r_n, 0};
Point(43) = {-l_n/2, 0, -r_n};

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
Physical Volume(74) = {72};
