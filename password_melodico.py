import hashlib
import pygame
import time

def generar_melodia(frase):
    notas = {
        'a': 'do', 'b': 're', 'c': 'mi', 'd': 'fa',
        'e': 'sol', 'f': 'la', 'g': 'si', 'h': 'do#',
        'i': 're#', 'j': 'mi#', 'k': 'fa#', 'l': 'sol#',
        'm': 'la#', 'n': 'si#', 'o': 'do', 'p': 're',
        'q': 'mi', 'r': 'fa', 's': 'sol', 't': 'la',
        'u': 'si', 'v': 'do#', 'w': 're#', 'x': 'mi#',
        'y': 'fa#', 'z': 'sol#', ' ': ' '
    }

    melodia = []
    for letra in frase:
        try:
            melodia.append(notas.get(letra.lower(), letra.lower()))
        except UnicodeEncodeError:
            melodia.append(' ')

    return melodia

def convertir_a_contraseña(melodia):
    # Convierte la melodía en una cadena usando SHA-256
    contraseña = hashlib.sha256(''.join(melodia).encode()).hexdigest()
    return contraseña

def reproducir_melodia(melodia):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.mixer.init()

    for nota in melodia:
        if nota != ' ':
            sound = pygame.mixer.Sound(f"notas/{nota}.wav")
            sound.play()
            time.sleep(0.5)  # Pausa entre notas
            pygame.time.wait(int(sound.get_length() * 1000))

    pygame.mixer.quit()

def main():
    # Ingresa una frase para generar la contraseña melódica
    frase = input("Ingresa una frase: ")

    # Genera la melodía y la contraseña
    melodia = generar_melodia(frase)
    contraseña = convertir_a_contraseña(melodia)

    # Muestra la melodía y la contraseña generada
    print(f"Melodía generada: {' '.join(melodia)}")
    print(f"Contraseña generada: {contraseña}")

    # Reproduce la melodía
    reproducir_melodia(melodia)

if __name__ == "__main__":
    main()
