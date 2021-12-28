echo "Extending PYTHONPATH:"
echo "export PYTHONPATH=${PYTHONPATH}:${HOME}/Desktop/hmi" >> ~/.bashrc

echo "creating service File"
sudo cp setup_files/yt_client.service /etc/systemd/system/

sudo cp setup_files/austart /etc/xdg/lxsession/LXDE-pi/

sudo systemctl daemon-reload
sudo systemctl enable yt_client