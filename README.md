curl -L "https://avatars.githubusercontent.com/u/71009747?v=4&s=400" -o avatar.png
python3 tools/ascii_portrait.py --image avatar.png --preview   # eyeball it
python3 tools/ascii_portrait.py --image avatar.png > tools/portrait.json
python3 tools/build_card.py
