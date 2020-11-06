# ㄒㄩ尺Ҝ乇ㄚ ㄒ乇卂爪
from linepy import *##ㄒㄩ尺Ҝ乇ㄚ ㄒ乇卂爪
from akad.ttypes import Message ## ＴＵＲＫＥＹ ＴＥＡＭ
from liff.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from ZarifKing.thrift.protocol import TCompactProtocol
from ZarifKing.thrift.transport import THttpClient
from ZarifKing.ttypes import LoginRequest
from Naked.toolshed.shell import execute_js
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
from gtts import gTTS
from threading import Thread
from io import StringIO
from multiprocessing import Pool
from googletrans import Translator
from urllib.parse import urlencode
from wikiapi import WikiApi
from tmp.MySplit import *
from random import randint
from shutil import copyfile
from youtube_dl import YoutubeDL
from threading import Thread, activeCount
import LineService
import subprocess, youtube_dl, humanize, traceback
import subprocess as cmd
import requests, json, random
import time, random, sys, json, null, codecs, html5lib ,shutil ,threading, glob, re, base64, string, os, requests, six, ast, pytz, wikipedia, urllib, urllib.parse, atexit, asyncio, traceback
_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
#=====================================================================
zarifoglu = LINE("Token veya gmail koy" , appName="Buraya güncel appname koy") #turkeyteam
Channel(zarifoglu, "1597127494").getChannelResult().channelAccessToken
#=======================================================
waitOpen = codecs.open("zarifoglu/wait.json","r","utf-8")
settingsOpen = codecs.open("zarifoglu/temp.json","r","utf-8")
premiumOpen = codecs.open("zarifoglu/user.json","r","utf-8")
javaOpen = codecs.open("zarifoglu/java.json","r","utf-8")
#=====================================================================
#=====================================================================
zarifogluProfile = zarifoglu.getProfile()
zarifogluSettings = zarifoglu.getSettings()
zarifogluPoll = OEPoll(zarifoglu)
zarifogluMID = zarifoglu.getProfile().mid
#=====================================================================
loop = asyncio.get_event_loop()
myAdmin = ["u5d854616fc8ea66893e7a85b7cb0b9f1"]
muhasebe = ["u5d854616fc8ea66893e7a85b7cb0b9f1"]
botStart = time.time()
msg_dict = {}
temp_flood = {}
wait = json.load(waitOpen)
settings = json.load(settingsOpen)
premium = json.load(premiumOpen)
java = json.load(javaOpen)

hoho = {
    "savefile": False,
    "namefile": "",
}

chatbot = {
    "admin": [],
    "botMute": [],
    "botOff": [],
}

read = { 
    "readMember": {},
    "readPoint": {}
}

wmin = {
    "wMessage": False,
    "textnya": "Enjoying in this group",
}

lvin = {
    "lMessage": False,
    "textnya": "See u next time",
}

tailah = {
    "siderTemp": {},
    "siderPesan": "You can join chat?",
}

setbot = {
    "background": "#000000",
    "text": "#ffffff",
    "separator": "#ffffff",
    "helptext": "#00FFFF",
    "helpseparator": "#00FFFF"
}

gwcool = {
    "squad": "Turkey Team™",
}

javascript = {
    "jskick": "bypass",
    "jskick1": "cleanse",
    "cancels": "cancel",
}
#=====================================================================
def QRV2(to):
    apiKey = "Buraya apikey koy"
    headers = {
        "apiKey":apiKey, 
        "appName": "Güncel appname kullan aslan parçası ;)",
        "cert" : None, 
        "server": random.choice(["pool-1","pool-2"]), 
        "sysname": "Türkiye Line Federasyonu" 
        }
    main = json.loads(requests.get("https://api.be-team.me/qrv2",headers=headers).text)
    zarifoglu.sendMessage(to,"2 dakika içinde linke giriş yapın:-\n " + main["result"]["qr_link"])
    #print("Login IP: " + main["result"]["login_ip"])
    if not headers["cert"]:
        zarifoglu.sendMessage(to,main["result"]["cb_pincode"])
        zarifoglu.sendMessage(to, "Önce şu linki kopyala 👆👆👆 Tokene giriş yaptıktan sonra internet tarayıcına yapıştırıp pinkodunu görebilirsin..")
        result = json.loads(requests.get(main["result"]["cb_pincode"],headers=headers).text)
        zarifoglu.sendMessage(to,"Pin Kodu: " + result["result"])
    result = json.loads(requests.get(main["result"]["cb_token"],headers=headers).text)
    if result["status"] != 200:
        print("[ Error ] "+ result["reason"])
    else:
      #print("Your Cert: " + result["result"]["cert"])
        return result["result"]["token"]
#=====================================================================
settings["myProfile"]["displayName"] = zarifogluProfile.displayName
settings["myProfile"]["statusMessage"] = zarifogluProfile.statusMessage
settings["myProfile"]["pictureStatus"] = zarifogluProfile.pictureStatus
cont = zarifoglu.getContact(zarifogluMID)
settings["myProfile"]["videoProfile"] = cont.videoProfile
coverId = zarifoglu.getProfileDetail()["result"]["objectId"]
settings["myProfile"]["coverId"] = coverId
#=====================================================================
#=====================================================================
with open("zarifoglu/temp.json", "r", encoding="utf_8_sig") as f:
    anu = json.loads(f.read())
    anu.update(settings)
    settings = anu
with open("zarifoglu/wait.json", "r", encoding="utf_8_sig") as f:
    itu = json.loads(f.read())
    itu.update(wait)
    wait = itu
with open('zarifoglu/by.json', 'r') as fp:
    wait = json.load(fp)
def sendFooter(to, isi):
    data = {
        "type": "text",
        "text": isi,
        "sentBy": {
            "label": "Turkey Team™",
            "iconUrl": "https://obs.line-scdn.net/{}".format(zarifoglu.getContact('u8894217061510fa60bf2592338441704').pictureStatus),
            "linkUrl": "line://ti/p/~zarifbirbey"
        }
    }
    sendTemplate(to, data)
def sendTemplate(to, data):
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1597127494-QDP2OlYl', xyzz)
    token = zarifoglu.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1597127494-QDP2OlYl', xyzz)
    token = client.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
def sendTemplate(group, data):
    xyz = LiffChatContext(group)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1597127494-QDP2OlYl', xyzz)
    token = zarifoglu.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))

def helppss(to):
    data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Turkey Team™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Chatbot",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=chatbot"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Feature",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=feature"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Images",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=images"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Profile",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=profile"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Protect",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=protect"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Social",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=social"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Timeline",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=timeline"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Translate",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=translate"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Settings",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=settings"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  }},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Turkey Team™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Banning",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=banning"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Wordban",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=wordban"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Friend",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=friend"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Self",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=self"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Memegen",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=memegen"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Kick",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=kick"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Utility",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=utility"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Github",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=github"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "About",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=about"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }
  }},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Turkey Team™",
                    "size": "xl",
                    "color": "#ffffff",
                    "weight": "bold"
                  }
                ],
                "margin": "lg"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "image",
                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png"
                  }
                ],
                "cornerRadius": "100px",
                "borderColor": "#ffffff",
                "borderWidth": "2px",
                "width": "40px",
                "height": "40px"
              }
            ]
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ]
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Group",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=group"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Mention",
                            "align": "center",
                            "size": "sm",
                            "color": "#ffffff",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=mention"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Steal",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=steal"
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "List",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=list"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Bcast",
                            "align": "center",
                            "color": "#ffffff",
                            "size": "xs",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=bcast"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Leave",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text="
                            }
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "separator"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Reboot",
                        "size": "sm",
                        "color": "#ffffff",
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=reboot"
                        }
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Timeleft",
                            "size": "sm",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=timeleft"
                            }
                          }
                        ]
                      },
                      {
                        "type": "separator"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Logout",
                            "size": "xs",
                            "color": "#ffffff",
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=logout"
                            }
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            ],
            "borderColor": "#ffffff",
            "borderWidth": "2px"
          }
        ]
      }
    ],
    "cornerRadius": "xl",
    "borderColor": "#ffffff",
    "borderWidth": "4px"
  },
  "styles": {
    "body": {
      "backgroundColor": "#000000"
    }}}]}}
    sendTemplate(to,data)

def helpalay(to):
    data={"type":"flex","altText":"ραчıɔαя™","contents":{
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "borderWidth": "4px",
    "borderColor": "{}".format(setbot["helpseparator"]),
    "cornerRadius": "xl",
    "contents": [
      {
        "type": "image",
        "url": "https://i.ibb.co/JxrVHwr/Pics-Art-12-07-05-46-40.jpg",
        "size": "full",
        "aspectMode": "cover",
        "aspectRatio": "1:1",
        "gravity": "center"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "ραчıɔαя™",
                    "size": "lg",
                    "color": "{}".format(setbot["text"]),
                    "weight": "bold",
                    "align": "center",
                    "offsetStart": "15px"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "Selfbots Edition",
                    "size": "sm",
                    "color": "{}".format(setbot["text"]),
                    "weight": "bold",
                    "align": "center"
                  }
                ]
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "spacer"
                  }
                ],
                "margin": "xs"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Login",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Login"
                        }
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Logout",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Logout"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Giriş",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Giriş"
                        }
                      },
                      {
                        "type": "spacer"
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Çıkış",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Çıkış"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "xl"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Reader",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Reader"
                        }
                      }
                    ],
                    "offsetStart": "0px"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Mentions",
                        "size": "sm",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Mentions"
                        }
                      }
                    ],
                    "offsetStart": "10px"
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "sm"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "spacer",
                    "size": "xxl"
                  },
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Addservice @",
                        "color": "{}".format(setbot["helptext"]),
                        "align": "center",
                        "action": {
                          "type": "uri",
                          "label": "action",
                          "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Addservice"
                        }
                      }
                    ],
                    "margin": "lg",
                    "offsetEnd": "20px"
                  },
                  {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Helper2",
                            "size": "sm",
                            "color": "{}".format(setbot["helptext"]),
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Helper2"
                            }
                          }
                        ],
                        "offsetEnd": "20px"
                      },
                      {
                        "type": "filler"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Helper3",
                            "size": "sm",
                            "color": "{}".format(setbot["helptext"]),
                            "align": "center",
                            "action": {
                              "type": "uri",
                              "label": "action",
                              "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Helper3"
                            }
                          }
                        ],
                        "offsetEnd": "40px"
                      },
                      {
                        "type": "filler"
                      }
                    ],
                    "margin": "md"
                  }
                ],
                "margin": "md"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "filler"
                  }
                ],
                "margin": "sm"
              }
            ],
            "spacing": "xs"
          }
        ],
        "position": "absolute",
        "offsetBottom": "0px",
        "offsetStart": "0px",
        "offsetEnd": "0px",
        "paddingAll": "20px"
      }
    ],
    "paddingAll": "0px"
  }
}]}}
    sendTemplate(to, data)
