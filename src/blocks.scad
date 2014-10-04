// LIBGL_ALWAYS_SOFTWARE=1 openscad --projection=ortho --imgsize=83,83 -o /tmp/o.png /tmp/blocks.scad --camera=1,0.5,1,60,0,45,14

color([0.16, 0.27, 0.78]) cube();
color([0.27, 0.79, 0]) translate([1,0,0])cube();
color([0.84, 0.22, 0]) translate([0.5,0,1])cube();
