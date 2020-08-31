from PIL import Image, ImageDraw, ImageFont
import qrcode
import textwrap


def make_qr(place):
    img = Image.open("template_level2.png")
    draw = ImageDraw.Draw(img)
    text_size = 65
    text_font = ImageFont.truetype("fonts/OpenSans-ExtraBold.ttf", text_size, encoding='utf-8')

    # бэкграунд
    draw.rectangle((85, 1345, 565, 1435), fill=(255, 231, 7))

    text2 = place[3]
    name_hight, name_width = text_font.getsize(text=text2)

    draw.rectangle((85, 1450, 85+name_hight+80, 1540), fill=(255, 231, 7))
    draw.rectangle((85, 1555, 565, 1645), fill=(255, 231, 7))
    draw.rectangle((85, 1660, 565, 1750), fill=(255, 231, 7))


#текст
    text1_coords = (110, 1340)
    text2_coords = (110, 1450)
    text3_coords = (110, 1555)
    text4_coords = (110, 1660)

    text = place[2]
    text1 = text[0:10]
    text2 = place[3]
    text3 = place[4][0:6]
    text4 = place[4][6:]
    draw.text(text1_coords, text=text1, font=text_font, fill="#000")
    draw.text(text2_coords, text=text2, font=text_font, fill="#000")
    draw.text(text3_coords, text=text3, font=text_font, fill="#000")
    draw.text(text4_coords, text=text4, font=text_font, fill="#000")


#картинка
    watermark = Image.open('3d-house.png')
    img.paste(watermark, (750,1400), watermark)

#qr код
    qr_coord = (410, 165)
    qr_size = 675

    qr_img = qrcode.make(place[1], border=1)
    qr_img = qr_img.resize((qr_size, qr_size))

    img.paste(qr_img, qr_coord)
    img.save(f"qr_result_2/qr_{place[0]}.png", "PNG")




places = [
    ["Google","www.google.com/search/putin", "Оплати в","Шанхай сити","через Balance!"],
    ["TPDNE", "https//www.thispersondoesnotexists.com", "Оплати в","Опен санс сити","через Balance!"],
    ["QwertyUiop", "https//www.thispersondoesnotexists.com", "Оплати в","GOOGLE","через Balance!"],
]

for place in places:
    make_qr(place)