def foro(to, text):
    data = {
    "type": "flex",
    "altText": text,
    "contents": {
    "type": "bubble",
    "styles": {
    "footer": {
    "backgroundColor": "{}".format(setbot["background"])
    }
    },
    "footer": {
    "type": "box",
    "layout": "vertical",
     "cornerRadius": "xl",
    "borderWidth": "4px",
    "borderColor": "{}".format(setbot["separator"]),
    "spacing": "sm",
    "contents": [
    {
    "type": "box",
    "layout": "baseline",
    "contents": [
    {
    "type": "icon",
    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
    "size": "md"
    },
    {
    "type": "text",
    "text": text,
    "color": "{}".format(setbot["text"]),
    "gravity": "center",
    "align":"center",
    "wrap": True,
    "size": "md"
    },
    {
    "type": "icon",
    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
    "size": "md"
    },
    ]
    }
    ]
    }
    }
    }
    sendTemplate(to, data)
def helpss(to):
    ret_ = helpers(to)
    k = len(ret_)//10
    for aa in range(k+1):
        data = {
            "type": "flex",
            "altText": "Help",
            "contents": {
                "type": "carousel",
                "contents": ret_[aa*10 : (aa+1)*10]
            }
        }
        sendTemplate(to, data)
def helpers(to):
    ret_ = []
    ret_.append(
        {
            "styles": {"body": {"backgroundColor": "{}".format(setbot["background"])},"header": {"backgroundColor": "{}".format(setbot["background"])}},
            "type": "bubble",
            "body": {"contents": [{
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "spacer",
                        "size": "xxl"
                    },
                    {
                        "contents": [{
                        "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                        "size": "xxs",
                        "type": "image",
                        "action": {
                        "type": "uri",
                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Login%20sb"
                    }
                }, {
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                    "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Restart%20sb"
                                                    }
                                                },{
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                   "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Logout%20sb"
                                                    }
                                                }],
                                                "layout": "horizontal",
                                                "type": "box",
                                                "flex": 1
                                            }, 
                                                                 {
        "type": "box",
        "layout": "horizontal",
        "spacing": "xxl",       
        "contents": [
          {
            "type": "text", 
            "text": 'Login sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center",
          },
          {
            "type": "text",
            "text": 'Restart sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center"
          },
          {
            "type": "text", 
            "text": 'Logout sb',
            "color": "{}".format(setbot["text"]),
            "size": "xs"
          }
        ]
      },
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
       "type": "spacer",
       "size": "xl"
     }
],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }  
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical",
      }
    }
    )
    ret_.append(
        {
            "styles": {"body": {"backgroundColor": "{}".format(setbot["background"])},"header": {"backgroundColor": "{}".format(setbot["background"])}},
            "type": "bubble",
            "body": {"contents": [{
                "type": "box",
                "layout": "baseline",
                "contents": [
                    {
                        "type": "spacer",
                        "size": "xxl"
                    },
                    {
                        "contents": [{
                        "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                        "size": "xxs",
                        "type": "image",
                        "action": {
                        "type": "uri",
                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Reader"
                    }
                }, {
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                    "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Support"
                                                    }
                                                },{
                                                    "url": "https://i.ibb.co/PGJt3qP/Pics-Art-12-07-05-41-20.png",
                                                    "size": "xxs",
                                                   "type": "image",
                                                    "action": {
                                                        "type": "uri",
                                                        "uri": "line://app/1597127494-QDP2OlYl?type=fotext&text=Mentions"
                                                    }
                                                }],
                                                "layout": "horizontal",
                                                "type": "box",
                                                "flex": 1
                                            }, 
                                                                 {
        "type": "box",
        "layout": "horizontal",
        "spacing": "xxl",       
        "contents": [
          {
            "type": "text", 
            "text": 'Reader',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center",
          },
          {
            "type": "text",
            "text": 'Support',
            "color": "{}".format(setbot["text"]),
            "size": "xs",
            "align": "center"
          },
          {
            "type": "text", 
            "text": 'Mentions',
            "color": "{}".format(setbot["text"]),
            "size": "xs"
          }
        ]
      },
            ],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          },
          {
            "contents": [
              {
       "type": "spacer",
       "size": "xl"
     }
],
            "type": "box",
            "spacing": "xs",
            "layout": "vertical"
          }  
        ],
        "type": "box",
        "spacing": "xs",
        "layout": "vertical",
      }
    }
    )
    return ret_
def support(to):
    data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "carousel",
  "contents": [
    {
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://i.ibb.co/zHkYgV7/left.png",
                "offsetStart": "10px"
              },
              {
                "type": "text",
                "color": "#Ffffff",
                "text": "Friend search",
                "size": "md",
                "offsetStart": "20px"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "lg"
              }
            ]
          }
        ],
        "backgroundColor": "#464F69"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "offsetStart": "10px",
                "cornerRadius": "xl",
                "borderColor": "#adb5bd",
                "borderWidth": "6px",
                "width": "20px",
                "height": "20px"
              },
              {
                "type": "text",
                "text": "ID",
                "offsetStart": "18px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "xl",
                "borderWidth": "6px",
                "backgroundColor": "#adb5bd",
                "offsetEnd": "85px"
              },
              {
                "type": "text",
                "text": "Phone number",
                "offsetEnd": "75px"
              }
            ]
          },
          {
            "type": "spacer"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "zarifbirbey",
                "offsetStart": "10px",
                "size": "sm"
              }
            ],
            "borderColor": "#adb5bd",
            "borderWidth": "1px",
            "offsetStart": "10px"
          },
          {
            "type": "spacer",
            "size": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "filler"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "margin": "xxl",
            "cornerRadius": "100px",
            "height": "72px",
            "width": "72px",
            "offsetStart": "110px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').displayName),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Add Friend",
                        "size": "sm",
                        "color": "#Ffffff",
                        "align": "center"
                      }
                    ],
                    "borderWidth": "1px",
                    "backgroundColor": "#008000",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://line.me/ti/p/~zarifbirbey"
                    }
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "md"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ],
            "margin": "xxl"
          }
        ],
        "margin": "xxl"
      }
    ],
    "paddingAll": "0px"
  }
},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://i.ibb.co/zHkYgV7/left.png",
                "offsetStart": "10px"
              },
              {
                "type": "text",
                "color": "#Ffffff",
                "text": "Friend search",
                "size": "md",
                "offsetStart": "20px"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "lg"
              }
            ]
          }
        ],
        "backgroundColor": "#464F69"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "offsetStart": "10px",
                "cornerRadius": "xl",
                "borderColor": "#adb5bd",
                "borderWidth": "6px",
                "width": "20px",
                "height": "20px"
              },
              {
                "type": "text",
                "text": "ID",
                "offsetStart": "18px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "xl",
                "borderWidth": "6px",
                "backgroundColor": "#adb5bd",
                "offsetEnd": "85px"
              },
              {
                "type": "text",
                "text": "Phone number",
                "offsetEnd": "75px"
              }
            ]
          },
          {
            "type": "spacer"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "zarifbirbey",
                "offsetStart": "10px",
                "size": "sm"
              }
            ],
            "borderColor": "#adb5bd",
            "borderWidth": "1px",
            "offsetStart": "10px"
          },
          {
            "type": "spacer",
            "size": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "filler"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "margin": "xxl",
            "cornerRadius": "100px",
            "height": "72px",
            "width": "72px",
            "offsetStart": "110px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').displayName),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Add Friend",
                        "size": "sm",
                        "color": "#Ffffff",
                        "align": "center"
                      }
                    ],
                    "borderWidth": "1px",
                    "backgroundColor": "#008000",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://line.me/ti/p/~zarifbirbey"
                    }
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "md"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ],
            "margin": "xxl"
          }
        ],
        "margin": "xxl"
      }
    ],
    "paddingAll": "0px"
  }
},{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer"
          },
          {
            "type": "box",
            "layout": "baseline",
            "contents": [
              {
                "type": "icon",
                "url": "https://i.ibb.co/zHkYgV7/left.png",
                "offsetStart": "10px"
              },
              {
                "type": "text",
                "color": "#Ffffff",
                "text": "Friend search",
                "size": "md",
                "offsetStart": "20px"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "lg"
              }
            ]
          }
        ],
        "backgroundColor": "#464F69"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "spacer",
            "size": "xxl"
          },
          {
            "type": "box",
            "layout": "horizontal",
            "contents": [
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "offsetStart": "10px",
                "cornerRadius": "xl",
                "borderColor": "#adb5bd",
                "borderWidth": "6px",
                "width": "20px",
                "height": "20px"
              },
              {
                "type": "text",
                "text": "ID",
                "offsetStart": "18px"
              },
              {
                "type": "box",
                "layout": "vertical",
                "contents": [
                  {
                    "type": "text",
                    "text": "."
                  }
                ],
                "width": "20px",
                "height": "20px",
                "cornerRadius": "xl",
                "borderWidth": "6px",
                "backgroundColor": "#adb5bd",
                "offsetEnd": "85px"
              },
              {
                "type": "text",
                "text": "Phone number",
                "offsetEnd": "75px"
              }
            ]
          },
          {
            "type": "spacer"
          }
        ]
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "zarifbirbey",
                "offsetStart": "10px",
                "size": "sm"
              }
            ],
            "borderColor": "#adb5bd",
            "borderWidth": "1px",
            "offsetStart": "10px"
          },
          {
            "type": "spacer",
            "size": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "filler"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "margin": "xxl",
            "cornerRadius": "100px",
            "height": "72px",
            "width": "72px",
            "offsetStart": "110px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "text",
                "text": "{}".format(zarifoglu.getContact('u5d854616fc8ea66893e7a85b7cb0b9f1').displayName),
                "size": "md",
                "color": "#000000",
                "weight": "bold",
                "align": "center"
              },
              {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                  {
                    "type": "filler"
                  },
                  {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                      {
                        "type": "text",
                        "text": "Add Friend",
                        "size": "sm",
                        "color": "#Ffffff",
                        "align": "center"
                      }
                    ],
                    "borderWidth": "1px",
                    "backgroundColor": "#008000",
                    "action": {
                      "type": "uri",
                      "label": "action",
                      "uri": "http://line.me/ti/p/~zarifbirbey"
                    }
                  },
                  {
                    "type": "filler"
                  }
                ],
                "margin": "md"
              }
            ],
            "margin": "md"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "spacer",
                "size": "xxl"
              }
            ],
            "margin": "xxl"
          }
        ],
        "margin": "xxl"
      }
    ],
    "paddingAll": "0px"
  }}]}}
    sendTemplate(to,data)
