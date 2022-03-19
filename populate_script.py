import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventsGow.settings')
django.setup()

from events.models import Tags


tag_list = [
# type    
"food", "outdoors", "indoors", "sports", "music", "film", "trekking", "whisky", "party",
# type
"entertainment", "academic", "sport", "art", "society", 
"private", "public", "ticket", "free", 
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
'tie', 'triathlon', 'umpire', 'vault', 'volley', 'walk', 'weight', 'win', 'winner', 'winning', 'wrestler'
# academic

]


for i in tag_list:
    tag = Tags(tag_name = i)
    tag.save()

# tag = Tags(tag_name="outdoors")
# tag = Tags(tag_name="indoors")
# tag = Tags(tag_name="sports")
# tag = Tags(tag_name="trekking")
# tag = Tags(tag_name="food")
# tag = Tags(tag_name="music")
# tag = Tags(tag_name="film")

# Start excution here!
# if __name__ == '__main__':
#     print('Starting EventsGow population script...')
#     populate()