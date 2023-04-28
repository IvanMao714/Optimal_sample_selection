# Optimal Sample Selection (Project for Artificial Intelligence)

<p align="center">
  <!-- License -->
  <a href="./LICENSE">
    <img src="https://img.shields.io/badge/license-Apache%202.0-yellow.svg?logo=apache"/>
  </a>
  <!-- GitHub last commit -->
  <a href="./"><img src="https://img.shields.io/github/last-commit/IvanMao714/Optimal-sample-selection?logoColor=blue&style=plastic"/>
  </a>
</p>

<img src=".\static\logo.png" style="zoom:76%;" />




## Introduction

 It is known that the amount of data generated has been increasing tremendously in the last few years due to the ease of accessing to the Internet, cheap or inexpensive mass storage devices, the ease of transferring data through Internet, communication lines and digital data are used in all walks of life. Nowadays, these big data have been used for data mining, knowledge discovery, machine learning, statistical learning, statistical analysis and experiments. In order to extract or discover useful data, information or knowledge from these big data, one of methods we usually adopted is samples selection.

This project we mainly focus on how to use less long string(k length) to convert short string(s length). And you can see detailed rules by this [link](https://raw.githubusercontent.com/IvanMao714/Optimal-sample-selection/kivy/introduce/Group%20Project(23).pdf).

We upload all of our source code on the $\href{https://github.com/IvanMao714/Optimal-sample-selection/}{github}$, and you download it if you interested.

## Download

You can download our different edition software by website as follows:

- [Windows](https://raw.githubusercontent.com/IvanMao714/Optimal-sample-selection/kivy/installer/Windows/installer.exe)

- [MacOS](https://raw.githubusercontent.com/IvanMao714/Optimal-sample-selection/kivy/installer/MacOS/OSS.zip)

## Installation

After you download the installer, you would get an file named *installer.exe* .Then you should double click this file, and you will get picture like this

<img src=".\img\1.png" style="zoom:75%;" />

Finally, you can choose the destination path you want to install and click the button. The Optimal Sample Selection Software had been installed in your computer.

For MacOS users, you can download software directory directly by above link.

## Usage

### Index Page

 First, find your installation path and *main folder*, and double click the *'main.exe'*. You will get picture like this.

<img src=".\img\2.png" style="zoom: 75%;" />

*Select Button*: you can into algorithms parameters setting page and run our algorithms by click this button.
*Database Button*: you can into database page and **display** or **delete** data you had record in our database. Moreover, you can download theses data in your computer.

### Algorithms Parameters Setting Page

After you click *select Button*, you will see page like this

<img src=".\img\3.png" style="zoom:75%;" />

If you want to use specified number to test our algorithms, you input number in the textbox. However, there some rules about the parameters' setting.

- 45<= m <= 54
- 7<= n <=25
- 4<= k <=7
- s <= j <= k
- 3 <= s <= 7


And then click *Specified Select Button*. We promise you can get you want. Of course, if you don't want to input number, we also provide *Random Select Button* which can run our algorithms by random number.  

### Import data to database

After you run algorithms, you will see page like this.

<img src=".\img\4.png" style="zoom:75%;" />

You can record your data by *Import to Database Button*, or just cancel the result. 

### Database Page

After you click *Database Button*, you will see page like this.

<img src=".\img\5.png" style="zoom:75%;" />

*Display Database Data*: You can display the database data which your record by set specified m, n, k, j, s, times.
*Delete Database Data*: You delete all of data in the database.
*Download Database File*:  You can download the data in your computer as **DB.txt** and you can choose the path of file if you want.

## Dependency

- kivy
- random
- pymongo
- sys

## Contributor

- Mao Yifan
- Li Zhankeng
- Wang Zhonghan