def debug():
    get_profile_time_start = time.time()
    get_profile = zarifoglu.getProfile()
    get_profile_time = time.time() - get_profile_time_start
    get_group_time_start = time.time()
    get_group = zarifoglu.getGroupIdsJoined()
    get_group_time = time.time() - get_group_time_start
    get_contact_time_start = time.time()
    get_contact = zarifoglu.getContact(get_profile.mid)
    get_contact_time = time.time() - get_contact_time_start
    elapsed_time = time.time() - get_profile_time_start
    return " 「 Debug 」\n - Send Message\n   %.5f\n - Get Profile\n   %.5f\n - Get Contact\n   %.5f\n - Get Group\n   %.5f" % (elapsed_time,get_profile_time,get_contact_time,get_group_time)
#=====================================================================
def shareall(to, text):
    lol = zarifoglu.getGroupIdsJoined()
    for group in lol:
        zarifoglu.sendPostToTalk(group, text)
    zarifoglu.sendMessage(to, "Gönderi {} gruba gönderildi".format(str(len(lol))))
#=====================================================================
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
#=====================================================================
#def Template(to):
def sendMessageCustom(to, text, icon , name):
    annda = {'MSG_SENDER_ICON': icon,
        'MSG_SENDER_NAME':  name,
    }
    zarifoglu.sendMessage(to, text, contentMetadata=annda)
def sendMessageCustomContact(to, icon, name, mid):
    annda = { 'mid': mid,
    'MSG_SENDER_ICON': icon,
    'MSG_SENDER_NAME':  name,
    }
    zarifoglu.sendMessage(to, '', annda, 13)

def B64e(to, url):
	import base64
	return zarifoglu.sendMessage(to, base64.b64encode(url.encode()).decode())

def B64d(to, url):
	import base64
	return zarifoglu.sendMessage(to, base64.b64decode(url.encode()).decode())
	
