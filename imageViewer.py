from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Image Viewer")
root.iconphoto(True, PhotoImage(file="icon.png"))

my_img_1 = Image.open("/home/soumyo/PycharmProjects/Image Viewer/images/pic1.jpg")  # Opening the original image
my_img_1 = my_img_1.resize((300, 303), Image.ANTIALIAS)  # Resize the original image
IMG_1 = ImageTk.PhotoImage(my_img_1)  # Storing the resized image

my_img_2 = Image.open("/home/soumyo/PycharmProjects/Image Viewer/images/pic2.jpg")
my_img_2 = my_img_2.resize((384, 512), Image.ANTIALIAS)
IMG_2 = ImageTk.PhotoImage(my_img_2)

my_img_3 = Image.open("/home/soumyo/PycharmProjects/Image Viewer/images/pic3.jpg")
my_img_3 = my_img_3.resize((384, 512), Image.ANTIALIAS)
IMG_3 = ImageTk.PhotoImage(my_img_3)

my_img_4 = Image.open("/home/soumyo/PycharmProjects/Image Viewer/images/pic4.jpg")
my_img_4 = my_img_4.resize((446, 594), Image.ANTIALIAS)
IMG_4 = ImageTk.PhotoImage(my_img_4)

my_img_5 = Image.open("/home/soumyo/PycharmProjects/Image Viewer/images/pic5.jpg")
my_img_5 = my_img_5.resize((518, 388), Image.ANTIALIAS)
IMG_5 = ImageTk.PhotoImage(my_img_5)

img_list = [IMG_1, IMG_2, IMG_3, IMG_4, IMG_5]  # Storing images inside a list

img_label = Label(root, image=IMG_1)  # Defining image label
img_label.grid(row=0, column=0, columnspan=4)

status_label = Label(root, text="1 of 5", bd=2, relief="sunken")  # Adding status bar
status_label.grid(row=1, column=1)


# Creating Functions
def forward(image_number):  # Adding attribute to the function
    global img_label
    global forward_btn
    global back_btn
    global status_label

    img_label.grid_forget()
    img_label = Label(image=img_list[image_number - 1])

    status_label = Label(root, text=str(image_number) + " of 5", bd=2,
                         relief="sunken")  # Updating the status bar status
    status_label.grid(row=1, column=1)

    forward_btn = Button(root, text=">>", command=lambda: forward(image_number + 1))  # Updating the forward button
    back_btn = Button(root, text="<<", command=lambda: backward(image_number - 1))  # Updating the backward button

    if image_number == 5:
        forward_btn = Button(root, text=">>", state=DISABLED)

    forward_btn.grid(row=1, column=2)
    back_btn.grid(row=1, column=0)
    img_label.grid(row=0, column=0, columnspan=4)


def backward(image_number):
    global img_label
    global forward_btn
    global back_btn
    global status_label

    img_label.grid_forget()
    img_label = Label(image=img_list[image_number - 1])

    status_label = Label(root, text=str(image_number) + " of 5", bd=2, relief="sunken")  # Updating the status bar status
    status_label.grid(row=1, column=1)

    forward_btn = Button(root, text=">>", command=lambda: forward(image_number + 1))  # Updating the forward button
    back_btn = Button(root, text="<<", command=lambda: backward(image_number - 1))  # Updating the backward button

    if image_number == 1:
        back_btn = Button(root, text="<<", state=DISABLED)

    forward_btn.grid(row=1, column=2)
    back_btn.grid(row=1, column=0)
    img_label.grid(row=0, column=0, columnspan=4)


# Adding Button
back_btn = Button(root, text="<<", command=backward, state=DISABLED)
back_btn.grid(row=1, column=0)

forward_btn = Button(root, text=">>", command=lambda: forward(2))  # Passing the value to the function attribute
forward_btn.grid(row=1, column=2)

exit_btn = Button(root, text="Quit", command=root.quit)
exit_btn.grid(row=1, column=3)

root.mainloop()
