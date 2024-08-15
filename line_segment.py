# Author: Ashton Lee
# Github User: ashton01L
# Date: 8/14/2024
# Description: Define a 'Point' class that has two data members
# '_x_coord' and '_y_coord', representing the two coordinates of the point.

class Point:
    """
    A Class representing a point object within a two-dimensional coordinate plane grid layout along an x-axis and y-axis.

    Attributes:
        _x_coord: (float) the x-axis coordinate of the point.
        _y_coord: (float) the y-axis coordinate of the point.
    """
    def __init__(self, x_coord, y_coord):
        """
        initializes the Point object.

        :param x_coord: the x-axis coordinate of the point.
        :param y_coord: the y-axis coordinate of the point.
        """
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        """
        Returns the x-axis coordinate of the point.

        :return: (float) the x-coordinate.
        """
        return self._x_coord

    def get_y_coord(self):
        """
        Returns the y-axis coordinate of the point.

        :return: (float) the x-coordinate.
        """
        return self._y_coord

    def set_x(self, x_coord):
        """
        Sets the x-axis coordinate of the point.

        :param: x_coord (float): The new x-coordinate.
        """
        self._x_coord = x_coord

    def set_y(self, y_coord):
        """
        Sets the y-axis coordinate of the point

        :param: y_coord (float): The new y-coordinate
        """
        self._y_coord = y_coord

    def distance_to(self, other_point):
        """
        Calculates the distance between two Point objects.

        :param: Point: another Point object.
        :return: (float): Returns the distance between the two Point objects as a float.
        """
        dx = other_point.get_x_coord() - self._x_coord
        dy = other_point.get_y_coord() - self._y_coord
        return (dx**2 + dy**2) ** 0.5

class LineSegment:
    """
    A class representing a line segment defined by two endpoints.

    Attributes:
        _endpoint_1 (Point): The first endpoint of the line segment.
        _endpoint_2 (Point): The second endpoint of the line segment.
    """
    def __init__(self, endpoint_1, endpoint_2):
        """
        Initializes a LineSegment object.

        :param: endpoint_1 (Point): The first endpoint of the line segment.
        :param: endpoint_2 (Point): The second endpoint of the line segment.
        """
        self._endpoint_1 = endpoint_1
        self._endpoint_2 = endpoint_2

    def get_endpoint_1(self):
        """
        Returns the first endpoint of the line segment.

        :return: Point: The first endpoint.
        """
        return self._endpoint_1

    def get_endpoint_2(self):
        """
        Returns the second endpoint of the line segment.

        :return: Point: The second endpoint.
        """
        return self._endpoint_2

    def set_endpoint_1(self, endpoint_1):
        """
        Sets the first endpoint of the line segment.

        :return: The new first endpoint.
        """
        self._endpoint_1 = endpoint_1

    def set_endpoint_2(self, endpoint_2):
        """
        Sets the second endpoint of the line segment.

        :return: The new second endpoint.
        """
        self._endpoint_2 = endpoint_2

    def length(self):
        """
        Calculates the length of the line segment.

        :return: self._endpoint_1.distance_to(self._endpoint_2).
        """
        return self._endpoint_1.distance_to(self._endpoint_2)

    def slope(self):
        """
        Calculates the slope of the line segment.

        :return: The slope of the line segment.
        """
        dx = self._endpoint_2.get_x_coord() - self._endpoint_1.get_x_coord()
        dy = self._endpoint_2.get_y_coord() - self._endpoint_1.get_y_coord()
        if dx == 0:
            return None  # slope is undefined
        return dy / dx

    def is_parallel_to(self, other_line):
        """
        Determines if this line segment is parallel to another line segment.

        :param other_line: Another line segment.

        :return: bool: True if the two line segments are parallel, False otherwise.
        """
        try:
            slope_1 = self.slope()
            slope_2 = other_line.slope()

            # Edge cases where both line segments are vertical and thus have ZERO slope
            if slope_1 is None and slope_2 is None:
                return True

            # Edge cases where one line segment is vertical and the other is not, thus they are not parallel
            if slope_1 is None or slope_2 is None:
                return False

            # Handle case where one or both line segments have zero length
            if self.length() == 0 or other_line.length() == 0:
                # If the zero-length segment lies exactly on the other segment, return False
                if self.length() == 0:
                    single_point = self.get_endpoint_1()
                    if other_line.get_endpoint_1().distance_to(
                            single_point) + other_line.get_endpoint_2().distance_to(single_point) == other_line.length():
                        return False
                if other_line.length() == 0:
                    single_point = other_line.get_endpoint_1()
                    if self.get_endpoint_1().distance_to(single_point) + self.get_endpoint_2().distance_to(
                            single_point) == self.length():
                        return False
            return True

            # Compare slopes using floating-point precision as instructed in prompt
            return abs(slope_1 - slope_2) < 0.000001
        except ValueError:
            # if both lines are vertical, they are parallel.
            return self._endpoint_1.get_x_coord() == self._endpoint_2.get_x_coord() and \
                other_line.get_endpoint_1().get_x_coord() == other_line.get_endpoint_2().get_x_coord()

# point_1 = Point(7, 4)
# point_2 = Point(-6, 18)
# print(point_1.distance_to(point_2))  # 19.1049731745428
# line_seg_1 = LineSegment(point_1, point_2)
# print(line_seg_1.length())  # 19.1049731745428
# print(line_seg_1.slope())  # -1.0769230769230769
#
# point_3 = Point(-2, 2)
# point_4 = Point(24, 12)
# line_seg_2 = LineSegment(point_3, point_4)
# print(line_seg_1.is_parallel_to(line_seg_2))  # False
#
# point_5 = Point(1,2)
# point_6 = Point(4,6)
# line_seg_3 = LineSegment(point_5, point_6)
# print(line_seg_1.is_parallel_to(line_seg_3))  #False
# print(point_5.distance_to(point_6))  # 5.0
# print(line_seg_3.length())  # 5.0
# print(line_seg_3.slope())   # 1.3333333333333
#
# point_7 = Point(-2, 2)
# point_8 = Point(24, 12)
# line_seg_4 = LineSegment(point_7, point_8)
# print(line_seg_1.is_parallel_to(line_seg_4))  # False
#
# point_9 = Point(2,3)
# point_10 = Point(5,7)
# line_seg_5 = LineSegment(point_9, point_10)
# print(line_seg_1.is_parallel_to(line_seg_5))  # False
#
# print(line_seg_3.is_parallel_to(line_seg_5))  # True
#
# point_11 = Point(1,1)
# point_12 = Point(4,4)
# line_seg_6 = LineSegment(point_11, point_12)
# print(line_seg_1.is_parallel_to(line_seg_6)) # False
#
point_13 = Point(1,-4)
point_14 = Point(4,-1)
line_seg_7 = LineSegment(point_13, point_14)
# print(line_seg_6.is_parallel_to(line_seg_7))  # True

point_15 = Point(1,1)
point_16 = Point(1,1)
line_seg_8 = LineSegment(point_15, point_16)
print(line_seg_7.is_parallel_to(line_seg_8))  # True


