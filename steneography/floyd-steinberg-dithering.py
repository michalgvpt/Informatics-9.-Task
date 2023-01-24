from PIL import Image

def grey(x, y):
    sf=int(sum(pixels[x, y])/3)
    pixels[x, y] = (sf, sf, sf)

img=Image.open('steneography/dolphin.jpg')
pixels=img.load()

for i in range(img.size[1]-1):
    for j in range(1, img.size[0]-1):
        grey(j, i)
        odlP = list(pixels[j, i])
        pix = []
        error = []
        num_of_colour = 1
        for f in odlP:
            pix.append(int(round(num_of_colour * f / 255) * (255/num_of_colour)))
            error.append(f-pix[-1])
        pixels[j, i] = tuple(pix)
        dit_pix_1 = []
        dit_pix_2 = []
        dit_pix_3 = []
        dit_pix_4 = []
        for a in range(3):
            dit_pix_1.append(int(list(pixels[j+1, i+1])[a] + error[a] * 7/16))
        for b in range(3):
            dit_pix_2.append(int(list(pixels[j-1, i+1])[b] + error[b] * 3/16))
        for c in range(3):
            dit_pix_3.append(int(list(pixels[j+1, i+1])[c] + error[c] * 5/16))
        for d in range(3):
            dit_pix_4.append(int(list(pixels[j+1, i+1])[d] + error[d] * 1/16))
        pixels[j+1, i+1] = tuple(dit_pix_1)
        pixels[j-1, i+1] = tuple(dit_pix_2)
        pixels[j+1, i+1] = tuple(dit_pix_3)
        pixels[j+1, i+1] = tuple(dit_pix_4)

img.show()