def sendMention(to, mid, firstmessage='', lastmessage=''):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        try:
            zarifoglu.sendMessage(to, text, {'MSG_SENDER_NAME': zarifoglu.getContact(mid).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + zarifoglu.getContact(mid).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        except Exception as e:
            zarifoglu.sendMessage(to, text, {'MSG_SENDER_NAME': zarifoglu.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").displayName,'MSG_SENDER_ICON': 'http://dl.profile.line-cdn.net/' + zarifoglu.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        print(error)
def mentions(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PydrFans  "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    zarifoglu.sendMessage(to, textx, {'AGENT_NAME':'LINE OFFICIAL', 'AGENT_LINK': 'line://ti/p/~{}'.format(zarifoglu.getProfile().userid), 'AGENT_ICON': "http://dl.profile.line-cdn.net/" + zarifoglu.getContact("u085311ecd9e3e3d74ae4c9f5437cbcb5").picturePath, 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def changeVideoAndPictureProfile(pict, vids):
    try:
        files = {'file': open(vids, 'rb')}
        obs_params = zarifoglu.genOBSParams({'oid': zarifogluMID, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = zarifoglu.server.postContent('{}/talk/vp/upload.nhn'.format(str(zarifoglu.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return "Failed update profile"
        zarifoglu.updateProfilePicture(pict, 'vp')
        return "Success update profile"
    except Exception as e:
        raise Exception("Error change video and picture profile {}".format(str(e)))
        os.remove("zarifogluWasHere.mp4")
#=====================================================================
def speedtest(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    weaks, days = divmod(days,7)
    if days == 0:
        return '%02d' % (secs)
    elif days > 0 and weaks == 0:
        return '%02d' %(secs)
    elif days > 0 and weaks > 0:
        return '%02d' %(secs)
        
def change(url):
	import base64
	return base64.b64encode(url.encode()).decode()
	
def tagdia(to, text="",ps='', mids=[]):
        arrData = ""
        arr = []
        mention = "@MentionOrang "
        if mids == []:
            raise Exception("Invalid mids")
        if "@!" in text:
            if text.count("@!") != len(mids):
                raise Exception("Invalid mids")
            texts = text.split("@!")
            textx = ''
            h = ''
            for mid in range(len(mids)):
                h+= str(texts[mid].encode('unicode-escape'))
                textx += str(texts[mid])
                if h != textx:slen = len(textx)+h.count('U0');elen = len(textx)+h.count('U0') + 13
                else:slen = len(textx);elen = len(textx) + 13
                arrData = {'S':str(slen), 'E':str(elen), 'M':mids[mid]}
                arr.append(arrData)
                textx += mention
            textx += str(texts[len(mids)])
        else:
            textx = ''
            slen = len(textx)
            elen = len(textx) + 18
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
            arr.append(arrData)
            textx += mention + str(text)
        zarifoglu.sendMessage(to, textx, {'MSG_SENDER_NAME': zarifoglu.getContact(ps).displayName,'MSG_SENDER_ICON': "http://dl.profile.line-cdn.net/" + zarifoglu.getContact(ps).pictureStatus,'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
#=====================================================================
def logError(text):
    zarifoglu.log("ERROR 404 !\n" + str(text))
    tz = pytz.timezone("Asia/Jakarta")
    timeNow = datetime.now(tz=tz)
    timeHours = datetime.strftime(timeNow,"(%H:%M)")
    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    inihari = datetime.now(tz=tz)
    hr = inihari.strftime('%A')
    bln = inihari.strftime('%m')
    for i in range(len(day)):
        if hr == day[i]: hasil = hari[i]
    for k in range(0, len(bulan)):
        if bln == str(k): bln = bulan[k-1]
    time = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + " | " + inihari.strftime('%H:%M:%S')
    with open("zarifoglu/errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
#=====================================================================
#=====================================================================
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd
#=====================================================================
def likeNotify(to):
    true = True
    data = {
        "type": "flex",
        "altText": "LIKE BILDIRIMI",
        "contents": {
            "type": "bubble",
            "styles": {
                "header": {
                    "backgroundColor": "#333333"
                },
                "hero": {
                    "backgroundColor": "#333333"
                },
                "body": {
                    "backgroundColor": "#FFFFFF",
                    "separator": true,
                    "separatorColor": "#FFFFFF"
                },
                "footer": {
                    "backgroundColor": "#333333",
                    "separator": true
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "LIKE BILDIRIMI",
                        "weight": "bold",
                        "size": "xxl",
                        "color": "#000000",
                        "margin": "md"
                    },
                    {
                        "type": "text",
                        "text": "Your Post Has Been Liked",
                        "size": "xs",
                        "color": "#aaaaaa",
                        "wrap": true
                    },
                    {
                        "type": "separator",
                        "margin": "xxl"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "xxl",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "SELFBOT KİRALA",
                                        "weight": "bold",
                                        "color": "#000000",
                                        "size": "sm",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "ÖDEME :",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• Selfbot",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "80 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• Helper",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "300 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "• KORUMA",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    },
                                    {
                                        "type": "text",
                                        "text": "150 ₺",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "align": "end"
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "horizontal",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Get free 100 accounts autolike bots",
                                        "size": "sm",
                                        "color": "#aaaaaa",
                                        "flex": 0
                                    }
                                ]
                            },
                            {
                                "type": "separator",
                                "margin":"md"
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "text",
                                "text": "Sunucu mu istiyorsun ?",
                                "size": "xs",
                                "color": "#000000",
                                "flex": 0
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "spacer",
                                "size": "xl"
                            },
                            {
                                "type": "button",
                                "action": {
                                    "type": "uri",
                                    "label": "İletişime geç",
                                    "uri": "line://ti/p/~zarifbirbey"
                                },
                                "style": "primary",
                                "color": "#000000"
                            }
                        ]
                    }
                ]
            }
        }
    }
    sendTemplate(to, data)
#=====================================================================
def removeCmd(cmd, text):
	key = settings["keyCommand"]
	if settings["setKey"] == False: key = ''
	rmv = len(key + cmd) + 1
	return text[rmv:]
def backupData():
    try:
        backup = settings
        f = codecs.open('zarifoglu/temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = wait
        f = codecs.open('zarifoglu/wait.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        f = codecs.open('zarifoglu/user.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = java
        f = codecs.open('zarifoglu/java.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        f = codecs.open('zarifoglu/by.json','w','utf-8')
        json.dump(wait, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = premium
        return True
    except Exception as error:
        logError(error)
        return False
#=====================================================================
def bcTemplate(gr, data):
    xyz = LiffChatContext(gr)
    xyzz = LiffContext(chat=xyz)
    view = LiffViewRequest('1597127494-QDP2OlYl', xyzz)
    token = zarifoglu.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
#=====================================================================
async def zarifogluBot(op):
    try:
        if settings["restartPoint"] != None:
            zarifoglu.sendMessage(settings["restartPoint"], 'Activated♪')
            settings["restartPoint"] = None
        if op.type == 0:
            return
                        
        if op.type in [22,24]:
            zarifoglu.leaveRoom(op.param1)
#=====================================================================
        if op.type in [13,124]:
            if zarifoglu.getProfile().mid in op.param3:
                G = zarifoglu.getCompactGroup(op.param1)
                if settings["autoJoin"] == True:
                    zarifoglu.acceptGroupInvitation(op.param1)
        if op.type == 15:
            #print ("[ 15 ] NOTIFIED LEAVE GROUP")
            if lvin["lMessage"] == True:
                mat = zarifoglu.getContact(op.param2)
                fit = zarifoglu.getCompactGroup(op.param1)
                pesanya = lvin["textnya"]
                data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Bye bye {}".format(str(mat.displayName)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesanya),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                sendTemplate(op.param1,data)
        if op.type == 17:
            #print ("[ 17 ] NOTIFIED INVITE INTO GROUP")
            if wmin["wMessage"] == True:
                mat = zarifoglu.getContact(op.param2)
                fit = zarifoglu.getCompactGroup(op.param1)
                pesanya = wmin["textnya"]
                data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(mat.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello {}".format(str(mat.displayName)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "Welcome to {}".format(str(fit.name)),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesanya),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                sendTemplate(op.param1,data)
        if op.type == 19:
                    zarif = zarifoglu.getContact(op.param2)
                    neon = zarifoglu.getContact(op.param3)
                    data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "cornerRadius": "xl",
    "borderWidth": "4px",
    "borderColor": "#ffffff",
    "contents": [
      {
        "type": "text",
        "text": "KICK NOTIFY",
        "weight": "bold",
        "size": "xxl",
        "margin": "md"
      },
      {
        "type": "separator",
        "color": "#000000"
      },
      {
        "type": "text",
        "text": "Execution :",
        "weight": "bold",
        "size": "md",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(zarif.pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "30px",
            "height": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": f"{zarifoglu.getContact(op.param2).displayName}",
                    "size": "md",
                    "color": "#000000"
                  }
                ],
                "spacing": "md",
                "margin": "sm",
                "offsetTop": "2px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "6px"
      },
      {
        "type": "text",
        "text": "Victim :",
        "weight": "bold",
        "size": "md",
        "margin": "md"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "image",
                "url": "https://obs.line-scdn.net/{}".format(neon.pictureStatus),
                "aspectMode": "cover",
                "size": "full"
              }
            ],
            "cornerRadius": "100px",
            "width": "30px",
            "height": "30px"
          },
          {
            "type": "box",
            "layout": "vertical",
            "contents": [
              {
                "type": "box",
                "layout": "baseline",
                "contents": [
                  {
                    "type": "text",
                    "text": f"{zarifoglu.getContact(op.param3).displayName}",
                    "size": "md",
                    "color": "#000000"
                  }
                ],
                "spacing": "md",
                "margin": "sm",
                "offsetTop": "2px"
              }
            ]
          }
        ],
        "spacing": "xl",
        "paddingAll": "6px"
      }
    ],
    "paddingAll": "0px"
  }
}}
                    sendTemplate(op.param1,data)
#=====================================================================
        if op.type == 26:
            #print ("[ 26 ] RECEIVE MESSAGE")
            msg = op.message
            text = str(msg.text)
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            zariftag = "u79916ca401217606c21a2f568d3e51df"
            to = msg.to
            cmd = command(text)
            isValid = True
            setKey = settings["keyCommand"].title()
            if settings["setKey"] == False: setKey = ''
            if isValid != False:
                if msg.toType == 0 and sender != zarifogluMID: to = sender
                else: to = receiver
                if msg.contentType == 6:
                    try:
                        contact = zarifoglu.getContact(sender)
                        if msg.toType == 2:
                            anu = zarifoglu.getGroup(to)
                            if msg.contentMetadata['GC_EVT_TYPE'] == 'S' and msg.contentMetadata['GC_MEDIA_TYPE'] == 'LIVE':
                                anu = msg.contentMetadata={'GC_EVT_TYPE': 'S', 'GC_CHAT_MID': to, 'RESULT': 'INFO', 'SKIP_BADGE_COUNT': 'false', 'GC_IGNORE_ON_FAILBACK': 'false', 'TYPE': 'G', 'DURATION': '0', 'GC_MEDIA_TYPE': 'VIDEO', 'VERSION': 'X', 'CAUSE': '16'}
                    except Exception as e:
                        zarifoglu.sendMessage(to, str(e))
                if msg.contentType == 14:
                    if hoho["savefile"] == True:
                        try:
                             namafile = hoho["namafile"]
                             zarifoglu.downloadObjectMsg(msg_id,saveAs=namafile)
                             hoho["savefile"] = False
                             zarifoglu.sendMessage(to, "Successful, the file has been uploaded")
                        except Exception as e:
                         	zarifoglu.sendMessage(to, str(e))
                if msg.contentType == 1:
                    if settings["changePicture"] == True:
                        path = zarifoglu.downloadObjectMsg(msg_id, saveAs="tmp/pict.bin")
                        settings["changePicture"] = False
                        zarifoglu.updateProfilePicture(path)
                        zarifoglu.sendMessage(to,"Profile Image Updated.")
                if msg.contentType == 1: 
                    if settings["changeCoverProfile"] == True:
                        path = zarifoglu.downloadObjectMsg(msg_id)
                        settings["changeCoverProfile"] = False
                        zarifoglu.updateProfileCover(path)
                        zarifoglu.sendMessage(to,"Cover Image Updated.")                                           
                if msg.contentType in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]:
                    if msg.toType == 0:
                        if settings["autoRead"] == True:
                            zarifoglu.sendChatChecked(to, msg_id)
                    if msg.toType == 2:
                        if settings["autoRead1"] == True:
                            zarifoglu.sendChatChecked(to, msg_id)
                if msg.contentType == 0:
                    if "/ti/g/" in text.lower():
                        if settings["autoJoin"] == True:
                            link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                            links = link_re.findall(text)
                            n_links = []
                            for l in links:
                                if l not in n_links:
                                   n_links.append(l)
                            for ticket_id in n_links:
                                group = zarifoglu.findGroupByTicket(ticket_id)
                                if len(group.members) >= wait["Members"]:
                                    zarifoglu.acceptGroupInvitationByTicket(group.id,ticket_id)
                                else:
                                    zarifoglu.acceptGroupInvitationByTicket(group.id,ticket_id)
                                    zarifoglu.leaveGroup(group.id)
                    if msg._from in myAdmin:
                        if "/remote" in cmd:
                            function = lambda s:s[:1].lower() + s[1:] if s else ''
                            number = cmd.split("/remote:")[1];number = number.split()[0];zarifoglu.getGroupIdsJoined()
                            if number.isdigit():number = int(number);group = zarifoglu.getGroupIdsJoined()[number-1];to = group
                            cmd = cmd.replace("/remote:%s"%number,"").lstrip().rstrip()
                            if '/remote:' in text:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            else:text = text.replace("/remote:%s"%number,"").lstrip().rstrip();function(text)
                            if msg.toType == 0:msg.to = sender
                            elif msg.toType == 2:msg.to = msg.to
                            sendFooter(msg.to, "Command '%s' has been send to : %s" % (cmd, zarifoglu.getGroup(group).name))
#==========================================
                    if cmd == "threads":
                        zarifoglu.sendMessage(to,'Threads: {}'.format(threading.active_count()))
                        log.info("Debug Threads.")                            
#==========================================
                    elif cmd.startswith("savefile"):
                        if msg._from in myboss:
                            text = removeCmd("savefile", text)
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ", text)
                            if " " in key:
                                zarifoglu.sendMessage(to, "Failed !")
                            else:
                                hoho["namafile"] = str(key).lower()
                                hoho["savefile"] = True
                                zarifoglu.sendMessage(to, "Send file to save to be「 {} 」".format(str(key).lower()))
                    elif cmd.startswith("exec"):
                        if msg._from in myboss:
                            try:
                                sep = text.split("\n")
                                txt = text.replace(sep[0] + "\n","")
                                exec(txt)
                            except:
                                pass
#==========================================
                    elif cmd.startswith("down "):
                        if msg._from in myAdmin:
                           number = removeCmd("down", text)
                           if len(number) > 0:
                               if number.isdigit():
                                   number = int(number)
                                   if number > 5000:                                             
                                       zarifoglu.sendMessage(to,"invalid >_< ! Max: 5000.")
                                   else:
                                       for i in range(0,number):
                                           zarifoglu.sendMessage(to,str(number))
                                           number -= 1
                                           time.sleep(0.008)
                               else:
                                  zarifoglu.sendMessage(to,"Please specify a valid number.")
                    elif cmd == "change dp" :
                        if msg._from in myAdmin:
                            settings["changePicture"] = True
                            zarifoglu.sendMessage(to, "Send a Image to change picture.")
                    elif cmd == "change cover":
                        if msg._from in myAdmin:
                            settings["changeCoverProfile"] = True
                            zarifoglu.sendMessage(to,"Send a Image to change cover.")
                    elif cmd == "read on":
                        tailah["siderTemp"][receiver] = []
                        zarifoglu.sendMessage(to, "Getreader set to on.")
                    elif cmd == "read off":
                        if receiver in tailah["siderTemp"]:
                            del tailah["siderTemp"][receiver]
                            zarifoglu.sendMessage(to, "Getreader set to off.")
                    elif cmd == "welcome on":
                        if wmin["wMessage"] == True:
                            msgs=" 「 Welcome 」\nWelcomemsg already Enable♪"
                        else:
                            msgs=" 「 Welcome 」\nWelcomemsg set to Enable♪"
                            wmin["wMessage"] = True
                        zarifoglu.sendMessage(to, msgs)
                    elif cmd == "welcome off":
                        if wmin["wMessage"] == False:
                            msgs=" 「 wMessage 」\nWelcomemsg already DISABLED♪"
                        else:
                            msgs=" 「 Welcome 」\nWelcomemsg set to DISABLED♪"
                            wmin["wMessage"] = False
                        zarifoglu.sendMessage(to, msgs)
                    elif cmd == "leave on":
                        if lvin["lMessage"] == True:
                            msgs=" 「 Leave 」\nLeavemsg already Enable♪"
                        else:
                            msgs=" 「 Leave 」\nLeavemsg set to Enable♪"
                            lvin["lMessage"] = True
                        zarifoglu.sendMessage(to, msgs)
                    elif cmd == "leave off":
                        if lvin["lMessage"] == False:
                            msgs=" 「  Leave 」\nLeavemsg already DISABLED♪"
                        else:
                            msgs=" 「  Leave  」\nLeavemsg set to DISABLED♪"
                            lvin["lMessage"] = False
                        zarifoglu.sendMessage(to, msgs)
                    elif cmd.startswith("updatername "):
                        if msg._from in myAdmin:
                            key = removeCmd("updatername", text)
                            kiy = settings["keyCommand"]
                            settings["keyCommand"] = str(key).lower()
                            zarifoglu.sendMessage(to, "╭──「 Update Rname 」\n│ ⌬ Status : Success\n│ ⌬ From : "+str(kiy.title())+"\n╰To : "+str(key.title()))
                    elif cmd == "java":
                        if msg._from in myAdmin:               
                            helpz="Java code :\n" 
                            helpz+="\n• Kickall > " + str(javascript['jskick1'])
                            helpz+="\n• Bypass > " + str(javascript['jskick'])
                            helpz+="\n• Cancel > " + str(javascript['cancels'])
                            helpz+="\n\nSettings :\n"
                            helpz+="\n• Change 1 <txt>"
                            helpz+="\n• Change 2 <txt>"
                            helpz+="\n• Change 3 <txt>"
                            zarifoglu.sendMessage(to,helpz)
                    elif cmd.startswith("change"):
                        if msg._from in myAdmin:               
           #                 textx = text.replace(text.split(" ")[0]+" ","")
                            textx = removeCmd("change", text)
                            sal = textx.lower()
                            if sal.startswith("kickall"):
                               texts = textx[2:]
                               javascript["jskick1"] = texts
                               zarifoglu.sendMessage(to, "Kickall update to `%s`" % texts)
                            if sal.startswith("2"):
                               texts = textx[2:]
                               javascript["jskick"] = texts
                               zarifoglu.sendMessage(to, "Bypass update to `%s`" % texts)
                            if sal.startswith("3"):
                               texts = textx[2:]
                               javascript["cancels"] = texts
                               zarifoglu.sendMessage(to, "Cancel update to `%s`" % texts)
                    elif cmd == javascript['jskick1']:
                        if msg._from in myAdmin:               
                          xyz = zarifoglu.getGroup(to)
                          mem = [c.mid for c in xyz.members]
                          targets = []
                          for x in mem:
                            if x not in ["u5d854616fc8ea66893e7a85b7cb0b9f1","u8894217061510fa60bf2592338441704",zarifoglu.profile.mid]:targets.append(x)
                          if targets:
                            imzarif = 'simple.js gid={} token={} app={}'.format(to, zarifoglu.authToken, "IOSIPAD\t11.2.5\tiPhone X\t11.2.5")
                            for target in targets:
                              imzarif += ' uid={}'.format(target)
                            success = execute_js(imzarif)
                            if success:zarifoglu.sendMessage(to, "Success kick %i members." % len(targets))
                            else:zarifoglu.sendMessage(to, "Failed kick %i members." % len(targets))
                          else:zarifoglu.sendMessage(to, "Target not found.")
                    elif cmd == javascript['jskick']:
                        if msg._from in myAdmin: 
                          xyz = zarifoglu.getGroup(to)
                          if xyz.invitee == None:pends = []
                          else:pends = [c.mid for c in xyz.invitee]
                          targp = []
                          for x in pends:
                            if x not in ["u5d854616fc8ea66893e7a85b7cb0b9f1","u8894217061510fa60bf2592338441704",zarifoglu.profile.mid]:targp.append(x)
                          mems = [c.mid for c in xyz.members]
                          targk = []
                          for x in mems:
                            if x not in ["u5d854616fc8ea66893e7a85b7cb0b9f1","u8894217061510fa60bf2592338441704",zarifoglu.profile.mid]:targk.append(x)
                          imzarif = 'dual.js gid={} token={}'.format(to, zarifoglu.authToken)
                          for x in targp:imzarif += ' uid={}'.format(x)
                          for x in targk:imzarif += ' uik={}'.format(x)
                          execute_js(imzarif)
                    elif cmd == javascript["cancels"]:
                        if msg._from in myAdmin: 
                            group = zarifoglu.getGroup(to)
                            cm = 'clear.js gid={} token={}"'.format(to, zarifoglu.authToken)
                            for invitees in group.invitee:
                                  cm += ' uid={}'.format(invitees.mid)
                            print(cm)
                            success = execute_js(cm)
#==========================================
                    elif cmd.startswith("mentionmid "):
                            contact = removeCmd("mentionmid", text)
                            sendMention(to, contact)
							
                    elif cmd.startswith("iletişimbul "):
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   zarifoglu.sendMessage(msg.to, "•  Kişiyi Ekle  •")
                               else:
                                   mi_d = str(key)
                                   zarifoglu.sendContact(to,mi_d)
								   
                    elif cmd.startswith("! "):
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               mi_d = str(key)
                               zarifoglu.sendContact(to,mi_d)
								   
                    if cmd == "kiss me":
                        zarifoglu.generateReplyMessage(msg.id)
                        zarifoglu.sendReplyMessage(msg.id, to,"。。・゜゜・❤ "+zarifoglu.getContact(sender).displayName+" ❤ \n(づ￣ ³￣)づ")
                    elif cmd == "reader":
                        ret = "Now set : " + str(tailah["siderPesan"])
                        ret += "\n\n⌬ {}read on/off".format(setKey)
                        ret += "\n⌬ {}read set <text>".format(setKey)
                        zarifoglu.sendMessage(to, str(ret))
                    elif cmd == "leave":
                        ret = "Now set : " + str(lvin["textnya"])
                        ret += "\n\n⌬ {}leave on/off".format(setKey)
                        ret += "\n⌬ {}leave set <text>".format(setKey)
                        zarifoglu.sendMessage(to, str(ret))
                    elif cmd == "welcome":
                        ret = "Now set : " + str(wmin["textnya"])
                        ret += "\n\n⌬ {}welcome on/off".format(setKey)
                        ret += "\n⌬ {}welcome set <text>".format(setKey)
                        zarifoglu.sendMessage(to, str(ret))
                    elif cmd == ".":
                        if msg._from in myAdmin:
                            if msg.toType == 2:
                                group = zarifoglu.getGroup(to)
                                if group.invitee is None or group.invitee == []:
                                    zarifoglu.sendMessage(msg.to, "No invites Pending")
                                else:
                                    invitee = [contact.mid for contact in group.invitee]
                                    for inv in invitee:
                                        zarifoglu.cancelGroupInvitation(to, [inv])
                                        zarifoglu.findAndAddContactsByMid(inv)                                        
                                        zarifoglu.inviteIntoGroup(to, [inv])
#==========================================
                    elif cmd.startswith("read set "):
                        text_ = removeCmd("read set", text)
                        try:
                            tailah["siderPesan"] = text_
                            zarifoglu.sendMessage(to,"「 Get Reader 」\nChanged to : " + text_)
                        except:
                            foto(to,"「Get Reader 」\nFailed to replace message")
                    elif cmd.startswith("leave set "):
                        text_ = removeCmd("leave set", text)
                        try:
                            lvin["textnya"] = text_
                            zarifoglu.sendMessage(to,"「 LeaveMsg 」\nChanged to : " + text_)
                        except:
                            zarifoglu.sendMessage(to,"「 LeaveMsg 」\nFailed to replace message")
                    elif cmd.startswith("welcome set "):
                        text_ = removeCmd("welcome set", text)
                        try:
                            wmin["textnya"] = text_
                            zarifoglu.sendMessage(to,"「 WelcomeMsg 」\nChanged to : " + text_)
                        except:
                            zarifoglu.sendMessage(to,"「 WelcomeMsg 」\nFailed to replace message")
                    elif cmd.startswith("bye "):
                        if msg._from in myAdmin:
                            number = removeCmd("bye", text)
                            groups = zarifoglu.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = zarifoglu.getGroup(group)
                                try:
                                    zarifoglu.leaveGroup(G.id)
                                except:
                                    zarifoglu.leaveGroup(G.id)
                                zarifoglu.sendMessage(to, "「Leave 」\n\nGroup : " + G.name)
                            except Exception as error:
                                zarifoglu.sendMessage(to, str(error))
                    elif cmd == "support":
                        support(to)
                    elif cmd.startswith("thegoldsystem "):
                        if msg._from in myAdmin:
                                a=subprocess.getoutput(zarifoglu.mainsplit(msg.text))
                                k = len(a)//10000
                                for aa in range(k+1):
                                    try:
                                        zarifoglu.sendReplyMessage(msg.id,to,'{}'.format(a.strip()[aa*10000 : (aa+1)*10000]))
                                    except:
                                        zarifoglu.sendMessage(to, "Sᴜɴᴜᴄᴜᴅᴀᴋɪ Gᴇʀᴇᴋꜱɪᴢ Dᴏꜱʏᴀʟᴀʀ Vᴇ Çöᴘʟᴇʀ Tᴇᴍɪᴢʟᴇɴᴅɪ")

                    elif cmd == "giriş" or cmd =="login":
                                zarifoglu.generateReplyMessage(msg.id)
                                if sender in wait['info']:
                                        us = wait["info"][sender]
                                        ti = wait['name'][us]["pay"]-time.time()
                                        sec = int(ti %60)
                                        minu = int(ti/60%60)
                                        hours = int(ti/60/60 %24)
                                        days = int(ti/60/60/24)
                                        wait['name'][us]["pay"] = wait['name'][us]["pay"]
                                        if wait["name"][us]["pay"] <= time.time():
                                            os.system('rm -rf {}'.format(us))
                                            os.system('screen -S %s -X kill'%us)
                                            mentions(to, 'Üzgünüm @! Botunun süresi dolmuş. Lütfen sahibimle iletişime geç', [sender])
                                        else:
                                            us = wait["info"][sender]
                                            try:
                                                def zarif():                                       
                                                    token = QRV2(to)												
                                                    os.system('screen -S %s -X kill'%us)
                                                    os.system('cp -r TheneonS2 {}'.format(us))
                                                    os.system('cd {} && echo -n "{}" > token.txt'.format(us, token))
                                                    os.system('screen -dmS {}'.format(us))
                                                    os.system('screen -r {} -X stuff "cd {} && python3 theneon.py \n"'.format(us, us))
                                                    contact = zarifoglu.getContact(sender)
                                                    zarifoglu.sendMessage(to, "𝗟𝗢𝗚𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟:-\n Dosya Adı: {}\nKALAN ZAMAN: {} Gün {} Saat {} Dakika".format(us,days,hours,minu))
                                                    zarifoglu.sendMessage(to, "Lütfen speed yazın. Botunuz tepki veriyorsa çıkış yazmayın!!.. Gereksiz yere çıkış giriş yapanlar bi süre bottan silinecektir.")
                                                thread = threading.Thread(target=zarif)
                                                thread.daemon = True
                                                thread.start()
                                                backupData()
                                            except:
                                                pass
                                else:
                                    mentions(to, ' Merhaba @!\n İletişimini listede göremiyorum. Bot almak istiyorsan @! iletişime geçebilirsin..', [sender, "u5d854616fc8ea66893e7a85b7cb0b9f1"])
                                    backupData()

                    elif cmd == "liff" or cmd =="onay":
                                                    pincode = ["https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQA_KOllZwA8wuO5Rvw_AX-AVNkVmWWsTJmPQ1pgbVkraFqw2n8","https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSc5OttglDVREf7smgxBZ7ahxeeWEuHhRCseHk9YhorhTTHChQL","https://www.pixelstalk.net/dark-blue-background-free-download/"]
                                                    data = {
"type": "flex",
"altText": "ONAY VER",
"contents": {
  "type": "bubble",
  "size": "micro",
  "hero": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": random.choice(pincode),
        "position": "absolute",
        "align": "center",
        "size": "full",
        "aspectMode": "cover",
        "action": {"type": "uri","label": "action","uri": "line://app/1597127494-QDP2OlYl?type=text=Help"}
      },
      {
        "type": "text",
        "text": "- ONAY VER -",
        "color": "#ffffff",
        "weight": "bold",
        "size": "md",
        "offsetStart": "30px",
        "action": {"type": "uri","label": "action","uri": "line://app/1597127494-QDP2OlYl?type=text=Help"}
      },
      {
        "type": "text",
        "text": "Liff Onayla",
        "color": "#ffffff",
        "size": "xxl",
        "weight": "bold",
        "offsetTop": "-5px",
        "offsetStart": "2px",
        "action": {"type": "uri","label": "action","uri": "line://app/1597127494-QDP2OlYl?type=text=Help"}
      }
    ],
    "height": "60px",
    "backgroundColor": "#000000",
    "borderWidth": "2px",
    "borderColor": "#8b0000",
    "cornerRadius": "10px"
  }
}
}
                                                    sendTemplate(to, data)
													
                    elif cmd.startswith("liff2"):
                            zarifoglu.sendMessage(to, "line://app/1597127494-QDP2OlYl")
													
                    elif cmd == "helper":
                        try:
                            help = "Rname : {}".format(setKey)
                            help += "\nSname : Turkey"
                            help += "\n\nGeneral Commands :\n"
                            help += "\n⌬ {}reader".format(setKey)
                            help += "\n⌬ {}mentions".format(setKey)
                            help += "\n\nService Commands :\n"
                            help += "\n⌬ {}login".format(setKey)
                            help += "\n⌬ {}logout".format(setKey)
                            help += "\n⌬ {}restart".format(setKey)
                            help += "\n\nOwner Commands :\n"
                            help += "\n⌬ {}addservice".format(setKey)
                            help += "\n⌬ {}delservice".format(setKey)
                            help += "\n⌬ {}list service".format(setKey)
                            help += "\n\nAuthor : @!                  "
                            mentions(to, str(help),[zariftag])
                        except Exception as error:
                            zarifoglu.sendMessage(to, "「 Result Error 」\n" + str(error))
#==========================================
#Süresiz
                    elif cmd == "login":
                        if msg._from in premium["myService"]:
                            zarifoglu.sendMention(msg.to, '⌬ User : @!\n⌬ Type : {}logout'.format(setKey),' ', [msg._from])
                    elif cmd == "logout" and msg._from in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            del premium['listLogin'][msg._from]
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('rm -rf {}'.format(str(user)))
                            time.sleep(2)
                            zarifoglu.sendMention(msg.to, '⌬ User: @!\n⌬ Stats : Success to logout',' ', [msg._from])
                    elif cmd == "logout" and msg._from not in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            zarifoglu.sendMention(msg.to, '⌬ User : @!\n⌬ Type : {}login'.format(setKey),' ', [msg._from])
							
                    elif cmd == "giriş":
                        if msg._from in premium["myService"]:
                            zarifoglu.sendMention(msg.to, '⌬ Kullanıcı : @!\n⌬ Yorum : {}Önce Çıkış Yazınız'.format(setKey),' ', [msg._from])

                    elif cmd == "çıkış" and msg._from not in premium['listLogin']:
                        if msg._from in premium["myService"]:
                            zarifoglu.sendMention(msg.to, '⌬ Kullanıcı : @!\n⌬ Yorum : {}Giriş yazınız'.format(setKey),' ', [msg._from])
							
                    elif text.lower().startswith("addme "):
                        if msg._from not in premium['myService']:
                            nama = str(text.split(' ')[1])
                            premium['myService'][msg._from] =  '%s' % nama
                            zarifoglu.sendMention(msg.to, "「 Add Me 」 \nAdd @! to Login..","",[msg._from])
                        else:
                            zarifoglu.sendMention(msg.to, "「Add Me 」\nOwner @! already in List..","",[msg._from])
#==========================================
                    elif text.lower().startswith("eklemid") and msg._from in myAdmin and to not in chatbot["botOff"]:
                        anu = msg.text.split(" ")
                        anu2 = msg.text.replace(anu[0] + " ","")
                        anu3 = anu2.split(" ")
                        nama = str(anu3[0])
                        mid = str(anu3[1])
                        if mid not in wait['info']:
                            pay = time.time()
                            wait['name'][nama] =  {"mid":mid,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                            wait['info'][mid] =  '%s' % nama
                            zarifoglu.sendMention(to, '「 Servis 」\n @! Üye listesine eklendi ','', [mid])
                        if mid in wait['info']:
                            zarifoglu.sendMention(to, '「 Servis 」\n@! Zaten üye listesinde var  ','', [mid])  

                    if text.lower().startswith('süreekle') and sender in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        wait['name'][wait['info'][key1]]['pay'] = wait['name'][wait['info'][key1]]['pay']+60*60*24*30
                                        mentions(msg.to, ' Dostum @! Selfbotun şimdi yenilendi ve şu tarihte sona erecek: {}'.format(humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][key1]]["pay"]))), [key1])
                                    else:pass
