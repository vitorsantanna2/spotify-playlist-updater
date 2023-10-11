# Spotify Playlist Updater


#### A Python script to update Spotify Playlist data (descrption, photo) using timed intervals.  

## Description

An automatic playlist updater using Spotify API and Authorization code flow in Python to update a Playlist on a repeating time interval. 

## Getting Started

#### Spotify Playlist Updater requires three dependencies: 

##### Pip

* A Package Management System for Python.
* [Installation Link](https://pip.pypa.io/en/stable/installation/)

##### Schedule
* Python job scheduler to run the script on a timer.
* [Installation Link](https://schedule.readthedocs.io/en/stable/installation.html)

##### Spotipy
* Python library for the Spotify Web API
* [Installation Link](https://spotipy.readthedocs.io/en/2.19.0/#installation)
* For Windows, you can run ``` py -m pip install spotipy --upgrade ``` in CMD to install. 

#

### Set Up

##### Installing the Script

* Install the dependencies listed above. 
* Choose a location on your device (I'll refer to this as the working directory)
* Download the latest release of [spotify-playlist-updater](https://github.com/aeriie/spotify-playlist-updater/) to the working directory. 
* Save your playlist photo (if applicable) in the ``data`` folder of the working directory
    * The photo must be 150KB or less. If it is too large, resize the photo. 
    * You can use this website to resize your image: https://www.resizepixel.com/reduce-image-in-kb/

##### Set up Client ID, Client Secret and Redirect URI
* Login to Spotify Developer Account
    * Go to https://developer.spotify.com/dashboard/ and click Manage Dashboard. 
    * Then, sign in with your Spotify credentials and accept the latest Developer terms of service.
    * Note your Client ID, and Client Secret. 
* Create an App
    * In the Developer Dashboard, create an App. You can put whatever you'd like for the App name and description. 
    * Click Edit Settings. 
        * Add your domain address to the Redirected URI's field, and click Add. Make sure to Save. 

##### Adding your Playlist information
* Right click \spotify-playlist-updater.py from the working directory, and select "Edit with IDLE"
   * Put your Playlist Image path in place of: ```` "./photo/photo.jpg" ````
   * Put your Spotify Username in place of: ```` 'username' ````
   * Put your Client ID in place of ```` 'clientid' ````
   * Put your Client Secret in place of ```` 'clientsecret' ````
   * Put your Web Domain Address in place of ```` 'redirect_uri' ````
   * Put your Spotify Playlist Link in place of ```` 'playlist_id' ````
   * Put your Playlist Description in place of ```` 'Playlist Name' ````
   * Put your Playlist Description in place of ```` 'Playlist Description' ````
* **Save the script once your changes are made.** 



### Running the Script
 Use `nohup python3 ./script_name.py &` to run in background

## Thank you

If you enjoyed my project, please feel free to leave tips on my [Ko-Fi. https://ko-fi.com/autumntillman](https://ko-fi.com/autumntillman)
or [Paypal](https://www.paypal.com/paypalme/autterpop?locale.x=en_US).

## FAQ
* How do I schedule this to run at a set time every day instead of all the time?
   * replace schedule.every(1).minutes.do(func2) with schedule.every().day.at('13:56').do(sched_job)
   * note that time is based on military time (24 hour clock)
   * you can replace 'day' with a specific day of the week as well

## Help

* If you get an error that "Read timed out. (read timeout=5)", restart the script. 
* If your script doesnt get past "Starting Playlist Updater", run the script using IDLE:
   * Right click spotify-playlist-updater and click Edit with IDLE
   * Click F5 to run the script
      * Let the script run. Any errors will be listed as the script encounters them.
    
If you're having issues getting this setup, feel free to reach out to me via Discord: .aeriie

To report code issues, create a new issue on Github or reach out to me directly at [autumntillman0@gmail.com](mailto:autumntillman0@gmail.com)

## Authors

[Aeriie](https://github.com/aeriie) on GitHub
[Vitor Santanna](https://github.com/vitorsantanna2) on GitHub

## Version History

* 0.1
    * Initial Release
 
* 0.2
   * Added improved reliability for schedule function
   * Cleaned up code
* 0.3
  * Add support to env enviroments
  * Simplify code with @repeat method
  * Nohup instructions to run in background
