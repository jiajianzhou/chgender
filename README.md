# chgender
Introduction:

Gender guess for Chinese names in English(Pinyin) form

- language: Python
- method: Naive Bayes with different weight
- dataset: 20 million Chinese name
- accuracy: 81% for 1500 random selected samples

Possible usage field:

- User registration on websites or New contact creation. Based on the names, we can pre select the gender option. 
- Gender analysis for Chinese people who publish papers on English journals.

How to use:

install:
1. use pip
	$ pip install chgender
2. clone from the git
	$ git clone git@github.com:jiajianzhou/chgender.git
	$ sudo python setup.py install

usage:
1.use as module
>>>import chgender
>>>chgender.guess('dehua liu')
('male', 0.966248721556)

2.use on bash
$chg -n dehua xueyou fucheng ming
name: dehua => gender: male, probability: 0.966248721556
name: xueyou => gender: male, probability: 0.985020743536
name: fucheng => gender: male, probability: 0.999357367222
name: ming => gender: male, probability: 0.851123622896

3.use for batch 
3.批量处理
$chg -f samples.txt
name: dehua => gender: male, probability: 0.966248721556
name: xueyou => gender: male, probability: 0.985020743536
name: fucheng => gender: male, probability: 0.999357367222
name: ming => gender: male, probability: 0.851123622896
......


简介：

依据拼音形式的中文名字来猜测性别

- python
- 使用朴素贝叶斯法，并对不同的位置的字分配权重
- 基于2000万姓名数据量
- 对1500个随机样本进行测试，准确率81%


可使用领域：

-账户注册、通讯录添加等。可依据用户输入的拼音，提前判断并选择好男女选项，提高用户体验。
-英文文献数据分析。对于外文期刊中的拼音形式的中文名字，分析相关方面的男女差异。


用法：

安装方式：
1.pip直接安装
	$ pip install chgender

2.git下载本地
	$ git clone git@github.com:jiajianzhou/chgender.git
	$ sudo python setup.py install

使用形式：
1.作为模块使用
>>>import chgender
>>>chgender.guess('dehua liu')
('male', 0.966248721556)

2.在bash上使用
$chg -n dehua xueyou fucheng ming
name: dehua => gender: male, probability: 0.966248721556
name: xueyou => gender: male, probability: 0.985020743536
name: fucheng => gender: male, probability: 0.999357367222
name: ming => gender: male, probability: 0.851123622896

3.批量处理
$chg -f samples.txt
name: dehua => gender: male, probability: 0.966248721556
name: xueyou => gender: male, probability: 0.985020743536
name: fucheng => gender: male, probability: 0.999357367222
name: ming => gender: male, probability: 0.851123622896
......


