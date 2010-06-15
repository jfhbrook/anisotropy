r_cv = 0.4;

Point(1) = {0, 0, 0};
Point(2) = {r_cv, 0, 0};
Point(3) = {0, r_cv, 0};
Point(4) = {0, 0, r_cv};
Point(5) = {-r_cv, 0, 0};
Point(6) = {0, -r_cv, 0};
Point(7) = {0, 0, -r_cv};

Circle(8) = {2,1,3};
Circle(9) = {3,1,5};
Circle(10) = {5,1,6};
Circle(11) = {6,1,2};

Circle(12) = {3,1,4};
Circle(13) = {4,1,6};
Circle(14) = {6,1,7};
Circle(15) = {7,1,3};

Circle(16) = {4,1,2};
Circle(17) = {2,1,7};
Circle(18) = {7,1,5};
Circle(19) = {5,1,4};

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

Surface Loop(36) = {21, 23, 25, 31, 29, 35, 33, 27};
Volume(37) = {36};
Physical Volume(38) = {37};
