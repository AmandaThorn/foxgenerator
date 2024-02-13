import tkinter as tk
import requests
from PIL import Image, ImageTk

response = requests.get("https://randomfox.ca/floof")
filename = 'foxyyy.png'



def image_call():
    filename = 'foxyyy.png'
    response = requests.get("https://randomfox.ca/floof")

    response_lib = response.json()
    fox_url = response_lib['image']
    print(fox_url)

    image = requests.get(fox_url)

    if image.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(image.content)
def image_update():
    try:
        foxy_image = Image.open("foxyyy.png")
        global converted_image
        converted_image = ImageTk.PhotoImage(foxy_image)
    except Exception as e:
        print('Error', e)



def on_button_click():
    label.config(text='Generating Foxes :3')
#image is overwritten with new random fox image
    image_call()
    image_update()
#updates the image to the new image
    Label2.config(image=converted_image)

#updates the origina box
    box.update()







box = tk.Tk()
box.title('testing')
box.geometry('400x300')
box.resizable(True, True)


# Opening Image from Foxy Program

try:
    foxy_image = Image.open("foxyyy.png")
    converted_image = ImageTk.PhotoImage(foxy_image)
except Exception as e:
    print('Error', e)





label = tk.Label(box, text = 'Welcome to the Fox Program!')
label.pack()

button = tk.Button(box, text = 'click me to generate foxes', command = on_button_click)
button.pack()

Label2 = tk.Label(box, image=converted_image)
Label2.pack()


box.mainloop()

