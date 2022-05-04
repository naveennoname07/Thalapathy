echo "Cloning main Repository"
git clone -b master https://github.com/200920082007/TigerShroff.git /Wan-peng
cd /Wan-peng
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Wan peng....🔥"
python3 bot.py
