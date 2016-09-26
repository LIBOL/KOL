cmake_minimum_required(VERSION 2.6)

project(KOL)

set (EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
#IF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
set (CMAKE_INSTALL_PREFIX ${CMAKE_SOURCE_DIR})
#ENDIF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)

#check if Eigen exists
find_path(EIGEN_PATH NAMES Eigen PATHS ${EIGEN_DIR} REQUIRED)
if (NOT EIGEN_DIR)
    message(FATAL_ERROR "Eigen is not found, please specify by: -DEIGEN_DIR=<eigen_path>")
endif (NOT EIGEN_DIR)


FILE(GLOB data_files src/data/*.h)
FILE(GLOB loss_files src/loss/*.h)
FILE(GLOB opti_files src/kernel/*.h)
FILE(GLOB comm_files src/common/*.h)

set (data_files ${data_files} 
    src/data/basic_io.cpp 
    )

include_directories(
    ${EIGEN_PATH}
    )

#set (data_files ${datafiles} 
#    src/data/basic_io.cpp 
#    src/data/zlib_io.cpp 
#    src/data/gzip_io.cpp
#    )
source_group("data" FILES ${data_files})
source_group("loss" FILES ${loss_files})
source_group("kernel" FILES ${opti_files})
source_group("common" FILES ${comm_files})

set (SRC_LIST
    ${data_files} ${loss_files} ${opti_files} ${comm_files}
    )

IF(CMAKE_COMPILER_IS_GNUCXX)
    SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-write-strings -O2 -s")
ENDIF(CMAKE_COMPILER_IS_GNUCXX)
    
add_executable(KOL src/Params.cpp src/Params.h 
    src/main.cpp ${SRC_LIST}) 
IF(UNIX)
    target_link_libraries(KOL pthread)
ENDIF(UNIX)

add_executable(Cacher src/data/Cacher.cpp ${data_files})
IF(UNIX)
    target_link_libraries(Cacher pthread)
ENDIF(UNIX)

install(TARGETS KOL Cacher
    DESTINATION .)
