from nodebox.graphics import *
import numpy
import random

firefly_radius = 20
cycle_time = canvas.fps * 5

class Firefly(object):
    def __init__(self, iy, ix, flies):
        self.blink_time = random.randint(1, cycle_time)
        self.ix = ix
        self.iy = iy
        self.x = ix * firefly_radius + .5 * firefly_radius
        self.y = iy * firefly_radius + .5 * firefly_radius
        self.others = flies
        self.bounds = self._get_bounds(1)

    def _get_bounds(self, distance):
        rows, cols = self.others.shape

        left = max(0, self.ix - distance)
        top  = max(0, self.iy - distance)
        right  = min(self.ix + distance + 1, cols)
        bottom = min(self.iy + distance + 1, rows)

        return (left, top, right, bottom)

    def update(self):
        left, top, right, bottom = self.bounds
        blink_times = []
        indices = []
        for x in xrange(left, right):
            for y in xrange(top, bottom):
                blink_times.append(self.others[y][x].blink_time)
                indices.append((x, y))

        # new_blink_time = int(numpy.average(blink_times))
        new_blink_time = sorted(blink_times)[2]
        self.blink_time = new_blink_time 

    def __str__(self):
        print self.ix, self.iy, self.bounds, self.blink_time

    def draw(self):
        # FF9900
        # http://www.cityinabottle.org/nodebox/#canvas
        frame = canvas.frame % cycle_time
        distance = abs(self.blink_time - frame)
        max_alpha = 200
        max_distance = 10
        if distance < max_distance:
            alpha = max_alpha - distance * .75 * (max_alpha / max_distance)
            orange = Color(255, 153, 0, alpha, base=255.0, colorspace=RGB)
            fill(orange)
            ellipse(self.x, self.y, firefly_radius, firefly_radius)
        """
        else: 
            fill(.2, 0.75)
            ellipse(self.x, self.y, firefly_radius, firefly_radius)
        """

def make_flies(w, h):
    cols = w / firefly_radius
    rows = h / firefly_radius
    flies = numpy.empty((rows, cols), dtype=Firefly)
    print "making flies", flies.shape
    for r in range(rows):
        for c in range(cols):
            flies[r][c] = Firefly(r, c, flies)

    return flies

