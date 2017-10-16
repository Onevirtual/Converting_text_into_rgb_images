
# coding: utf-8

#!/usr/bin/env python

#Creating a set of phonems images from the respective strings

import io
import os
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
text = """i y ɨ ʉ ɯ u ɪ ʏ ɪ̈ ʊ̈ ɯ̽ ʊ e ø ɘ ɵ ɤ o ə ɛ œ ɜ ɞ ʌ ɔ æ ɐ a ɶ ä ɑ ɒ





	m	 	ɱ	 	ŋ͡m	 	n̪	 	n	 	 	ɳ	 	 	ɲ	 	ŋ	 	ŋʷ	 	ɴ	 	 
m͡p	m͡b	 	ᵑk͡p	ᵑɡ͡b	n͡t̪	n͡d̪	n͡t	n͡d	 	ɳ͡ʈ	ɳ͡ɖ	 	ɲ͡c	ɲ͡ɟ	ŋ͡k	ŋ͡ɡ	 	ɴ͡q	ɴ͡ɢ	 	 
p	b	p̪	b̪	k͡p	ɡ͡b	t̪	d̪	t	d	 	ʈ	ɖ	 	c	ɟ	k	ɡ	kʷ	ɡʷ	q	ɢ	 	ʡ	 	ʔ	 	 
p͡ɸ	b͡β	p͡f	b͡v	 	t͡θ	d͡ð	t͡s	d͡z	t͡ʃ	d͡ʒ	ʈ͡ʂ	ɖ͡ʐ	t͡ɕ	d͡ʑ	c͡ç	ɟ͡ʝ	k͡x	ɡ͡ɣ	 	q͡χ	ɢ͡ʁ	 	ʡ͡ʜ	 	ʔ͡h	 	 
	m͡ɸ	m͡β	ɱ͡f	ɱ͡v	 	n͡θ	n͡ð	n͡s	n͡z	n͡ʃ	n͡ʒ	 	 	 	ŋ͡k	ŋ͡ɡ	 	 	 	 	 
	ɸ	β	f	v	 	θ	ð	s	z	ʃ	ʒ	ʂ	ʐ	ɕ	ʑ	ç	ʝ	x	ɣ	xʷ	ɣʷ	χ	ʁ	ħ	ʕ	ʜ	ʢ	h	ɦ	 
	 	β̞	 	ʋ	 		 	ð̞	 	ɹ	 	 	ɻ	 	 	j	 	ɰ	ʍ	w	 	 	 	 	 	 	 
	ʙ̥	ʙ	 	 	 	r̪	r̥	r	 	 		 	 	 	 	 	ʀ	 	 		 	 
	 		 	ⱱ	 	 	ɾ̪	 	ɾ	 	 	ɽ	 	 	 	 	 	 	 		 	 
	 	 	t͡ɬ	d͡ɮ	 	 	 	 	 	 	 	 	 	 	 	 	 	 
	 	 	ɬ	ɮ	 		 	 		 		 	 	 	 	 
	 	 	l̪	l̥	l	 	 	ɭ	 	 	ʎ	 	ʟ	 	 	 	 
 	 	 	ɺ	 	 		 	 		 		 	 	 	 
	ɓ̥	ɓ	 	 	 	ɗ̥	ɗ	 	 		 	ʄ̊	ʄ	ɠ̊	ɠ	 	ʛ̥	ʛ	 	 
pʼ	 	 	 	t̪ʼ	 	tʼ	 	 	ʈʼ	 	 	cʼ	 	kʼ	 	 	qʼ	 	 	 
ɸʼ	 	fʼ	 	 	θʼ	 	sʼ	 	ʃʼ	 	ʂʼ	 	ɕʼ	 	çʼ	 	xʼ	 	 	χʼ	 	 	 
ʘ	 	 	ǀ	 	ǃ	 	ǂ	 	 	 	 
 	 	ǁ	 	 	 	 	"""
texte1=[]

for m in text:
    texte1 = text.split()
    
phonems = ['[%s]'% x for x in texte1]


def create_image_of_given_text(phonem):
    img = Image.new('RGB',(100,50),(255,255,255))#Creates a new image
    fnt = ImageFont.truetype('Times New Roman.ttf', 20)
    d = ImageDraw.Draw(img)
    d.text((40,20),phonem,font=fnt, fill=(255,0,0))
    img.save("%s.png"%(phonem))

for m in phonems:
    create_image_of_given_text(m)


