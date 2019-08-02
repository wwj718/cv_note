# install
opencv安装相关

### mac
```
pip3 install opencv-contrib-python
pip3 install opencv-python imutils
```


### raspberrypi
参考[运行在树莓派中的 scratch3-adapter opencv 插件](https://blog.just4fun.site/adapter-opencv.html)

```
sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
sudo apt-get install libxvidcore-dev libx264-dev
sudo apt install libatlas-base-dev
sudo apt-get install qt4-dev-tools
# 如果失败 则:  sudo apt-get install qt4-dev-tools --fix-missing
pip3 install opencv-contrib-python opencv-python imutils --user
```