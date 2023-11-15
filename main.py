from datetime import datetime, timedelta
from drive import Drive


def rda():
    now = datetime.now()
    timenow1 = now + timedelta(seconds=1)  # Cria o atilho

    while True:  # Loop inifito em formato de Switch Case
        now = datetime.now()
        if now >= timenow1:
            try:
                site = 'https://drive.google.com/file/d/15aoRtRgCoxC7rgE5g3YDKHuuWVVvJbub/view'
                nome_documento = 'renault-kardian.jpg'
                rda1 = Drive(site, nome_documento)
                rda1.exec_rda()
                rda1 = None
            except:  # Informa no console qual fluxo deu erro (Serve também para locais isolados)
                print(f"Erro no RDA 1 - {datetime.now()}")
                pass
            timenow1 = now + timedelta(minutes=1)


if __name__ == '__main__':
    rda()
