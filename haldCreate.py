from PIL import Image

out = "Neutral"
lutSize = 64
haldSize = round((lutSize**3)**0.5)

hald = Image.new('RGB', (haldSize,haldSize), (0,0,0))
pixel = hald.load()
r = g = b = 0

for y in range(hald.height):
    for x in range(hald.width):
        def value(color):
            return round((255/(lutSize - 1))*color)
        if r >= lutSize : 
            r = 0
            g += 1
        if g >= lutSize:
            g = 0
            b += 1
        pixel[x,y] = (value(r), value(g), value(b))
        r += 1

hald.save(out+"_"+str(lutSize)+".png")  