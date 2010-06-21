% COMSOL Multiphysics Model M-file
% Generated in part by COMSOL 3.5a (COMSOL 3.5.0.608, $Date: 2009/05/11 07:38:49 $)

flreport('off');

flclear fem

% COMSOL version
clear vrsn
vrsn.name = 'COMSOL 3.5';
vrsn.ext = 'a';
vrsn.major = 0;
vrsn.build = 608;
vrsn.rcs = '$Name: v35ap $';
vrsn.date = '$Date: 2009/05/11 07:38:49 $';
fem.version = vrsn;

% Geometry
g1=sphere3('0.4','pos',{'0','0','0'},'axis',{'0','0','1'},'rot','0');
g2=cylinder3('0.00025','0.1','pos',{'-0.05','0','0'},'axis',{'1','0','0'},'rot','15');
parr={point3(0,0,0)};
g3=geomcoerce('point',parr);
parr={point3(0.4,0,0)};
g4=geomcoerce('point',parr);
parr={point3(0,0.4,0)};
g5=geomcoerce('point',parr);
parr={point3(0,0,0.4)};
g6=geomcoerce('point',parr);
parr={point3(-0.4,0,0)};
g7=geomcoerce('point',parr);
parr={point3(0,-0.4,0)};
g8=geomcoerce('point',parr);
parr={point3(0,0,-0.4)};
g9=geomcoerce('point',parr);

% Analyzed Geometry (?)
clear p s
p.objs={g3,g4,g5,g6,g7,g8,g9};
p.name={'ORIGIN','PT1','PT2','PT3','PT4','PT5','PT6'};
p.tags={'g3','g4','g5','g6','g7','g8','g9'};

s.objs={g1,g2};
s.name={'SNOW','NEEDLE'};
s.tags={'g1','g2'};

fem.draw=struct('p',p,'s',s);
fem.geom=geomcsg(fem);


% ODE Settings
clear ode
clear units;
units.basesystem = 'SI';
ode.units = units;
fem.ode=ode;


% Initialize mesh
fem.mesh=meshinit(fem, ...
                  'hauto',5, ...
                  'hgradsub',[2,1.1], ...
                  'hmaxsub',[2,0.0005]);

% Refine mesh
fem.mesh=meshrefine(fem, ...
                    'mcase',0, ...
                    'rmethod','longest');

fem=multiphysics(fem);

fem.mesh
