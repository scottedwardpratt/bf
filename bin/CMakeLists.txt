cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(msuboltzbf_project)
set(GITHOME_MSU $ENV{GITHOME_MSU})

add_custom_target(extern_msu_commonutils COMMAND make WORKING_DIRECTORY ${GITHOME_MSU}/commonutils/software)
add_custom_target(extern_msu_sampler COMMAND make WORKING_DIRECTORY ${GITHOME_MSU}/msu_sampler/software)
add_custom_target(extern_msu_boltzmann COMMAND make WORKING_DIRECTORY ${GITHOME_MSU}/msu_boltzmann/software)
add_custom_target(extern_msu_hydrobalance COMMAND make WORKING_DIRECTORY ${GITHOME_MSU}/hydrobalance/software)
add_custom_target(extern_msu_eos COMMAND make WORKING_DIRECTORY ${GITHOME_MSU}/msu_eos/software)


set(CMAKE_CXX_FLAGS "-W -Wall -march=native -std=c++17 -O2")
message(STATUS "CXX_FLAGS = " ${CMAKE_CXX_FLAGS})

set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake")
find_package(GSL REQUIRED)
find_package(Eigen3 REQUIRED)

include_directories(SYSTEM ${GSL_INCLUDE_DIR} ${EIGEN3_INCLUDE_DIR} ${GITHOME_MSU}/commonutils/software/include  ${GITHOME_MSU}/msu_sampler/software/include  ${GITHOME_MSU}/msu_boltzmann/software/include ${GITHOME_MSU}/hydrobalance/software/include ${GITHOME_MSU}/msu_eos/software/include)

link_directories(${GITHOME_MSU}/msu_sampler/software/lib ${GITHOME_MSU}/msu_boltzmann/software/lib ${GITHOME_MSU}/commonutils/software/lib ${GITHOME_MSU}/hydrobalance/software/lib ${GITHOME_MSU}/msu_eos/software/lib)

find_library(${GITHOME_MSU}/commonutils/software/lib msu_commonutils)
find_library(${GITHOME_MSU}/msu_sampler/software/lib msu_sampler)
find_library(${GITHOME_MSU}/msu_boltzmann/software/lib msu_boltzmann)
find_library(${GITHOME_MSU}/hydrobalance/software/lib msu_hydrobalance)
find_library(${GITHOME_MSU}/msu_eos/software/lib msu_eos)

set(SOURCE_FILES ./bf_fromhydro.cc)
add_executable(bf_fromhydro ${SOURCE_FILES})
add_dependencies(bf_fromhydro extern_msu_sampler extern_msu_commonutils extern_msu_boltzmann extern_msu_eos)
target_link_libraries(bf_fromhydro msu_boltzmann msu_commonutils msu_sampler msu_eos ${GSL_LIBRARY} ${GSL_CBLAS_LIBRARY} ${EIGEN3_LIBRARY} ${GITHOME_MSU}/commonutils/software/lib/libmsu_commonutils.a ${GITHOME_MSU}/msu_boltzmann/software/lib/libmsu_boltzmann.a ${GITHOME_MSU}/msu_sampler/software/lib/libmsu_sampler.a ${GITHOME_MSU}/msu_eos/software/lib/libmsu_eos.a)

set(SOURCE_FILES ./hydro2udsmain.cc)
add_executable(hydro2uds ${SOURCE_FILES})
add_dependencies(hydro2uds extern_msu_sampler extern_msu_commonutils extern_msu_boltzmann extern_msu_hydrobalance extern_msu_eos)
target_link_libraries(hydro2uds msu_boltzmann msu_commonutils msu_sampler msu_hydrobalance msu_eos ${GSL_LIBRARY} ${GSL_CBLAS_LIBRARY} ${EIGEN3_LIBRARY} ${GITHOME_MSU}/commonutils/software/lib/libmsu_commonutils.a ${GITHOME_MSU}/msu_boltzmann/software/lib/libmsu_boltzmann.a ${GITHOME_MSU}/msu_sampler/software/lib/libmsu_sampler.a ${GITHOME_MSU}/hydrobalance/software/lib/libmsu_hydrobalance.a ${GITHOME_MSU}/msu_eos/software/lib/libmsu_eos.a)
