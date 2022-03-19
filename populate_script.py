import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventsGow.settings')
django.setup()

from events.models import Tags

tag_list = ["food", "outdoors", "indoors", "sports", "music", "film", "trekking", "whisky", "party"]

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