import cv2
import numpy as np
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

# Função para abrir o seletor de arquivos
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp"), ("All files", "*.*")]
    )
    return file_path

# Função para equalizar o histograma em escala de cinza
def equalize_histogram():
    file_path = open_file()
    if file_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        equalized_image = cv2.equalizeHist(image)
        show_images(image, equalized_image, "Equalized Grayscale Image")

# Função para negativo da imagem em escala de cinza
def negative_image():
    file_path = open_file()
    if file_path:
        image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        negative = 255 - image
        show_images(image, negative, "Negative Grayscale Image")

# Função para equalizar o histograma de uma imagem colorida (RGB)
def equalize_histogram_color():
    file_path = open_file()
    if file_path:
        image = cv2.imread(file_path)
        # Separar canais de cores
        channels = cv2.split(image)
        equalized_channels = [cv2.equalizeHist(c) for c in channels]
        equalized_image = cv2.merge(equalized_channels)
        show_images(image, equalized_image, "Equalized Color Image")

# Função para exibir a imagem original e a imagem processada
def show_images(original_image, processed_image, title):
    # Exibir imagem original
    image_rgb_original = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB) if len(original_image.shape) == 3 else original_image
    im_pil_original = Image.fromarray(image_rgb_original)
    im_pil_original.thumbnail((400, 400))  # Reduz o tamanho para visualização
    im_tk_original = ImageTk.PhotoImage(im_pil_original)
    
    original_image_label.configure(image=im_tk_original)
    original_image_label.image = im_tk_original
    
    # Exibir imagem processada
    image_rgb_processed = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB) if len(processed_image.shape) == 3 else processed_image
    im_pil_processed = Image.fromarray(image_rgb_processed)
    im_pil_processed.thumbnail((400, 400))  # Reduz o tamanho para visualização
    im_tk_processed = ImageTk.PhotoImage(im_pil_processed)
    
    processed_image_label.configure(image=im_tk_processed)
    processed_image_label.image = im_tk_processed
    
    root.title(title)

# Criar a interface com customtkinter
ctk.set_appearance_mode("dark")
root = ctk.CTk()
root.title("Atividade 01 - Processamento de Imagens")

# Label para exibir a imagem original
original_image_label = ctk.CTkLabel(root, text="")
original_image_label.pack(pady=10)

# Label para exibir a imagem processada
processed_image_label = ctk.CTkLabel(root, text="")
processed_image_label.pack(pady=10)

# Botão para equalizar o histograma (escala de cinza)
button1 = ctk.CTkButton(root, text="Equalizar o Histograma (Escala de Cinza)", command=equalize_histogram)
button1.pack(pady=10)

# Botão para negativo da imagem (escala de cinza)
button2 = ctk.CTkButton(root, text="Imagem Negativa (Escala de Cinza)", command=negative_image)
button2.pack(pady=10)

# Botão para equalizar o histograma (imagem colorida)
button3 = ctk.CTkButton(root, text="Equalizar o Histograma (Colorido)", command=equalize_histogram_color)
button3.pack(pady=10)

root.geometry("500x800")
root.mainloop()
