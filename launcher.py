import tkinter as tk
from PIL import Image, ImageTk
import launcher_mqtt 


def show_overlay(image_path):
    overlay = tk.Tk()
    overlay.title("Overlay")
    overlay.attributes('-topmost', 1) 
    overlay.overrideredirect(True)  
    try:
        image = Image.open(image_path)
        image = image.resize((600, 400), Image.Resampling.LANCZOS)  # Подгоняем размер изображения
        photo = ImageTk.PhotoImage(image)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{image_path}' не найден.")
        overlay.destroy()
        return

 
    screen_width = overlay.winfo_screenwidth()
    screen_height = overlay.winfo_screenheight()

    window_width = 600
    window_height = 400
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)

    overlay.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")


    canvas = tk.Canvas(overlay, width=window_width, height=window_height, highlightthickness=0, bd=0)
    canvas.pack()

    canvas.create_image(0, 0, anchor="nw", image=photo)

    canvas.create_text(window_width // 2, window_height - 20, text="pixeltoo", font=("Arial", 24), fill="white")


    overlay.after(5000, lambda: overlay.destroy())
    overlay.mainloop()


    launcher_mqtt.main()

# Основной код
if __name__ == "__main__":
    image_path = "icon.png"  
    show_overlay(image_path)
