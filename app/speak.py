import json, time, random, math, urllib, urllib2, subprocess, sys 

# returns the appropriate google speech url for a particular phrase
def getGoogleSpeechURL(phrase):
    googleTranslateURL = "http://translate.google.com/translate_tts?tl=en-us&"
    parameters = {'q': phrase}
    data = urllib.urlencode(parameters)
    googleTranslateURL = "%s%s" % (googleTranslateURL,data)
    return googleTranslateURL


# output phrase to audio using mplayer
def speakSpeechFromText(phrase):
    googleSpeechURL = getGoogleSpeechURL(phrase)
    subprocess.call(["mplayer",googleSpeechURL], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)



