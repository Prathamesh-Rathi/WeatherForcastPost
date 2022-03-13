import requests
import json
from PIL import Image , ImageFont , ImageDraw
from datetime import date

api_key = "Your API key"
india_list  = ["Jaipur" , "Mumbai" , "Hyderabad" , "Delhi" , "Chennai"]
uk_list = ["London" , "Manchester", "Edinburgh" , "Bristol" , "Birmingham"]
us_list = ["New York" , "Chicago" , "San Francisco" , "Los Angeles" , "San Diego"]
country_list = [india_list , uk_list , us_list]
position = [300 , 430 , 555 , 690 , 820]

#print(data)
for country in country_list:
    my_image = Image.open("post1.png")
    draw = ImageDraw.Draw(my_image)

    title_font = ImageFont.truetype('inter.ttf', size=50)
    content = "Todays Weather Forecast"
    color = 'rgb(255 ,255, 255)'
    draw.text((55,60) , content , color , font=title_font)

    title_font = ImageFont.truetype('inter.ttf', size=30)
    content = date.today().strftime("%A - %B %d , %Y")
    color = 'rgb(255 ,255, 255)'
    draw.text((55,145) , content , color , font=title_font)

    index = 0
    for city in country:
        url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid= your api id &units=metric".format(city)
        responce = requests.get(url)
        data = json.loads(responce.text)

        title_font = ImageFont.truetype('inter.ttf', size=60)
        color = 'rgb(0,0,0)'
        draw.text((135,position[index]) , city , color , font=title_font)

        title_font = ImageFont.truetype('inter.ttf', size=50)
        content = str(data['main']['temp']) + "\u00b0"
        color = 'rgb(255 ,255, 255)'
        draw.text((600,position[index]) , content , color , font=title_font)

        title_font = ImageFont.truetype('inter.ttf', size=50)
        content = str(data['main']['humidity']) + "%"
        color = 'rgb(255 ,255, 255)'
        draw.text((810,position[index]) , content , color , font=title_font)

        index += 1




    my_image.save(str(date.today()) +  country[0] + ".png")
