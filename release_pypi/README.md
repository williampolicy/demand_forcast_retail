python setup.py sdist bdist_wheel
twine upload dist/*
pip install kangforecast

-关于测试

在Python项目中，通常将测试代码放在一个名为"tests"的目录下，这个目录与你的"src"（源代码）目录是平行的。在你的情况下，源代码目录是"kangforecast"，因此你可以创建一个与"kangforecast"平行的新目录，命名为"tests"。如下所示：

```bash
kang@Love-Grace release_pypi$ tree
.
├── README.md
├── build
│   └── bdist.macosx-12-arm64
├── data
│   └── special_dates.csv
├── dist
│   ├── kangforecast-0.1-py3-none-any.whl
│   └── kangforecast-0.1.tar.gz
├── kangforecast
├── tests
├── kangforecast.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
└── setup.py
```

你可以在"tests"目录中添加你的测试代码。例如，你可以创建一个名为"test_kangforecast.py"的文件。这样，你的测试代码不会被包含在你的发布包（即通过`pip install`安装的包）中，但是它仍然在你的项目结构中，可以方便你进行开发和测试。

然后，你可以使用测试框架（如`pytest`）来运行你的测试。只需在项目根目录下运行命令`pytest`，它会自动查找并运行所有的测试。

当然，你也可以在你的`setup.py`中指定`tests`目录，这样当其他人安装你的包并希望运行测试时，他们可以直接使用`python setup.py test`命令。如果你决定这样做，你可能需要对你的`setup.py`做一些修改，添加一些关于测试的配置。


--- 关于执行顺序。
当你在终端中键入python，操作系统会遍历你的PATH环境变量中的每一个目录，寻找名为python的可执行文件。

PATH是一个包含了多个文件路径的环境变量，各路径之间由冒号:分隔。当你键入命令时，系统会按照PATH中的顺序，从前往后查找每个路径，看看哪个路径中包含了你要执行的命令。

比如你的PATH可能类似这样：/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Users/kang/miniconda3/bin。

当你键入python后，系统首先会查看/usr/local/bin目录下是否有python这个可执行文件，如果有，就会运行它。如果没有，就会接着查看/usr/bin，以此类推。只有在前面的路径都没有找到python可执行文件的情况下，才会去查看/Users/kang/miniconda3/bin。

所以，你使用的Python解释器版本是由PATH中的顺序决定的。如果你希望使用Homebrew的Python解释器，你需要确保Homebrew的路径（通常是/usr/local/bin）在PATH中的位置比Miniconda的路径（/Users/kang/miniconda3/bin）靠前。你可以通过修改PATH来改变这个顺序。
------ for Homebrew:
export PATH="/usr/local/bin:$PATH"

source ~/.bashrc

------for conda
conda create -n new_env python=3.11
conda activate new_env
pip install kangforecast