#==============================================================================================
                    if text.lower().startswith('ekle ') and msg._from in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 not in wait['info']:
                                        pay = time.time()
                                        nama = str(text.split(' ')[1])
                                        wait['name'][nama] =  {"mid":key1,"pay":pay+60*60*24*30,"runtime":pay,"token":{}}
                                        wait['info'][key1] =  '%s' % nama
                                        mentions(msg.to, ' 「 Add Service 」\n@! Servise eklendi',[key1])
                                    else:
                                        mentions(msg.to, ' 「 Add Service 」\n@! Zaten listede var',[key1])

                    if text.lower().startswith('sil ') and msg._from in myAdmin:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    if key1 in wait['info']:
                                        b = wait['info'][key1]
                                        os.system('screen -S %s -X kill'%b)
                                        try:subprocess.getoutput('rm -rf {}'.format(b))
                                        except:pass
                                        del wait['info'][key1]
                                        del wait['name'][b]
                                        mentions(to, ' 「 Del Service 」\n@! Servisten silindi', [key1])
                                    else:
                                        mentions(to, ' 「 Del Service 」\n@! Listede yok.', [key1])

                    if text.lower() == 'üyelistesi' and msg._from in muhasebe:
                                h = [a for a in wait['info']]
                                k = len(h)//20
                                for aa in range(k+1):
                                    if aa == 0:dd = '「 List Login 」';no=aa
                                    else:dd = '';no=aa*20
                                    msgas = dd
                                    for a in h[aa*20:(aa+1)*20]:
                                        no+=1
                                        if wait['name'][wait['info'][a]]["pay"] <= time.time():sd = 'Süre Doldu'
                                        else:sd = humanize.naturaltime(datetime.fromtimestamp(wait['name'][wait['info'][a]]["pay"]))
                                        if no == len(h):msgas+='\n{}. @!\n❧ {}'.format(no,sd)
                                        else:msgas += '\n{}. @!\n❧️ {}'.format(no,sd)
                                    mentions(to, msgas, h[aa*20:(aa+1)*20])

                    elif cmd.startswith('üyesil ') and msg._from in myAdmin:
                        h = [a for a in wait['info']]
                        mid = h[int(text.lower().split(' ')[1])-1]
                        user = wait["info"][mid]
                        if mid in wait['info'] and mid not in wait['name']:
                            del wait['info'][mid]
                            zarifoglu.sendMention(to, ' Service Delete @!in service ','', [mid])
                        if mid in wait['name']:
                            del wait['name'][mid]
                            del wait['info'][mid]
                            os.system("screen -S {} -X kill".format(user))
                            os.system('rm -rf {}'.format(user))
                        zarifoglu.sendMention(to, "User @!has been deleted.","",[mid])

                    elif cmd == "çıkış" or cmd =="logout":
                              if sender in wait['info']:
                                us = wait["info"][sender]
                                contact = zarifoglu.getContact(sender)
                                os.system('screen -S {} -X quit'.format(us))
                                os.system('rm -rf {}'.format(us))
                                if msg.toType == 2:
                                    mentions(to, "「 Logout Service 」\n@!,⌬ Durum : Çıkış başarılı", [sender])
                                else:
                                    mentions(to, "「 Logout Service 」\n⌬ Durum : Çıkış başarılı! ", [sender])
                              else:
                                mentions(to, ' 「 Logout Service 」\nMerhaba @!\nKayıtlı değilsin lütfen önce ödeme yap @! ', [sender, "ubdd032b9061d760477ce7cc6a12110d7"])
