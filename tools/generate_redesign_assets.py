#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFilter
from pathlib import Path
import math, random

ROOT = Path(__file__).resolve().parents[1]
CREAM=(247,245,240,255); ORANGE=(242,103,58,255); ORANGE2=(255,139,95,255)
PURPLE=(123,97,209,255); BLUE=(57,136,214,255); GREEN=(35,154,104,255); YELLOW=(241,184,59,255)
INK=(54,45,58,255); WHITE=(255,255,255,255); TRAN=(0,0,0,0)
random.seed(7)

def canvas(size, bg=TRAN): return Image.new('RGBA', size, bg)
def rr(d, box, r, fill, outline=None, width=1): d.rounded_rectangle(box, r, fill=fill, outline=outline, width=width)
def ellipse(d, box, fill, outline=None, width=1): d.ellipse(box, fill=fill, outline=outline, width=width)
def shadow(im, box, r=28, alpha=55, blur=22):
    lay=Image.new('RGBA', im.size, TRAN); ld=ImageDraw.Draw(lay); rr(ld, box, r, (50,35,30,alpha)); lay=lay.filter(ImageFilter.GaussianBlur(blur)); im.alpha_composite(lay)
def sparkle(d,x,y,s,c):
    pts=[(x,y-s),(x+s*.28,y-s*.28),(x+s,y),(x+s*.28,y+s*.28),(x,y+s),(x-s*.28,y+s*.28),(x-s,y),(x-s*.28,y-s*.28)]
    d.polygon(pts, fill=c)
def gradient(size, top, bottom):
    w,h=size; im=Image.new('RGBA',size); p=im.load()
    for y in range(h):
        t=y/max(1,h-1); col=tuple(round(top[i]*(1-t)+bottom[i]*t) for i in range(4))
        for x in range(w): p[x,y]=col
    return im

def draw_tv(im, cx, cy, scale=1.0, glasses=False, popcorn=False, magnifier=False):
    d=ImageDraw.Draw(im); w=int(300*scale); h=int(235*scale); x=cx-w//2; y=cy-h//2
    shadow(im,(x+18,y+32,x+w-8,y+h+35),int(32*scale),50,int(18*scale))
    d.line((cx-55*scale,y+15*scale,cx-92*scale,y-35*scale),fill=(116,126,145,255),width=max(4,int(8*scale)))
    d.line((cx+55*scale,y+15*scale,cx+92*scale,y-35*scale),fill=(116,126,145,255),width=max(4,int(8*scale)))
    ellipse(d,(cx-103*scale,y-47*scale,cx-81*scale,y-25*scale),PURPLE); ellipse(d,(cx+81*scale,y-47*scale,cx+103*scale,y-25*scale),PURPLE)
    rr(d,(x,y+5*scale,x+w,y+h),int(48*scale),ORANGE, (195,70,25,255), max(2,int(5*scale)))
    rr(d,(x+28*scale,y+40*scale,x+w-28*scale,y+h-48*scale),int(36*scale),(255,245,212,255),(211,82,37,255),max(2,int(4*scale)))
    # eyes / glasses
    if glasses:
        rr(d,(cx-105*scale,cy-38*scale,cx-8*scale,cy+28*scale),int(16*scale),(62,142,219,230),INK,max(2,int(5*scale)))
        rr(d,(cx+8*scale,cy-38*scale,cx+105*scale,cy+28*scale),int(16*scale),(222,73,74,225),INK,max(2,int(5*scale)))
        d.line((cx-8*scale,cy-5*scale,cx+8*scale,cy-5*scale),fill=INK,width=max(2,int(5*scale)))
    else:
        ellipse(d,(cx-71*scale,cy-34*scale,cx-35*scale,cy+10*scale),INK); ellipse(d,(cx+35*scale,cy-34*scale,cx+71*scale,cy+10*scale),INK)
        ellipse(d,(cx-62*scale,cy-27*scale,cx-52*scale,cy-17*scale),WHITE); ellipse(d,(cx+44*scale,cy-27*scale,cx+54*scale,cy-17*scale),WHITE)
    # smile
    d.arc((cx-42*scale,cy-2*scale,cx+42*scale,cy+55*scale),0,180,fill=(115,44,47,255),width=max(3,int(7*scale)))
    ellipse(d,(cx-86*scale,cy+10*scale,cx-66*scale,cy+27*scale),(255,151,128,255)); ellipse(d,(cx+66*scale,cy+10*scale,cx+86*scale,cy+27*scale),(255,151,128,255))
    # feet
    rr(d,(cx-95*scale,y+h-10*scale,cx-35*scale,y+h+30*scale),int(18*scale),ORANGE,(195,70,25,255),max(2,int(4*scale)))
    rr(d,(cx+35*scale,y+h-10*scale,cx+95*scale,y+h+30*scale),int(18*scale),ORANGE,(195,70,25,255),max(2,int(4*scale)))
    if magnifier:
        ellipse(d,(cx+25*scale,cy-65*scale,cx+112*scale,cy+22*scale),(205,235,248,150),BLUE,max(2,int(9*scale)))
        d.line((cx+92*scale,cy+8*scale,cx+135*scale,cy+60*scale),fill=(36,85,160,255),width=max(3,int(13*scale)))
    if popcorn:
        bx=cx+72*scale; by=cy+55*scale
        rr(d,(bx,by,bx+93*scale,by+98*scale),int(12*scale),(250,244,229,255),(166,57,46,255),max(2,int(4*scale)))
        for k in range(5):
            d.rectangle((bx+(10+17*k)*scale,by+10*scale,bx+(18+17*k)*scale,by+90*scale),fill=(224,67,57,255))
        for k in range(10):
            px=bx+(8+(k*17)%86)*scale; py=by-(8+(k%3)*11)*scale
            ellipse(d,(px,py,px+25*scale,py+25*scale),(255,220,91,255),(220,157,44,255),max(1,int(2*scale)))

