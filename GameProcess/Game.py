from MathLevel.Point import *
from MathLevel.CoordinateSystem import *
from MathLevel.BilinearForm import *
from MathLevel.VectorSpace import *
from Entity import *

from Exceptions.exceptionsGame import *


class Game:

    def __init__(self, cs, entities):
        if isinstance(cs, CoordinateSystem):
            if isinstance(entities, EntitiesList):
                self.cs = cs
                self.entities = entities
            else:
                raise WRONG_INPUT.MESSAGE("EntitiesList", type(entities))
        else:
            raise WRONG_INPUT.MESSAGE("CoordinateSystem", type(cs))

    def run(self):
        pass

    def update(self):
        pass

    def exit(self):
        pass

    def get_entity_class(self):

        class Game_entity(Entity):
            def __init__(pself):
                super().__init__(self.cs)

        return Game_entity

    def get_ray_class(self):

        class Game_Ray(Ray):
            def __init__(pself):
                super().__init__(self.cs, self.cs.initial_point, self.cs.space.basis[0])

        return Game_Ray

    def get_object_class(self):

        class Game_Object(self.get_entity_class()):

            def __init__(pself, position, direction):
                super().__init__()
                if isinstance(position, Point):
                    pself.set_property("position", position)
                else:
                    raise WRONG_INPUT.MESSAGE("Point", type(position))
                if isinstance(direction, Vector):
                    pself.set_property("direction", direction)
                else:
                    raise WRONG_INPUT.MESSAGE("Vector", type(direction))

            def move(self, direction):
                if isinstance(direction, Vector):
                    self['position'] += direction
                else:
                    raise WRONG_INPUT.MESSAGE("Vector", type(direction))

            def planar_rotate(self, ind1, ind2, angle):
                self.direction *= Matrix.get_rotation_matrix(ind1, ind2, angle)

            def rotate_3d(self, angle1, angle2, angle3):
                self.direction *= Matrix.get_teit_bryan_matrix(angle1, angle2, angle3)

            def set_position(self, position):
                if isinstance(position, Point):
                    self.position = position
                else:
                    raise WRONG_INPUT.MESSAGE("Point", type(position))

            def set_direction(self, direction):
                if isinstance(direction, Vector):
                    self.direction = direction
                else:
                    raise WRONG_INPUT.MESSAGE("Vector", type(direction))

        return Game_Object

    def get_camera_class(self):

        class Game_Camera(self.get_object_class()):

            def __init__(pself, *args, type='r'):
                super().__init__()
                l = len(args)
                if l == 2:
                    if isinstance(args[0], float) or isinstance(args[0], int):
                        if isinstance(args[1], float) or isinstance(args[1], int):
                            fov = args[0]
                            draw_distance = args[1]
                            if type == 'd':
                                fov *= 3.141592 / 180
                            vfov = arctg((16/9)*(sin(fov/2)/cos(fov/2)))
                            pself.fov = fov
                            pself.vfov = vfov
                            pself.draw_distance = draw_distance
                            pself.set_property("fov", fov)
                            pself.set_property("vfov", vfov)
                            pself.set_property("draw_distance", draw_distance)
                        else:
                            raise WRONG_INPUT.MESSAGE("float", type(args[1]))
                    else:
                        raise WRONG_INPUT.MESSAGE("float", type(args[0]))

                elif l == 3:
                    if isinstance(args[0], float) or isinstance(args[0], int):
                        if isinstance(args[2], float) or isinstance(args[2], int):
                            fov = args[0]
                            draw_distance = args[2]
                            if isinstance(args[1], float) or isinstance(args[1], int):
                                vfov = args[1]
                                if type == 'd':
                                    fov *= 3.141592/180
                                    vfov *= 3.141592/180
                                pself.fov = fov
                                pself.vfov = vfov
                                pself.draw_distance = draw_distance
                                pself.set_property("fov", fov)
                                pself.set_property("vfov", vfov)
                                pself.set_property("draw_distance", draw_distance)
                            elif isinstance(args[1], Point):
                                look_at = args[1]
                                if type == 'd':
                                    fov *= 3.141592/180
                                vfov = arctg((16 / 9) * (sin(fov / 2) / cos(fov / 2)))
                                pself.fov = fov
                                pself.vfov = vfov
                                pself.look_at = look_at
                                pself.draw_distance = draw_distance
                                pself.set_property("fov", fov)
                                pself.set_property("vfov", vfov)
                                pself.set_property("look_at", look_at)
                                pself.set_property("draw_distance", draw_distance)
                            else:
                                raise WRONG_INPUT.MESSAGE("Point or float", type(args[1]))
                        else:
                            raise WRONG_INPUT.MESSAGE("float", type(args[2]))
                    else:
                        raise WRONG_INPUT.MESSAGE("float", type(args[0]))
                elif l == 4:
                    if isinstance(args[0], float) or isinstance(args[0], int):
                        if isinstance(args[1], float) or isinstance(args[1], int):
                            if isinstance(args[2], Point):
                                if isinstance(args[3], float) or isinstance(args[3], int):
                                    fov = args[0]
                                    vfov = args[1]
                                    look_at = args[2]
                                    draw_distance = args[3]
                                    if type == 'd':
                                        fov *= 3.141592 / 180
                                        vfov *= 3.141592 / 180
                                    pself.fov = fov
                                    pself.vfov = vfov
                                    pself.look_at = look_at
                                    pself.draw_distance = draw_distance
                                    pself.set_property("fov", fov)
                                    pself.set_property("vfov", vfov)
                                    pself.set_property("look_at", look_at)
                                    pself.set_property("draw_distance", draw_distance)
                                else:
                                    raise WRONG_INPUT.MESSAGE("float", type(args[3]))
                            else:
                                raise WRONG_INPUT.MESSAGE("Point", type(args[2]))
                        else:
                            raise WRONG_INPUT.MESSAGE("float", type(args[1]))
                    else:
                        raise WRONG_INPUT.MESSAGE("float", type(args[0]))
        return Game_Camera