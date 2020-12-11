# Pomodoro Timer
## Author
[Preston-Too](https://github.com/Preston-Too)

## Live Link
* [here] 

## Description
Pomodoro App is an awesome platform used in offices by workaholics. Once you login,you will be able to set time to work and time to be on break and you can also see the work session you've completed.

## User Stories
What the user does...
* A user logs into the application.
* A user set the amount of time he/she wants to work. It should not be more than an hour
* A user set the amount of time he/she wants to go for break. It should not be less than 5 min & not more than 10 min
* A user specify what he/she wants to do with their break time before they start working.
* A user see how much time they are have left for working or taking a break. (A countdown clock).
* A user see how many work sessions he/she has completed.

## Installation / Setup instruction

#### The application requires the following installations to operate 
* python3.6
* pip

#### Cloning

* Open Terminal {Ctrl+Alt+T}

* git clone ```https://github.com/Preston-Too/Pomodoro-Timer.git```

* Move to the folder and install requirements
    ```pip install -r requirements.txt```

* Running the application
    ```python3.6 manage.py runserver / .start.sh```
* Testing the application
    ```python3.6 manage.py test```


## Behaviour Driven Development
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
|On loading View time on default | click on login to register and sign in|Taken to you profile|
|Start button| Click on start button| time starts running|
|Stop button | Click on stop button |  time stops running|
|Pause button | Click on pause button |time pauses running|
|Click on Sign Out | Redirects to the comment page|Signs user out|

## Technologies Used

* python3.8
* Flask
* Bootstrap
* HTML / CSS

## Known Bugs
* There are no known bugs at the moment

## Contact Information 

If you have any question or contributions, please email me at [toopreston@gmail.com]

## License
* [[License: MIT]](LICENCE.md)
* Copyright (c) 2020 **Preston Too**