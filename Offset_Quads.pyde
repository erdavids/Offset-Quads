# Inspired by this post:
# https://www.reddit.com/r/generative/comments/g07wgz/rythm/

w, h = 1000, 1000

#colors = [(127, 199, 175, 110), (218, 216, 167, 110), (167, 219, 216, 110), (237, 118, 112, 110)]
colors = [(92,97,130, 110), (79,164,165, 110), (202,166,122, 110), (212,117,100, 110)]
#colors = [(139,169,135, 150), (244,107,99, 150), (100,161,165, 150)]


# Number of quads
grid_x = 30
grid_y = 30

# Seperation between the bricks
diff = 6
base_deform = 3
back_deform = 3
offset = 2

# Nature of the grid changes
horizontal_length = 2

# The quads will draw inside this rectangle
grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

# Distance between the birds
sep_x = float(grid_x_pixels) / (grid_x - 1)
sep_y = float(grid_y_pixels) / (grid_y - 1)

def get_random_element(l):
    return l[int(random(len(l)))]

# Center of the quad, size, deform strength, rotation, outline, fill color
def draw_rect(x, y, x_s, y_s, d, r, o, f):

    stroke(*o)
    fill(*f)
    strokeJoin(ROUND)
    beginShape()
    
    vertex(x - x_s - random(-d, d), y - y_s - random(-d, d))
    vertex(x + x_s - random(-d, d), y - y_s - random(-d, d))
    vertex(x + x_s - random(-d, d), y + y_s - random(-d, d))
    vertex(x - x_s - random(-d, d), y + y_s - random(-d, d))
    
    endShape(CLOSE)
    
def setup():
    size(w, h)
    pixelDensity(2)
    background(255)
    
    strokeWeight(2)
    
    grid = []
    
    for i in range(grid_x):
        grid.append([])
        for j in range(grid_y):
            grid[i].append(1)
            
    for i in range(grid_x):
        for j in range(grid_y):
            if (i < grid_x - 1):
                if (random(1) < .3 and grid[i][j] is 1):
                    grid[i][j] = 2
                    grid[i + 1][j] = 0
            if (j < grid_y - 1):
                if (random(1) < .3 and grid[i][j] is 1 and grid[i][j + 1] is not 0):
                    grid[i][j] = 3
                    grid[i][j + 1] = 0
            if (i < grid_x - 1 and j < grid_y - 1):
                if (random(1) < .2 and grid[i][j] is 1 and grid[i][j + 1] is 1 and grid[i + 1][j] is 1 and grid[i + 1][j + 1] is 1):
                    grid[i][j] = 4
                    grid[i + 1][j] = 0
                    grid[i][j + 1] = 0
                    grid[i + 1][j + 1] = 0
        

    
    current_x = w/2.0 - grid_x_pixels/2.0
    current_y = h/2.0 - grid_y_pixels/2.0
    for i in range(grid_x):
        for j in range(grid_y):
            o = (0, 0, 0, 255)
            f = (0, 0, 255, 0)
            
            cell = grid[i][j]
            
            
            short_x = sep_x/2 - diff
            long_x = sep_x - diff
            short_y = sep_y/2 - diff
            long_y = sep_y - diff
            
            if (cell is 1):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + random(-offset, offset), current_y + random(-offset, offset), short_x, short_y, back_deform, -1, o, f)
            
                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x, current_y, short_x, short_y, base_deform, -1, o, f)
            if (cell is 2):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + sep_x/2 + random(-offset, offset), current_y + random(-offset, offset), long_x, short_y, back_deform, -1, o, f)
            
                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x + sep_x/2, current_y, long_x, short_y, base_deform, -1, o, f)
            if (cell is 3):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + random(-offset, offset), current_y + sep_y/2 + random(-offset, offset), short_x, long_y, back_deform, -1, o, f)

                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x, current_y + sep_y/2, short_x, long_y, base_deform, -1, o, f)
            if (cell is 4):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + sep_x/2 + random(-offset, offset), current_y + sep_y/2 + random(-offset, offset), long_x, long_y, back_deform, -1, o, f)

                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x + sep_x/2, current_y + sep_y/2, long_x, long_y, base_deform, -1, o, f)
            
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0
        current_x += sep_x
        
    save('Examples/out.png')
