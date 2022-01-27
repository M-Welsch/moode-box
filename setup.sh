echo "Extending PYTHONPATH:"
echo "export PYTHONPATH=${PYTHONPATH}:${HOME}/Desktop/hmi" >> ~/.bashrc
pip install -r requirements.txt

echo "enabling i2c and spi interface"
sudo raspi-config nonint do_spi 0  # yes, 0 means "activating"!

echo "creating service File"
sudo cp setup_files/yt_client.service /etc/systemd/system/

sudo cp setup_files/autostart /etc/xdg/lxsession/LXDE-pi/

sudo systemctl daemon-reload
sudo systemctl enable yt_client

