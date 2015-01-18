
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local -D PYTHON2_EXECUTABLE=/usr/local/bin/python -D PYTHON3_EXECUTABLE=/usr/local/bin/python3 -D PYTHON_INCLUDE_DIR=/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/include/python3.4m/ -D PYTHON_INCLUDE_DIR=/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/include/python2.7/ -D PYTHON_LIBRARY=/usr/local/Cellar/python3/3.4.2_1/Frameworks/Python.framework/Versions/3.4/lib/libpython3.4.dylib -D PYTHON_LIBRARY=/usr/local/Cellar/python/2.7.9/Frameworks/Python.framework/Versions/2.7/lib/libpython2.7.dylib  -D BUILD_DOCS=ON -D BUILD_EXAMPLES=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D INSTALL_TESTS=ON -D WITH_OPENGL=ON -D WITH_OPENCL=ON ..

make -j8
sudo make install
