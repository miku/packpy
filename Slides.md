# Packaging Python Applications

PyConBalkan, Belgrade, 2018-11-17 16:00-16:30

[Martin Czygan](mailto:martin.czygan@gmail.com) / github.com/miku / [@cvvfj](twitter.com/cvvfj)

----

# About me

* Software developer at [Leipzig University Library](https://www.ub.uni-leipzig.de/start/)
* Part-time consultant, co-author *Getting Started with Python Data Analysis* (2015)
* Maintainer of a few open source tools

![](images/montage.png)

----

# About me

* interest in (build) automation: code, writing, data
* anecdata: ant, ephemeral VMs, tried to ease adoption of Python at workplace

<!-- changed build system for book, worked for springer publishing, ... -->

There is some satisfaction in being able to just run *one command*. There are also some trade-offs.

----

# Packaging

* loosely defined as *approaches* and *tools* to create usable (installable, shippable) software
* there is this thing called: *The packaging gradient* 

----

# Packaging is moderately exiting

* not directly related to features
* many options

> ... plethora of packaging options ... (https://packaging.python.org/overview/)

* less formalized, project-dependent

----

# So why care about packaging?

* as individual or team
* as company

----

# Individuals or teams

* to share code
* collaborate or invite contributions

> It might seem strange to think about packaging before writing code, but this process does wonders for avoiding future headaches. (https://packaging.python.org/overview/)

----

# As a company

* Aug 9, 2000: [The Joel Test: 12 Steps to Better Code](https://www.joelonsoftware.com/2000/08/09/the-joel-test-12-steps-to-better-code/)

There are two items related to packaging:

* #2 Can you **make a build** in **one step**?
* #3 Do you make **daily builds**?

----

# On item #2

> By this I mean: <u>**how many steps**</u> does it take to make a **shipping build** from the latest source snapshot? On good teams, there's a <u>**single script**</u> you can run that does a full checkout from scratch, rebuilds every line of code, **makes the EXEs**, in all their various versions, languages, and #ifdef combinations, creates the **installation package**, and creates the final media — CDROM layout, download website, whatever.

----


# On item #2

> If the process takes any more than one step, it is <u>**prone to errors**</u>. And when you get closer to shipping, you want to have a <u>**very fast cycle**</u> of fixing the "last" bug, making the final EXEs, etc. If it takes 20 steps to compile the code, run the installation builder, etc., you’re <u>**going to go crazy**</u> and you’re going to make silly mistakes.

----

# Packaging is only a part of a larger story

* the decade of devops (2009-)
* code--build--test--**package**--**release**--configure--monitor

There slides reflect only a few small pieces of the puzzle.

----

# The Packaging Gradient

There is an nice talk called *The Packaging Gradient* by Mahmoud Hashemi at [PyBay 2017](https://www.youtube.com/watch?v=iLVNWfPWAC8) (YT:601), [BayPiggies2017](https://www.youtube.com/watch?v=Q3LyPTTb81w) (YT:82) - [blog](https://sedimental.org/the_packaging_gradient.html).

> One lesson threaded throughout Enterprise Software with Python is that deployment is **not the last step of development**. 

