echo "Cloning Repo, Please Wait..."
git clone -b master https://github.com/Naveen-TG/Vijay-Filter-BoT.git /Vijay-Filter-BoT
cd /Vijay-Filter-BoT
echo "Installing Requirements..."
pip3 install -U -r requirements.txt
echo "Starting Bot, Please Wait..."
python3 bot.py
