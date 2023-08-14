from PIL import Image, ImageDraw, ImageFont

def main():
    for i in range(359):
        img2aa(f'frames/frame{i}.jpg', f'aaframes/frame{i}.jpg')
        print(i)

def img2aa(srcpath, distpath):
    img = Image.open(srcpath)
    w, h = img.size
    aa = Image.new(mode='RGB', size=(w,h), color=(255,255,255)) # new canvas
    ascii ='W#%*+;:,.  ' #0-25, 26-50, ..., 226-250, 251-255
    fontsize=10
    # font = ImageFont.truetype(font="C:\\Windows\\Fonts\\msgothic.ttc", size=fontsize, encoding='utf-8')
    pix = img.load()
    draw = ImageDraw.Draw(aa)
    for y in range(0, h, fontsize):
        for x in range(0, w, fontsize):
            r,g,b = pix[x,y]
            gray = r*0.2126 + g*0.7152 + b*0.0722
            char = ascii[int(gray//25)]
            # draw.text(xy=(x,y), text=char, fill='#000000', font=font)
            draw.text(xy=(x,y), text=char, fill='#000000')
    aa.save(distpath)


main()