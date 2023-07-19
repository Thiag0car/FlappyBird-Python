from PIL import Image

def alterar_cor_imagem(caminho_imagem):
    imagem = Image.open(caminho_imagem)
    imagem_rgb = imagem.convert("RGB")
    pixels = imagem_rgb.load()
    largura, altura = imagem.size

    # Define a cor alvo (verde) e a cor substituta (vermelho)
    cor_alvo = (0, 255, 0)  # Verde (RGB)
    cor_substituta = (255, 0, 0)  # Vermelho (RGB)

    # Percorre todos os pixels da imagem
    for i in range(largura):
        for j in range(altura):
            r, g, b = pixels[i, j]

            # Verifica se a cor do pixel é igual à cor alvo (verde)
            if (r, g, b) == cor_alvo:
                # Substitui a cor atual pela cor substituta (vermelho)
                pixels[i, j] = cor_substituta

    # Salva a imagem modificada
    imagem_rgb.save("imagem_modificada.png")

# Exemplo de uso
caminho_imagem = "imgs/pipe.png"
alterar_cor_imagem(caminho_imagem)
