# SpamBot
A small automative script that takes text and repeats it a given amount of times via keyboard input. Additionally, it takes "victim" and "tts" arguments which mention a given user on Discord and run the text through text-to-speech, respectively.

### Installation
  Requires [Python3](https://www.python.org/downloads/) and [Pip](https://pypi.org/project/pip/)
   
  Install [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) using the following in any command line ran as *administrator*:
  > **python3 -m pip install -U pyautogui**
 
  or
  > **py -m pip install pyautogui**

## Methods
**Copy-paste Method**  
This method will manually type out the string, then copy it, and paste it a given number of times. Although this method is less computationally intensive, it is not optimal for requests for over 10 iterations, as Discord will rate limit at that point.   

![](https://media4.giphy.com/media/oeLa0Ac7Rl7ye24Dkp/giphy.gif?cid=790b7611d179f72808843ef329126eeb54fa1e5facd53e97&rid=giphy.gif&ct=g)

**Repeated input Method**  
This method will manually type out the string a given number of times. This method will become more computationally intensive and is much slower for longer strings, but does not run into Discord rate limits as it bypasses the 10,000 HTTP requests per 10 minute benchmark.   

![](https://media1.giphy.com/media/wLKt8KnNMavXGUYVbM/giphy.gif?cid=790b7611f2d07cd415437afd0b2feb3ada648a302198c888&rid=giphy.gif&ct=g)

## Links
[PyAutoGui Documentation](https://pyautogui.readthedocs.io/en/latest/)