#==============================================================================================

                    elif cmd.startswith("addservice ") and msg._from in myAdmin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 not in premium['myService']:
                                    nama = str(text.split(' ')[1])
                                    premium['myService'][key1] =  '%s' % nama
                                    zarifoglu.sendMention(msg.to, '⌬ Added @! to service','', [key1])
                                else:
                                    zarifoglu.sendMention(msg.to, '⌬ User @! already in service','', [key1])
                    elif cmd.startswith("delservice ") and msg._from in myAdmin:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                key = eval(msg.contentMetadata["MENTION"])
                                key1 = key["MENTIONEES"][0]["M"]
                                if key1 in premium['myService']:
                                    del premium['myService'][key1]
                                    zarifoglu.sendMention(msg.to, '⌬ Deleted @! from service','', [key1])
                                else:
                                    zarifoglu.sendMention(msg.to, '⌬ User @! not in service','', [key1])
                    elif cmd == "üye listesi" and msg._from in myAdmin and to not in chatbot["botMute"]:
                        h = [a for a in premium['myService']]
                        k = len(h)//20
                        for aa in range(k+1):
                            if aa == 0:msgas = '「 List Service 」\n';no = aa
                            else:msgas = '「 List Service 」\n';no = aa * 20
                            for a in h[aa * 20 : (aa + 1) * 20]:
                                no+=1
                                if premium['myService'][a] == "":cd = "None."
                                else:cd = premium['myService'][a]
                                if no == len(h):msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                                else:msgas+='\n{}. @!\nFile : {}'.format(no,cd)
                            zarifoglu.sendMention(msg.to, msgas,'', h[aa * 20 : (aa+1)*20])
                    elif cmd == "restart":
                        if msg._from in premium["myService"]:
                            user = premium["myService"][msg._from]
                            os.system("screen -S {} -X quit".format(str(user)))
                            os.system('screen -dmS {}'.format(user))
                            os.system('screen -r {} -X stuff "cd {} && python3 theneon.py \n"'.format(user, user))
                            time.sleep(3)
                            zarifoglu.sendMention(msg.to, '「  Restart Sb  」\n> @! Succes Restart selfbot',' ', [msg._from])
