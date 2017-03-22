from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

# print_matrix( make_translate(3, 4, 5) )
# print
# print_matrix( make_scale(3, 4, 5) )
# print
# print_matrix( make_rotX(math.pi/4) )
# print
# print_matrix( make_rotY(math.pi/4) )
# print
# print_matrix( make_rotZ(math.pi/4) )

add_circle( edges, 250, 250, 0, 200, 0.01 )
add_circle( edges, 250, 250, 0, 20 , 0.05 )
add_circle( edges, 250, 250, 0, 40 , 0.05 )

#add_edge ( edges, 210, 210, 0, 250, 210, 0 )
#add_edge ( edges, 210, 210, 0, 210, 250, 0 )
#add_edge ( edges, 210, 210, 0, 250, 160, 0 )

add_bezier_curve( edges, 210, 330, 210, 400, 250, 400, 250, 330, 0.01 )
add_bezier_curve( edges, 250, 330, 250, 400, 290, 400, 290, 330, 0.01 )
add_bezier_curve( edges, 170, 430, 175, 325, 175, 325, 59 , 300, 0.01 )
add_bezier_curve( edges, 330, 430, 325, 325, 325, 325, 441, 300, 0.01 )

parse_file( 'script', edges, transform, screen, color )
