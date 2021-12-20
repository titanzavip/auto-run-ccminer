apt-get install libcurl4-openssl-dev
apt-get install libssl-dev
apt-get install libjansson-dev
apt-get install automake
apt-get install autotools-dev
apt-get install build-essential
apt-get install nano -y


git clone https://github.com/mantvmass/auto-run-ccminer
cd auto-run-ccminer
chmod +x edit-miner
chmod +x run-miner


apt-get install python3 -y
pip3 install progress


mv src_run_ccminer ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin


run-miner


cd && cd ../etc/src_run_ccminer/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

run-miner