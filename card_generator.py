from PIL import Image, ImageFont, ImageDraw

def text_from_right(draw: ImageDraw, font: ImageFont, text, color, coords):
    text_width, text_height = font.getsize(text)
    coords = (coords[0] - text_width, coords[1])
    draw.text(coords, text, fill=color, font=font)

def make_and_save_card(person):
    template = Image.open("level0_template.jpg")

    name_font = ImageFont.truetype("fonts/OpenSans-Light.ttf", 50)
    last_name_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 50)
    title_font = ImageFont.truetype("fonts/OpenSans-SemiBold.ttf", 20)
    email_font = ImageFont.truetype("fonts/Poppins-Regular.ttf", 20)
    phone_number1_font = ImageFont.truetype("fonts/Poppins-Regular.ttf", 20)
    street_font = ImageFont.truetype("fonts/Poppins-Regular.ttf", 20)
    web_site_font = ImageFont.truetype("fonts/Poppins-Regular.ttf", 20)

    name_coords = (555, 265)
    last_name_coords = (555, 336)
    title_coords = (555, 413)
    email_coords = (760, 250)
    phone_number1_coords = (760, 330)
    street_coords = (760, 425)
    web_site_coords = (760, 510)

    draw = ImageDraw.Draw(template)

    text_from_right(draw, name_font, person[0].upper(), "#FFF", name_coords)
    text_from_right(draw, last_name_font, person[1].upper(), "#FFF", last_name_coords)
    text_from_right(draw, title_font, person[2].upper(), "#F00", title_coords)

    draw.text(email_coords, text=person[3], font=email_font)
    draw.text(phone_number1_coords, text=person[4], font=phone_number1_font)
    draw.text(street_coords, text=person[5], font=street_font)
    draw.text(web_site_coords, text=person[6], font=web_site_font)


    template.save(f"results/card_{person[0]}_{person[1]}.png", "PNG")


persons = [
    ["Alisher", "Alikulov", "Software Developer", "masteraalish@gmail.com", "+996 776 900 413", "Kyrgyzstan, Bishkek", "www.master.com"],
    ["Isaac", "Asimov", "Writer", "isaacaazimov@gmail.com", "+996 706 900 413", "USA, Manhattan, New York city", "www.asimov.fb"],
    ["George", "Lucas", "Film producer", "gorge@lucasfilm.com", "+8 79938 38837", "USA, California", "lucasfilm.com"],
]

for person in persons:
    make_and_save_card(person)