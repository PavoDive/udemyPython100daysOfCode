# To build the standalone app

I followed the instructions [here:](https://medium.com/analytics-vidhya/how-to-create-executable-of-your-python-application-from-linux-windows-mac-bcbcdd4603d4).
I had to downgrade setuptools package by:

```
pip3 install setuptools==65.7.0
```

Following directions [here:](https://answers.ros.org/question/411949/cannot-build-package-due-to-pkg_resourcesexternpackagingversioninvalidversion/).


# To build the android standalone

```
pip3 install buildozer

# cd path/to/folder

buildozer init

nano buildozer.spec

buildozer android debug deplot run
```

It initially failed beacuse git timed out (because of the bad internet connection).
