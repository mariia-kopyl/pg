import sys

# definice úvodních binárních sekvencí obrázkových souborů
jpeg_header = b'\xff\xd8'
gif_header1 = b'GIF87a'
gif_header2 = b'GIF89a'
png_header = b'\x89PNG\r\n\x1a\n'


def read_header(file_name, header_length):
    """
    Načte binární soubor z cesty file_name,
    přečte prvních header_length bytů a vrátí je
    """
    with open(file_name, "rb") as soubor: 
        header = soubor.read(header_length)
    return header


def is_jpeg(file_name):
    """
    Porovná hlavičku souboru s hlavičkou JPEG
    """
    header = read_header(file_name, len(jpeg_header))
    return header == jpeg_header


def is_gif(file_name):
    """
    Porovná hlavičku souboru s hlavičkami GIF87a a GIF89a
    """
    header = read_header(file_name, len(gif_header1))
    return header in (gif_header1, gif_header2)


def is_png(file_name):
    """
    Porovná hlavičku souboru s hlavičkou PNG
    """
    header = read_header(file_name, len(png_header))
    return header == png_header


def print_file_type(file_name):
    """
     Funkce vypíše typ souboru - tuto funkci není třeba upravovat
    """
    if is_jpeg(file_name):
        print(f"Soubor {file_name} je typu JPEG")
    elif is_gif(file_name):
        print(f"Soubor {file_name} je typu GIF")
    elif is_png(file_name):
        print(f"Soubor {file_name} je typu PNG")
    else:
        print(f"Soubor {file_name} je neznámého typu")


if __name__ == "__main__":
    try:
        file_name = sys.argv[1]
        print_file_type(file_name)
    except IndexError:
        print("Nebyl zadán název souboru")
    except FileNotFoundError:
        print("Soubor nebyl nalezen")
    except Exception as e:
        print(f"Došlo k chybě: {e}")
