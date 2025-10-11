# Installation of OpenSTA

## 1. Install CMake
```bash
sudo apt update
sudo apt install -y cmake
```
## 2. Install CUDD
```bash
git clone https://github.com/ivmai/cudd.git
cd cudd
autoreconf -i
./configure --prefix=/usr/local
make -j$(nproc)
sudo make install
```
## 3. Build OpenSTA
```bash
git clone https://github.com/The-OpenROAD-Project/OpenSTA.git
cd OpenSTA
mkdir build
cd build
cmake -DCUDD_DIR=/usr/local ..
make -j$(nproc)
```
For more detailed instructions, please refer to the [OpenSTA GitHub Repository](https://github.com/The-OpenROAD-Project/OpenSTA)