#==========================================
#==========================================
                    elif cmd.startswith("name "):
                        if msg._from in myAdmin:
                            string = removeCmd("name", text)
                            if len(string) <= 10000000000:
                                pname = zarifoglu.getContact(sender).displayName
                                profile = zarifoglu.getProfile()
                                profile.displayName = string
                                zarifoglu.updateProfile(profile)
                                zarifoglu.sendMessage(to, "「 Update Name 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif cmd.startswith("status "):
                        if msg._from in myAdmin:
                            string = removeCmd("status", text)
                            if len(string) <= 10000000000:
                                pname = zarifoglu.getContact(sender).statusMessage
                                profile = zarifoglu.getProfile()
                                profile.statusMessage = string
                                zarifoglu.updateProfile(profile)
                                zarifoglu.sendMessage(to, "「 Update Status 」\nStatus : Success\nFrom : "+str(pname)+"\nTo :"+str(string))
                    elif text.lower() == "req login":
                        contact = zarifoglu.getContact(sender)
                        owner = "u5d854616fc8ea66893e7a85b7cb0b9f1"
                        zarifoglu.sendContact(owner, "" + str(sender))
                        neon = "Request Login :\nFrom @!"
                        mid = zarifoglu.getContact(sender)
                        mentions(owner, neon, [sender])
                        zarifoglu.sendMessage(owner, "" + str(sender))
                        zarifoglu.sendMention(to, "Hi @!\nThe request to enter the selfbots has been sent , please wait for the owner to accept your request","",[msg._from])
                    elif cmd.startswith("chatmaker "):
                        sep = text.split(" ")
                        txt = text.replace(sep[0] + " ","")
                        contact = zarifoglu.getContact(sender)
                        owner = "u5d854616fc8ea66893e7a85b7cb0b9f1"
                        neon = "Sender: @!"
                        neon += "\nMessage: {}".format(txt)
                        mentions(owner, neon, [sender])
                        zarifoglu.sendMessage(owner, "" + str(sender))
                        zarifoglu.sendMention(to, "Hi @!\nmessage has been send","",[msg._from])
#==========================================
                    elif cmd == "ping":
                        if msg._from in myAdmin:
                            zarifoglu.sendMention(to, "PONG ! @!","",[msg._from])
                    elif cmd == "reboot":
                        if msg._from in myAdmin:
                            zarifoglu.sendMention(to, "@! Helper , Yeniden Başlatılıyor",' ', [msg._from])
                            restartBot()
                        else:pass
#==========================================
                    elif cmd == "join on":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == True:
                                msgs=" 「 Join 」\nJoin already Enable♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to Enable♪"
                                settings["autoJoin"] = True
                            zarifoglu.sendMessage(to, msgs)
                    elif cmd == "join off":
                        if msg._from in myAdmin:
                            if settings["autoJoin"] == False:
                                msgs=" 「 Join 」\nJoin already DISABLED♪"
                            else:
                                msgs=" 「 Join 」\nJoin set to DISABLED♪"
                                settings["autoJoin"] = False
                            zarifoglu.sendMessage(to, msgs)
                    elif cmd.startswith("$"):
                        if msg._from in myAdmin:
                            kntl = removeCmd("$", text)
                            ikkeh = os.popen("{}".format(str(kntl)))
                            enaena = ikkeh.read()
                            zarifoglu.sendMessage(to, "{}".format(str(enaena)))
                            ikkeh.close()
                    elif cmd == "screenlist":
                        if msg._from in myAdmin:
                            proses = os.popen("screen -list")
                            a = proses.read()
                            zarifoglu.sendMessage(to, "{}".format(str(a)))
                            proses.close()
                    elif cmd.startswith("post"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            gs = zarifoglu.getGroup(msg.to)
                            jmlh = int(shar[1])
                            zarifoglu.sendMessage(to, "Waiting for share.")
                            if jmlh <= 1000:
                                for baba in range(jmlh):
                                    try:
                                        zarifoglu.sendPostToTalk(to, str(shar[2]))
                                    except:
                                        pass
                                zarifoglu.sendMessage(to, "Sucess")
                            else:
                                zarifoglu.sendMessage(to, "Amount is wrong")
                    elif cmd.startswith("postall"):
                        if msg._from in myAdmin:
                            shar = text.split("-")
                            shareall(to, shar[1])
#==========================================
#==========================================
                    elif cmd == "mentions":
                        group = zarifoglu.getGroup(to);nama = [contact.mid for contact in group.members];nama.remove(zarifoglu.getProfile().mid)
                        zarifoglu.datamention(to,'Mentions',nama)
#==========================================
#==========================================
                    elif cmd.startswith("cvp"):
                        if msg._from in myAdmin:
                            link = removeCmd("cvp", text)
                            contact = zarifoglu.getContact(sender)
                            zarifoglu.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Download...")
                            print("Sedang Mendownload Data ~")
                            pic = "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            subprocess.getoutput('youtube-dl --format mp4 --output TeamAnuBot.mp4 {}'.format(link))
                            pict = zarifoglu.downloadFileURL(pic)
                            vids = "TeamAnuBot.mp4"
                            time.sleep(2)
                            changeVideoAndPictureProfile(pict, vids)
                            zarifoglu.sendMessage(to, "Type: Profile\n • Detail: Change video url\n • Status: Succes")
                            os.remove("TeamAnuBot.mp4")                            
#==========================================
#==========================================
                    elif cmd == "debug":
                       if msg._from in myAdmin:
                            zarifoglu.sendMessage(to, debug())
                    elif cmd == "speed":
                        start = time.time()
                        zarifoglu.sendMessage("u5d854616fc8ea66893e7a85b7cb0b9f1", '< ... >')
                        elapsed_time = time.time() - start
                        zarifoglu.sendMessage(to,"Time:\n%s"%str(round(elapsed_time,5)))
#==========================================
#==========================================
                    elif cmd == "glist":
                       if msg._from in myAdmin:
                            key = settings["keyCommand"].title()
                            if settings['setKey'] == False:key = ''
                            gid = zarifoglu.getGroupIdsJoined()
                            sd = zarifoglu.getGroups(gid)
                            ret = "「 Group List 」\n"
                            no = 0
                            total = len(gid)
                            cd = "\n\nTotal {} Groups\n\n「 Command 」\n\n> Remote Mention\nUsage: #Glist [num] tag [1|<|>|-]\n\n> Remote Kick\nUsage: #glist [num] kick [1|<|>|-]\n\n> Leave Groups\nUsage: #Leave [num]\n\n> Get QR\nUsage: #Openqr  [num]\n\n> Cek Member\nUsage: #Glist [num]\nUsage: #Glist [num] mem [num]".format(total)
                            for G in sd:
                                member = len(G.members)
                                no += 1
                                ret += "\n{}. {} | {}".format(no, G.name[0:20], member)
                            ret += cd
                            k = len(ret)//10000
                            for aa in range(k+1):
                                zarifoglu.generateReplyMessage(msg.id)
                                zarifoglu.sendReplyMessage(msg.id, to,'{}'.format(ret[aa*10000 : (aa+1)*10000]))
                    elif cmd.startswith('glist'):
                        if msg._from in myAdmin:
                            to = msg.to
                            gid = zarifoglu.getGroupIdsJoined()
                            group = zarifoglu.getGroup(gid[int(cmd.split(' ')[1])-1])
                            nama = [a.mid for a in group.members]
                            if len(cmd.split(" ")) == 2:
                                total = "Local ID: {}".format(int(cmd.split(' ')[1]))
                                zarifoglu.datamention(to,'List Member',nama,'\n├Group: '+group.name[:20]+'\n├'+total)
                            if len(cmd.split(" ")) == 4:
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' mem '):zarifoglu.getinformation(to,nama[int(cmd.split(' ')[3])-1],wait)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' tag'):zarifoglu.adityaarchi(wait,'Mention','tag',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                                if cmd.startswith('glist '+cmd.split(' ')[1]+' kick'):zarifoglu.adityaarchi(wait,'Kick Member','kick',gid[int(cmd.split(' ')[1])-1],cmd.split(' ')[3],msg,"\n├Group: {}\n├Local ID: {}".format(group.name[:20],int(cmd.split(' ')[1])),nama=nama)
                    if cmd.startswith("leave groups "):
                        if msg.toType in [0,1,2]:
                            gid = zarifoglu.getGroupIdsJoined()
                            if len(cmd.split(" ")) == 3:
                                selection = MySplit(cmd.split(' ')[2],range(1,len(gid)+1))
                                k = len(gid)//100
                                for a in range(k+1):
                                    if a == 0:eto='╭「 Leave Group 」─'
                                    else:eto='├「 Leave Group 」─'
                                    text = ''
                                    no = 0
                                    for i in selection.parse()[a*100 : (a+1)*100]:
                                        zarifoglu.leaveGroup(gid[i - 1])
                                        no+=1
                                        if no == len(selection.parse()):text+= "\n╰{}. {}".format(i,zarifoglu.getGroup(gid[i - 1]).name)
                                        else:text+= "\n│{}. {}".format(i,zarifoglu.getGroup(gid[i - 1]).name)
                                    zarifoglu.sendMessage(to,eto+text)
                    elif cmd.startswith("gcast "):
                      if msg._from in myAdmin:
                            txt = removeCmd("gcast", text)
                            groups = zarifoglu.getGroupIdsJoined()
                            for group in groups:
                                sendFooter(group, "「 Group Broadcast 」\n{}".format(str(txt)))
                                time.sleep(1)
                            zarifoglu.sendMessage(to, "Succes broadcast to {} group".format(str(len(groups))))
                    elif cmd.startswith('joinme '):
                         if msg._from in myAdmin:
                             text = msg.text.split()
                             number = text[1]
                             if number.isdigit():
                              groups = zarifoglu.getGroupIdsJoined()
                              if int(number) < len(groups) and int(number) >= 0:
                                  groupid = groups[int(number)]
                                  group = zarifoglu.getGroup(groupid)
                                  target = sender
                                  try:
                                      zarifoglu.getGroup(groupid)
                                      zarifoglu.findAndAddContactsByMid(target)
                                      zarifoglu.inviteIntoGroup(groupid, [target])
                                      zarifoglu.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                  except:
                                      zarifoglu.sendMessage(msg.to,"I no there baby")

                    elif cmd.startswith('invme '):
                         if msg._from in myAdmin:
                             cond = cmd.split(" ")
                             num = int(cond[1])
                             gid = zarifoglu.getGroupIdsJoined()
                             group = zarifoglu.getCompactGroup(gid[num-1])
                             zarifoglu.findAndAddContactsByMid(sender)
                             zarifoglu.inviteIntoGroup(gid[num-1],[sender])

                    elif cmd.startswith("openqr "):
                      if msg._from in myAdmin:
                            number = removeCmd("/openqr", text)
                            groups = zarifoglu.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = zarifoglu.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    zarifoglu.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(zarifoglu.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    zarifoglu.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(zarifoglu.reissueGroupTicket(G.id)))
                                zarifoglu.sendMessage(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                zarifoglu.sendMessage(to, str(error))
                    elif cmd == "/byeall":
                        if msg._from in myAdmin:
                            anu = zarifoglu.getGroupIdsJoined()
                            for i in anu:
                                try:
                                    zarifoglu.leaveGroup(i)
                                except Exception as e:
                                    zarifoglu.sendMessage(msg.to, e)
                        else:zarifoglu.sendMention(msg.to, "Wtf @!Siktir!!!","Hahahahha",' ', [msg._from])

                    elif cmd == "helper3":
                            helpalay(to)

                    elif cmd == "helper4":
                            helpss(to)

                    elif cmd == "helper5":
                            likeNotify(to)

                    elif cmd == "helper2":
                        if msg._from in myAdmin:
                            helppss(to)

                    if text.lower() == "rname":
                        if msg._from in myAdmin:
                            key = settings["keyCommand"]
                            if settings["setKey"] == True:
                                statuskey = "Enabled"
                            else:
                                statuskey = "Disabled"
                            zarifoglu.sendMessage(to, "⌬ Rname : "+str(key.title())+"\n⌬ Status : "+str(statuskey))
                    if text.lower() == "rname on":
                        if msg._from in myAdmin:
                            settings["setKey"] = True
                            zarifoglu.sendMessage(to, "Rname has been enabled")
                    if text.lower() == "rname off":
                        if msg._from in myAdmin:
                            settings["setKey"] = False
                            zarifoglu.sendMessage(to, "Rname has been disabled")
#==========================================
        if op.type == 55:
            if op.param1 in tailah["siderTemp"] and op.param2 not in tailah["siderTemp"][op.param1]:
                tailah["siderTemp"][op.param1].append(op.param2)
                if "@!" in settings["readerPesan"]:
                    contact = zarifoglu.getContact(op.param2)
                    pesan = tailah["siderPesan"]
                    data={"type":"flex","altText":"Turkey Team™","contents":{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
                    "type": "box",
                    "layout": "horizontal",
                    "contents": [
                      {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                          {
                            "type": "image",
                            "url": "https://obs.line-scdn.net/{}".format(contact.pictureStatus)
                          }
                        ],
                        "width": "60px",
                        "height": "60px",
                        "borderWidth": "2px",
                        "borderColor": "#ffffff",
                        "cornerRadius": "100px"
                      },
                      {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                          {
                            "type": "text",
                            "text": "Hello , {}".format(contact.displayName),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True
                          },
                          {
                            "type": "text",
                            "text": "{}".format(pesan),
                            "weight": "bold",
                            "size": "md",
                            "color": "#ffffff",
                            "wrap": True,
                          }
                        ],
                        "margin": "lg"
                      }
                    ]
                  }
        ],
        "paddingAll": "13px",
        "backgroundColor": "#000000",
        "cornerRadius": "2px",
        "margin": "xl"
      }
    ],
    "paddingAll": "0px"
  }
}}
                    sendTemplate(op.param1,data)
                
            if op.param1 in read["readPoint"]:
                _name = zarifoglu.getContact(op.param2).displayName
                tz = pytz.timezone("Asia/Jakarta")
                timeNow = datetime.now(tz=tz)
                timeHours = datetime.strftime(timeNow," (%H:%M)")
                read["readMember"][op.param1][op.param2] = str(_name) + str(timeHours)
