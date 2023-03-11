from PIL import Image

img=Image.open('steneography/dolphin.jpg')
pixels=img.load()

def find_closest_palette_colour(oldP):
    return (round(oldP[0]/255)*255,round(oldP[1]/255)*255,round(oldP[2]/255)*255)

def twotuplesminus(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1],t1[2]-t2[2])

def twotuplesplus(t1,t2,cons):
    return (int(t1[0]+t2[0]*cons),int(t1[1]+t2[1]*cons),int(t1[2]+t2[2]*cons))

for y in range(img.size[1]-1):
    for x in range(1,img.size[0]-1):
        oldP=pixels[x,y]
        Npixel=find_closest_palette_colour(oldP)
        pixels[x,y]=Npixel
        quant_error=twotuplesminus(oldP,Npixel)
        pixels[x + 1,y    ] = twotuplesplus(pixels[x + 1,y    ], quant_error , 7 / 16)
        pixels[x - 1,y + 1] = twotuplesplus(pixels[x - 1,y + 1], quant_error , 3 / 16)
        pixels[x    ,y + 1] = twotuplesplus(pixels[x    ,y + 1], quant_error , 5 / 16)
        pixels[x + 1,y + 1] = twotuplesplus(pixels[x + 1,y + 1], quant_error , 1 / 16)
pixels=img.show()
