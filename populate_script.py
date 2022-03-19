import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventsGow.settings')
django.setup()
from datetime import date, datetime
from accounts.models import CustomUser
from events.models import Tags, Events
# Creating a list of tags to populate them in our events form
tag_list = ["food", "outdoors", "indoors", "sports", "music", "film",
            "trekking", "whisky", "party", "adventure", "concert", "festival"]
# Saving the tag list
for i in tag_list:
    if len(Tags.objects.filter(tag_name=i)) == 0:
        tag = Tags(tag_name=i)
        tag.save()
# Creating an event list to populate some events when the application is run
user, created = CustomUser.objects.get_or_create(id=3)
events_list = [{'title': "Riverside Festival", 'venue': "Riverside Museum", 'description': "Riverside Festival is the music event in Glasgow you don't want to miss out on. Taking place at its usual beaut location, the Riverside Museum, this goings-on is set to be a heaving paradise for lovers of house, techno and the like.",
                'image': './static/images/riverside.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"),
                'url': "https://www.designmynight.com/glasgow/clubs/west-end/riverside-museum/riverside-festival-1", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                                                                                               ]},
               {'title': "TRNSMT Festival", 'venue': "Glasgow Green", 'description': "cinch presents TRNSMT Festival | 10th - 12th Septmeber 2021 | Glasgow Green. Keep up to date with all things TRNSMT, visit our website and subscribe to our mailing list.",
                'image': './static/images/trnsmt.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"),
                'url': "https://trnsmtfest.com/", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                            ]},
               {'title': "Coldplay - Music of the Spheres World Tour", 'venue': "Hampden Park", 'description': "The Music Of The Spheres World Tour begins on 18 March 2022 with the band’s first ever show in Costa Rica, before travelling to the Dominican Republic, Mexico, USA, Germany, Poland, France, Belgium and the UK.",
                'image': './static/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://www.coldplay.com/homepage/", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                            ]},
                {'title': "Chinese Festival", 'venue': "University Leaning Hub", 'description': "The Chinese Festival celebration starts at 8:00AM to 15:00PM. Visit our website and join us!",
                'image': './static/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://zh.wikipedia.org/wiki/%E6%98%A5%E7%AF%80", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                            ]},
                {'title': "2 Pints Of Tennents And A Packet Of Chris", 'venue': "Byres Road", 'description': "Join Chris Scott, Katie Tennent and Sam Tennent at The Admiral Bar on 19th March for '2 Pints Of Tennents And A Packet Of Chris' as part of Glasgow Comedy Festival 2022!!",
                'image': './static/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://www.whatsonglasgow.co.uk/event/100889-2-pints-of-tennents-and-a-packet-of-chris/", 'tags': [Tags.objects.filter(tag_name="food")[0], Tags.objects.filter(tag_name="whisky")[0], Tags.objects.filter(tag_name="music")[0]
                                                                            ]},
                {'title': "Amber Mark", 'venue': "Glasgow Central", 'description': "New York-based producer and sultry, soul-drenched vocalist Amber Mark is taking her new record Three Dimensions Deep out on tour, catch her live at The Garage on 19th March!",
                'image': './static/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://www.whatsonglasgow.co.uk/event/097431-amber-mark/", 'tags': [Tags.objects.filter(tag_name="food")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="party")[0]
                                                                            ]},
                {'title': "Brock Burn Festival", 'venue': "Glasgow South Side", 'description': "The first Brock Burn Festival, a free family fun nature day, is being held on Brockburn Path, Priesthill on Saturday 19th March!",
                'image': './static/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://www.whatsonglasgow.co.uk/event/097431-amber-mark/", 'tags': [Tags.objects.filter(tag_name="food")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="party")[0]
                                                                            ]},
                                                                            
                                                                            ]
                
                                                                            
for item in events_list:
    events = Events(title = item['title'], venue = item['venue'], description = item['description'], image = item['image'], date = item['date'], time = item['time'], creator = user, url = item['url'])
    events.tags.set(Tags.objects.all()[0])
    events.save()


# Start excution here!s
# if __name__ == '__main__':
#     print('Starting EventsGow population script...')
#     populate()