def person(im,cx,cy,scale,skin,shirt,hair):
    d=ImageDraw.Draw(im)
    # torso
    rr(d,(cx-48*scale,cy+35*scale,cx+48*scale,cy+150*scale),int(30*scale),shirt)
    # neck/head
    rr(d,(cx-11*scale,cy+21*scale,cx+11*scale,cy+50*scale),int(7*scale),skin)
    ellipse(d,(cx-42*scale,cy-54*scale,cx+42*scale,cy+35*scale),skin)
    # hair cap
    d.pieslice((cx-44*scale,cy-62*scale,cx+44*scale,cy+18*scale),180,355,fill=hair)
    # eyes + smile
    ellipse(d,(cx-20*scale,cy-13*scale,cx-11*scale,cy-3*scale),INK); ellipse(d,(cx+11*scale,cy-13*scale,cx+20*scale,cy-3*scale),INK)
    d.arc((cx-17*scale,cy-3*scale,cx+17*scale,cy+22*scale),0,180,fill=(130,62,58,255),width=max(2,int(3*scale)))
    # legs
    rr(d,(cx-37*scale,cy+130*scale,cx-5*scale,cy+215*scale),int(14*scale),(62,87,120,255))
    rr(d,(cx+5*scale,cy+130*scale,cx+37*scale,cy+215*scale),int(14*scale),(62,87,120,255))

