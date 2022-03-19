import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EventsGow.settings')
django.setup()

from events.models import Tags

tag_list = ["food", "outdoors", "indoors", "sports", "music", "film", "trekking", "whisky", "party", "adventure"]

for i in tag_list:
    tag = Tags(tag_name = i)
    tag.save()

# Start excution here!
# if __name__ == '__main__':
#     print('Starting EventsGow population script...')
#     populate()