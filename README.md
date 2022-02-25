<p align="center"><a href="https://t.me/VeezVideoBot"><img src="https://github.com/levina-lab/video-stream/raw/main/driver/veezlogo.png"></a></p>
<p align="center">
    <br><b>Video Stream è un Telegram Bot avanzato, questo ti consente di riprodurre video e musica su Telegram e Videochat di gruppo</b><br>
</p>
<p align="center">
    <a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-black.svg?style=flat-square&logo=python&logoColor=blue&color=red" /></a>
    <a href="https://github.com/SAIBYADAS/video-stream/graphs/commit-activity" alt="Maintenance"> <img src="https://img.shields.io/badge/Maintained%3F-yes-red.svg?style=flat-square" /></a>
    <a href="https://app.codacy.com/gh/SAIBYADAS/video-stream/dashboard"> <img src="https://img.shields.io/codacy/grade/a723cb464d5a4d25be3152b5d71de82d?color=red&logo=codacy&style=flat-square" alt="Codacy" /></a><br>
    <a href="https://github.com/SAIBYADAS/video-stream"> <img src="https://img.shields.io/github/repo-size/levina-lab/video-stream?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/SAIBYADAS/video-stream/commits/main"> <img src="https://img.shields.io/github/last-commit/SAIBYADAS/video-stream?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/SAIBYADAS/video-stream/issues"> <img src="https://img.shields.io/github/issues/SAIBYADAS/video-stream?color=red&logo=github&logoColor=blue&style=flat-square" /></a>
    <a href="https://github.com/SAIBYADAS/video-stream/network/members"> <img src="https://img.shields.io/github/forks/SAIBYADAS/video-stream?color=red&logo=github&logoColor=blue&style=flat-square" /></a>  
    <a href="https://github.com/SAIBYADAS/video-stream/network/members"> <img src="https://img.shields.io/github/stars/SAIBYADAS/video-stream?color=red&logo=github&logoColor=blue&style=flat-square" /></a>  
</p>

## 📊 Stats
[![CodeFactor](https://www.codefactor.io/repository/github/levina-lab/video-stream/badge)](https://www.codefactor.io/repository/github/levina-lab/video-stream)

## 🧪 Get `SESSION_NAME` from below:

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@levinalab/StringSession#main.py) ``Pyrogram``

## 🎭 Preview
<p align="center">
  <img src="https://telegra.ph/file/b8c1461bcbbad5664aa48.png">
</p>

## ✨ Features
- Supporto per streaming di musica e video
- Supporto multichat
- Supporto per playlist e coda
- Salta, Pausa, Riprendi, Interrompi funzione
- Funzione downloader di musica e video
- Supporto per la ricerca inline
- Supporto per la ricerca diretta su YouTube
- Supporto streaming YouTube/Locale/Live/m3u8
- Supporto per la ricerca in linea
- Controllo con il supporto del pulsante
- Controllo del volume
- Partecipazione automatica dell'Userbot
- Aggiornatore diretto

## 🛠 Commands:
| Command | Description |
| ------ | ------ |
| `/mplay (messaggio)` | riprodurre musica da youtube |
| `/vplay (messaggio)` | riprodurre video da youtube |
| `/vstream (link della live)` | riprodurre video in streaming dal vivo |
| `/pause` | mettere in pausa lo streaming (solo amministratore) |
| `/resume` | riprendere lo streaming (solo amministratore) |
| `/skip` | passa allo stream successivo (solo amministratore) |
| `/stop` | termina lo streaming (solo amministratore) |
| `/vmute` | per disattivare l'utentebot sulla chat vocale |
| `/vunmute` | per riattivare l'utentebot sulla chat vocale |
| `/volume 1/200` | regolare il volume dell'userbot (userbot deve essere amministratore) |
| `/playlist` | mostrarti tutto l'elenco di stream corrente |
| `/song (query)` | scarica musica da youtube |
| `/video (query)` | scarica video da youtube |
| `/userbotjoin` | invita lo userbot a unirsi al gruppo (solo amministratore) |
| `/userbotleave` | istruire userbot a lasciare il gruppo (solo admin) |
| `/leaveall` | ordina all'userbot di uscire da tutto i gruppi (solo sudo) |
| `/update` | aggiorna il tuo bot direttamente senza lasciare telegram (solo sudo) |
| `/restart` | riavvia il tuo bot direttamente senza lasciare telegram (solo sudo) |
| `/clean` | pulisci tutti i file non elaborati |
| `/rmd` | pulire tutti i file scaricati |
## Heroku Deployment 💜
The easy way to host this bot, deploy to Heroku, Change the app country to Europe (it will help to make the bot stable).

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/HollowUBot/video-stream)

## VPS Deployment 📡
Get the best Quality of streaming performance by hosting it on VPS, here's the step's:

```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/levina-lab/video-stream # clone the repo.
cd video-stream
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.

# continue the host with screen or anything else, thanks for reading.
```

# Credits 💖

- [Levina](https://github.com/levina-lab) ``Dev``
- [Zxce3](https://github.com/Zxce3) ``Dev``
- [DoellBarr](https://github.com/DoellBarr) ``Dev``
- [tofikdn](https://github.com/tofikdn) ``Dev``
- [Makoto-XD](https://github.com/Makoto-XD) ``Supporter``
- [Laky's](https://github.com/Laky-64) for [``py-tgcalls``](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [``Pyrogram``](https://github.com/pyrogram)

### Support & Updates 🎑
<a href="https://t.me/VeezSupportGroup"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/levinachannel"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