def hero():
    im=gradient((1792,1024),(255,242,216,255),(247,224,190,255)); d=ImageDraw.Draw(im)
    # calm room architecture
    d.rectangle((0,720,1792,1024),fill=(238,191,137,255)); d.rectangle((0,710,1792,730),fill=(225,169,114,255))
    # window
    rr(d,(1450,185,1725,570),24,(255,250,222,220),(230,181,112,255),7); d.line((1588,185,1588,570),fill=(230,181,112,255),width=6); d.line((1450,375,1725,375),fill=(230,181,112,255),width=6)
    # plants
    ellipse(d,(128,580,215,700),(60,157,102,255)); ellipse(d,(172,540,248,690),(52,145,93,255)); rr(d,(150,675,230,738),14,(178,116,78,255))
    ellipse(d,(1330,555,1420,705),(45,147,84,255)); ellipse(d,(1390,520,1480,705),(61,158,93,255)); rr(d,(1360,685,1450,748),14,(135,88,152,255))
    # sofa
    shadow(im,(360,500,1100,800),42,45,28); rr(d,(350,470,1110,790),55,(221,112,61,255)); rr(d,(390,510,1070,760),45,(237,132,71,255))
    person(im,620,485,1.0,(239,174,128,255),(41,142,91,255),(77,46,31,255))
    person(im,780,430,1.25,(225,153,110,255),(92,86,183,255),(75,40,27,255))
    person(im,940,485,1.0,(192,126,91,255),(241,177,56,255),(83,45,29,255))
    draw_tv(im,1210,630,0.82,magnifier=False)
    # subtle floating motifs in middle band
    for x,y,c in [(300,380,PURPLE),(1240,370,YELLOW),(1370,430,BLUE),(210,430,YELLOW),(1510,460,GREEN),(1090,340,PURPLE)]: sparkle(d,x,y,16,c)
    # paper planes
    for x,y,c in [(410,330,PURPLE),(1300,350,ORANGE2)]: d.polygon([(x,y),(x+70,y+24),(x+18,y+48),(x+30,y+25)],fill=c)
    # blank program cards
    for x,y,c in [(220,390,(178,154,226,220)),(1110,410,(104,177,220,220)),(1490,350,(134,193,112,220))]: rr(d,(x,y,x+90,y+58),13,c)
    im.convert('RGB').save(ROOT/'hero.png',optimize=True)

def empty_asset():
    im=canvas((1024,1024)); draw_tv(im,480,510,1.55,magnifier=True); d=ImageDraw.Draw(im)
    for x,y,c in [(780,320,YELLOW),(830,430,PURPLE),(735,470,GREEN)]: sparkle(d,x,y,28,c)
    im.save(ROOT/'leer.png',optimize=True)

def cinema():
    im=canvas((1024,1024)); glow=Image.new('RGBA',im.size,TRAN); gd=ImageDraw.Draw(glow)
    gd.ellipse((110,100,930,930),fill=(73,59,115,215)); glow=glow.filter(ImageFilter.GaussianBlur(32)); im.alpha_composite(glow)
    d=ImageDraw.Draw(im); rr(d,(140,145,884,820),75,(73,59,115,235),(111,83,160,230),8)
    for i in range(45):
        x=random.randint(190,840); y=random.randint(180,730); r=random.choice([2,3,5]); ellipse(d,(x-r,y-r,x+r,y+r),random.choice([YELLOW,WHITE,PURPLE]))
    draw_tv(im,500,520,1.35,glasses=True,popcorn=True)
    im.save(ROOT/'kino.png',optimize=True)

def icon_base(): return canvas((1024,1024))
def save_icon(im,name): im.save(ROOT/name,optimize=True)

def wissen():
    im=icon_base(); d=ImageDraw.Draw(im)
    ellipse(d,(215,190,720,695),(224,242,250,120),BLUE,34); d.line((620,610,810,800),fill=(35,78,148,255),width=62)
    # bulb
    ellipse(d,(350,280,580,520),YELLOW,(217,137,35,255),22); rr(d,(420,500,515,610),24,(141,99,72,255)); d.arc((405,330,530,470),180,355,fill=ORANGE,width=16)
    # planet
    ellipse(d,(210,650,390,830),ORANGE2); d.arc((175,680,430,790),165,350,fill=PURPLE,width=28)
    sparkle(d,720,245,28,PURPLE); sparkle(d,250,500,20,GREEN); save_icon(im,'interesse-wissen.png')

def tiere():
    im=icon_base(); d=ImageDraw.Draw(im)
    # fox
    ellipse(d,(170,280,565,690),ORANGE,(170,72,30,255),18); d.polygon([(205,350),(230,155),(355,315)],fill=ORANGE); d.polygon([(505,350),(485,155),(370,315)],fill=ORANGE)
    ellipse(d,(255,430,475,650),(255,238,205,255)); ellipse(d,(310,420,338,450),INK); ellipse(d,(395,420,423,450),INK); ellipse(d,(353,480,385,505),INK)
    # tail
    ellipse(d,(120,580,440,835),ORANGE); ellipse(d,(115,675,270,830),(255,238,205,255))
    # bird
    ellipse(d,(565,450,825,760),YELLOW,(218,145,34,255),16); ellipse(d,(650,525,676,555),INK); d.polygon([(690,585),(748,603),(690,620)],fill=ORANGE); ellipse(d,(625,680,655,715),ORANGE); ellipse(d,(730,680,760,715),ORANGE)
    sparkle(d,770,330,25,PURPLE); sparkle(d,160,430,23,YELLOW); save_icon(im,'interesse-tiere.png')

