import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventsGow.settings')
django.setup()

from datetime import date, datetime
from accounts.models import CustomUser
from events.models import Tags, Events


tag_list = [
# type    
"food", "sports", "music", "film", "trekking", "whisky", "party",
# type
"entertainment", "academic", "sport", "art", "society", 
"private", "public", "ticket", "free", "outdoors", "indoors",
# scale
"<10 people", "10-50 people", "50-100 people", ">100 people",
# entertainment
"banquet", "concert", "party", "international " ,
"dinner", "launch", "breakfasr", "team", "tennis", 
# country
'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua & Deps', 'Argentina', 'Armenia', 
'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 
'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 
'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 
'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Congo', 'Costa Rica', 'Croatia', 'Cuba', 
'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 
'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 
'Finland', 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 
'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 
'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jordan', 
'Kazakhstan', 'Kenya', 'Kiribati', 'Korea North', 'Korea South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 
'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 
'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 
'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 
'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 
'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman', 'Pakistan', 'Palau', 
'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 
'Romania', 'Russian Federation', 'Rwanda', 'St Kitts & Nevis', 'St Lucia', 'Saint Vincent & the Grenadines', 
'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 
'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 
'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 
'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 
'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 
'Uruguay', 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe',
# sport
'archer', 'arena', 'arrow','athlete', 'axel', 'badminton', 'ball', 
'base', 'bat', 'batter', 'bicycle', 'bike', 'bocce', 'bow', 'box', 'canoe', 'catch', 'cleats', 'club', 'coach', 
'compete', 'crew', 'cricket', 'cycle', 'cyclist', 'dart', 'defense', 'diamond', 'dive', 'diver', 'exercise', 
'fencing', 'field', 'fitness', 'frisbee', 'game', 'gear', 'goal', 'goalie', 'golf', 'golfer', 'guard', 'gym', 
'gymnast', 'helmet', 'hockey', 'home', 'hoop', 'hoops', 'ice', 'infield', 'inning', 'javelin', 'jog', 'judo', 
'jump', 'jumper', 'karate', 'kayak', 'kite', 'lacrosse', 'league', 'lose', 'loser', 'luge', 'major', 'mallet', 
'mat', 'medal', 'mitt', 'move', 'net', 'offense', 'olympics', 'out', 'paddle', 'pitch', 'play', 'player', 'pole', 
'polo', 'pool', 'puck', 'quarter', 'quiver', 'race', 'racer', 'referee', 'relay', 'ride', 'rink', 'row', 'rower', 
'sail', 'score', 'scuba', 'skate', 'ski', 'skier', 'slalom', 'sled', 'sledder', 'snowboard', 'soccer', 'sport', 
'squash', 'stadium', 'stick', 'surfer', 'swim', 'swimmer', 'tag', 'target', 'team', 'tee', 'tennis', 'throw', 
'tie', 'triathlon', 'umpire', 'vault', 'volley', 'walk', 'weight', 'win', 'winner', 'winning', 'wrestler',
# academic
'Life Science','Business','Chemistry','Computing Science','Critical Studies','Culture & Creative Arts','Education',
'Engineering','Geographical & Earth Sciences', 'Interdisciplinary Studies','Law','Mathematics & Statistics',' Medicine',
'Dentistry','Nursing','Modern Languages','Physics & Astronomy','Psychology & Neuroscience','Social & Political Sciences',
'Veterinary Medicine',
]



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
                'image': '/images/riverside.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"),
                'url': "https://www.designmynight.com/glasgow/clubs/west-end/riverside-museum/riverside-festival-1", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                                                                                               ]},

               {'title': "TRNSMT Festival", 'venue': "Glasgow Green", 'description': "cinch presents TRNSMT Festival | 10th - 12th Septmeber 2021 | Glasgow Green. Keep up to date with all things TRNSMT, visit our website and subscribe to our mailing list.",
                'image': '/images/trnsmt.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"),
                'url': "https://trnsmtfest.com/", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]
                                                                            ]},

               {'title': "Coldplay - Music of the Spheres World Tour", 'venue': "Hampden Park", 'description': "The Music Of The Spheres World Tour begins on 18 March 2022 with the band’s first ever show in Costa Rica, before travelling to the Dominican Republic, Mexico, USA, Germany, Poland, France, Belgium and the UK.",
                'image': '/images/coldplay.jpg', 'date': date.today(), 'time': datetime.now().strftime("%H:%M"), 'url': "https://www.coldplay.com/homepage/", 'tags': [Tags.objects.filter(tag_name="concert")[0], Tags.objects.filter(tag_name="outdoors")[0], Tags.objects.filter(tag_name="music")[0]]
                }]

for item in events_list:
    events = Events(title = item['title'], venue = item['venue'], description = item['description'], image = item['image'], date = item['date'], time = item['time'], creator = user, url = item['url'])
    events.save()

    for i in item['tags']:
        events.tags.add(Tags.objects.get(tag_name='outdoors'))