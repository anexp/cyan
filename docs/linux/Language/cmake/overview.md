# Overview

### Sample compile commands


with gcc
```sh
/usr/bin/cmake -S /home/user/Code/qt/tst1 -B /home/user/Code/qt/build-tst1-bbb1-Debug -DCMAKE_GENERATOR:STRING=Ninja -DCMAKE_BUILD_TYPE:STRING=Debug -DQT_QMAKE_EXECUTABLE:FILEPATH=/bin/qmake6 -DCMAKE_PREFIX_PATH:PATH=/usr -DCMAKE_C_COMPILER:FILEPATH=/bin/gcc -DCMAKE_CXX_COMPILER:FILEPATH=/bin/g++ -DCMAKE_CXX_FLAGS_INIT:STRING=-DQT_QML_DEBUG
```

with clang
```sh
/home/user/Qt/Tools/CMake/bin/cmake -S /home/user/Qt/Examples/Qt-6.5.3/serialport/terminal -B /home/user/Qt/Examples/Qt-6.5.3/serialport/build-terminal-Desktop_Qt_6_5_3_GCC_64bit-Debug -DCMAKE_GENERATOR:STRING=Ninja -DCMAKE_BUILD_TYPE:STRING=Debug -DCMAKE_PROJECT_INCLUDE_BEFORE:FILEPATH=/home/user/Qt/Examples/Qt-6.5.3/serialport/build-terminal-Desktop_Qt_6_5_3_GCC_64bit-Debug/.qtc/package-manager/auto-setup.cmake -DQT_QMAKE_EXECUTABLE:FILEPATH=/home/user/Qt/6.5.3/gcc_64/bin/qmake -DCMAKE_PREFIX_PATH:PATH=/home/user/Qt/6.5.3/gcc_64 -DCMAKE_C_COMPILER:FILEPATH=/bin/clang-14 -DCMAKE_CXX_COMPILER:FILEPATH=/bin/clang++-14 -DCMAKE_CXX_FLAGS_INIT:STRING=-DQT_QML_DEBUG
```
