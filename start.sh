echo "Cloning main Repository"
git clone -b main https://github.com/200920082007/TigerShroff.git /Wan-peng
cd /TigerShroff
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Test....🔥"
python3 bot.py
