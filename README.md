# AUTO RUN CCMINER IN TERMUX

Setting Step
```
apt-get update
```
```
apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git nano
```
```
git clone https://github.com/mantvmass/auto-run-ccminer
```
```
cd auto-run-ccminer
```
```
chmod +x edit-miner
```
```
chmod +x run-miner
```
```
sh setup.sh
```
```
run-miner
```
```
cd && cd ../etc
```
```
nano bash.bashrc
```
* เพิ่มบรรทัดแรกเป็น
- ```run-miner```
```
cd && cd ../etc/auto_miner/ccminer
```
```
chmod +x build.sh
```
```
chmod +x configure.sh
```
```
chmod +x autogen.sh
```
```
./build.sh
```
