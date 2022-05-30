echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/naveennoname07/Thalapathy.git /Thalapathy
cd /Vijay-Filter-BoT
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