#==========================================
        if op.type == 55:
            #print("[ 55 ] NOTIFIED READ MESSAGE")
            try:
                if op.param1 in wait['readPoint']:
                    if op.param2 in wait['ROM1'][op.param1]:
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                    else:
                        wait['ROM1'][op.param1][op.param2] = op.param2
                        wait['setTime'][op.param1][op.param2] = op.createdTime
                        try:
                            if wait['lurkauto'] == True:
                                if len(wait['setTime'][op.param1]) % 5 == 0:
                                    anulurk(op.param1,wait)
                        except:pass
                elif op.param2 in wait['readPoints']:
                    wait['lurkt'][op.param1][op.param2][op.param3] = op.createdTime
                    wait['lurkp'][op.param1][op.param2][op.param3] = op.param2
                else:pass
            except:
                pass
        backupData()
    except Exception as error:
        logError(error)
        traceback.print_tb(error.__traceback__)
    
def run():
    while True:
        try:
            ops = zarifogluPoll.singleTrace(count=50)
            if ops != None:
                for op in ops:
                   loop.run_until_complete(zarifogluBot(op))
                   zarifogluPoll.setRevision(op.revision)
        except Exception as e:
            logError(e)
            
if __name__ == "__main__":
    run()
	##ㄒㄩ尺Ҝ乇ㄚ ㄒ乇卂爪
	## ＴＵＲＫＥＹ ＴＥＡＭ