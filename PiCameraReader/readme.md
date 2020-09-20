
- For ARM 32bit toolchain

        sudo apt-get install gcc-arm-linux-gnueabihf g++-arm-linux-gnueabihf

- For ARM 64bit toolchain

        sudo apt-get install gcc-aarch64-linux-gnu g++-aarch64-linux-gnu


- Dependencies

        sudo apt-get install build-essential autoconf libtool cmake pkg-config git 


aarch64.cmake


    SET(CMAKE_SYSTEM_NAME Linux)

    # specify the cross compiler
    SET(CMAKE_C_COMPILER   /usr/bin/aarch64-linux-gnu-gcc)
    SET(CMAKE_CXX_COMPILER /usr/bin/aarch64-linux-gnu-g++)

    # where is the target environment
    SET(CMAKE_FIND_ROOT_PATH /usr/aarch64-linux-gnu)

    # search for programs in the build host directories
    SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
    # for libraries and headers in the target directories
    set(CMAKE_SYSTEM_PROCESSOR arm)
    set(CMAKE_CXX_STANDARD 17)
    SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
    SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
    # end of the file
