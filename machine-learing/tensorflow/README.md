# Tensorflow experiments

### Install tensorflow with a python virtual enviroment
Install the virtualenv python package.
```
sudo pip install virtualenv
```

Setting up a python2.7 virtual enviroment.
```
virtualenv --system-site-packages -p python2.7 .
```

Activate the virtual env.
```
source ./bin/activate
```

Upgrade all virtual enviroment python packages.
```
pip install --upgrade pip
```

List all venv python packages.
```
pip list
```

And to exit virtualenv later
```
deactivate
```



### Install Tensorflow
That installs tensorflow for macos without CUDA GPU support. For more GPU information [go here](https://www.tensorflow.org/install/gpu).
```
pip install --upgrade tensorflow
```

First line of tensorflow code 🤘🏻
```
python -c "import tensorflow as tf; print(tf.__version__)"
```
**More to read here at tensorflow** → [https://www.tensorflow.org](https://www.tensorflow.org/install/pip?lang=python2)



### Install Tensorflow
That installs tensorflow for macos without CUDA GPU support. For more GPU information [go here](https://www.tensorflow.org/install/gpu).
```
pip install --upgrade tensorflow
```

First line of tensorflow code 🤘🏻
```
python -c "import tensorflow as tf; print(tf.__version__)"
```
**More to read here at tensorflow** → [https://www.tensorflow.org](https://www.tensorflow.org/install/pip?lang=python2)
