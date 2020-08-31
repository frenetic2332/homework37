from PIL import Image, ImageDraw, ImageFont
import qrcode


def make_qr(place):
    text_size = 68
    img = Image.open("template_level1.jpg")
    text_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", text_size, encoding='utf-8')
    text_coords = (435, 1465)

    text = place[0]
    if len(text) >= 10:
        text = text[0:10]

    draw = ImageDraw.Draw(img)
    draw.text(text_coords, text=text, font=text_font, fill="#000")
    qr_coord = (338, 487)
    qr_size = 571

    qr_img = qrcode.make(place[1], border=1)
    qr_img = qr_img.resize((qr_size, qr_size))

    img.paste(qr_img, qr_coord)
    img.save(f"qr_results/qr_{place[0]}.png", "PNG")




places = [
    ["Google","www.google.com/search/putin"],
    ["TPDNE", "https//www.thispersondoesnotexists.com"],
    ["QwertyUiop", "https//www.thispersondoesnotexists.com"],
]

for place in places:
    make_qr(place)

    