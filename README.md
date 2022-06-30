# Python Troll Library :trollface:

Trollpy is a library purely for trolling others by overriding some built-in or common functions/classes seen within Python programs.

## 🚀 Installation

### Using pip

```shell
pip install trollpy
```

Or, if you have multiple versions of python installed:

```shell
pip3 install trollpy
```

### Using git

```shell
git clone https://github.com/zahtec/trollpy.git
```

## 🛠 Usage

Make sure to import this at the bottom of any import list in order to confirm that it ovverides any other imported functions.

**For Example:**

```py
import numpy as np
from cv2 import imshow
from PIL.Image import open
from builtin import open # Overrides Pillow's import
```

Also, this library is imported using the word `builtin`, very similar to pythons native module `builtins`, as to not arouse suspicion from whoever your trolling. It would be much to easy if it was called Trollpy

## ⚠️ Disclaimer

Please use this just as a little bit of trolling, not for malicious intent, thanks!

## 📔 Documentation

Read the [wiki](https://github.com/zahtec/trollpy/wiki)

## 📡 Contribution Guide

Contributing to Trollpy is very welcome, but there are a few guidlines that come with it:

-   Contribute with the main provided template on github
-   Contribute functions and/or classes one at a time (Do not contribute 2 or more functions/classes at once)
-   Keep it in the same file ([troll.py](https://github.com/zahtec/trollpy/blob/main/builtin/troll.py)). I do not plan on modularizing this library
-   As long as you follow and fill everything out in the template, you should be fine

This way contributing can be much faster and more standardized, you can go slightly off the template, but try to keep most of the fields there with your answers. Thank you for contributing!
