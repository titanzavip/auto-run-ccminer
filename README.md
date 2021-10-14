# OPEN TERMUN AUTO FILE TWO
[ FILE ONE ](https://github.com/mantvmass/auto-file-one)  
<br>
Step run  
```
apt-get update
```
```
apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git
```
```
git clone https://github.com/mantvmass/auto-file-two
```
```
cd auto-file-two
```
```
rm ../../etc/bash.bashrc
```
```
mv bash.bashrc ../../etc/
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