def magie():
    im=icon_base(); d=ImageDraw.Draw(im)
    # hat
    ellipse(d,(220,560,820,760),(44,40,57,255),(20,18,27,255),18); rr(d,(330,380,710,690),45,(42,38,55,255),(20,18,27,255),18); rr(d,(335,555,705,625),15,BLUE)
    for x,y,s,c in [(505,255,70,YELLOW),(665,315,55,PURPLE),(385,345,40,GREEN),(570,410,25,ORANGE2)]: sparkle(d,x,y,s,c)
    d.arc((355,255,675,625),70,245,fill=YELLOW,width=28); save_icon(im,'interesse-magie.png')

def abenteuer():
    im=icon_base(); d=ImageDraw.Draw(im)
    # map
    rr(d,(190,410,790,770),42,(250,226,176,255),(190,130,67,255),18); d.line((320,430,340,745),fill=(213,165,103,255),width=8); d.line((590,430,575,745),fill=(213,165,103,255),width=8)
    d.line((285,650,400,560,520,625,650,510),fill=ORANGE,width=18); sparkle(d,650,510,28,ORANGE)
    # telescope
    d.line((270,350,700,220),fill=ORANGE,width=88); d.line((430,300,610,245),fill=BLUE,width=78); ellipse(d,(655,175,785,305),BLUE,(220,154,48,255),20)
    # compass
    ellipse(d,(605,610,855,860),(255,239,195,255),(198,131,48,255),24); d.polygon([(730,655),(760,765),(705,730)],fill=ORANGE); d.polygon([(730,815),(700,710),(755,745)],fill=BLUE)
    save_icon(im,'interesse-abenteuer.png')

def lachen():
    im=icon_base(); d=ImageDraw.Draw(im)
    ellipse(d,(235,215,790,790),YELLOW,(220,144,37,255),22); d.arc((335,345,460,480),190,350,fill=INK,width=22); d.arc((565,345,690,480),190,350,fill=INK,width=22)
    d.pieslice((365,410,665,700),0,180,fill=(105,45,48,255)); ellipse(d,(430,570,600,680),(242,111,93,255))
    for x,y,c in [(175,285,PURPLE),(825,300,GREEN),(165,650,ORANGE),(845,675,BLUE),(340,835,GREEN),(690,845,PURPLE)]:
        d.polygon([(x,y),(x+35,y+12),(x+22,y+42),(x-10,y+28)],fill=c)
    sparkle(d,780,520,28,PURPLE); sparkle(d,250,525,22,GREEN); save_icon(im,'interesse-lachen.png')

def musik():
    im=icon_base(); d=ImageDraw.Draw(im)
    # radio
    rr(d,(220,360,760,730),62,ORANGE,(178,65,27,255),20); rr(d,(285,420,635,630),45,(255,245,213,255)); ellipse(d,(655,445,720,510),YELLOW); ellipse(d,(655,545,720,610),YELLOW)
    d.line((300,350,530,210),fill=(110,121,141,255),width=18); ellipse(d,(515,195,545,225),PURPLE)
    # notes
    for x,y,c in [(180,250,YELLOW),(770,235,PURPLE),(785,650,GREEN)]:
        ellipse(d,(x,y+70,x+50,y+120),c); d.line((x+45,y+85,x+45,y),fill=c,width=24); d.line((x+45,y,x+105,y+35),fill=c,width=24)
    sparkle(d,200,530,20,YELLOW); sparkle(d,800,470,20,PURPLE); save_icon(im,'interesse-musik.png')

if __name__=='__main__':
    hero(); empty_asset(); cinema(); wissen(); tiere(); magie(); abenteuer(); lachen(); musik()
    for name in ['hero.png','leer.png','kino.png','interesse-wissen.png','interesse-tiere.png','interesse-magie.png','interesse-abenteuer.png','interesse-lachen.png','interesse-musik.png']:
        p=ROOT/name; im=Image.open(p); print(name, im.size, im.mode)
