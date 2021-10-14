# OPEN TERMUN AUTO FILE TWO
[ FILE ONE ](https://github.com/mantvmass/auto-file-one)  
<br>
Step run  
```
apt-get update
```
```
apt-get install libcurl4-openssl-dev libssl-dev libjansson-dev automake autotools-dev build-essential git nano
```
```
git clone https://github.com/mantvmass/auto-file-two
```
```
cd auto-file-two
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
