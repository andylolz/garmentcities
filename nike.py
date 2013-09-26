import urllib
import urllib2
import json

# TODO: Some cities have multiple factories. Combine these first
# TODO: Fix matching between city / country naming

nike_data_url = 'http://manufacturingmap.nikeinc.com/maps/export_json'
un_data_base_url = 'https://api.scraperwiki.com/api/1.0/datastore/sqlite'
un_data_querystr = {
    'format': 'jsondict',
    'name': 'city_population_by_sex_city_and_city_type_un_data',
}

# fetch Nike data
nike_data = json.loads(urllib2.urlopen(nike_data_url).read())

# UN data base query
un_data_query = "SELECT * FROM `swdata` WHERE LOWER(`Country or Area`) = '%s' AND LOWER(`City`) LIKE '%%%s%%' AND `Sex` = 'Both Sexes'"

current_data = None
for x in nike_data:
    # populate current query
    un_data_querystr['query'] = un_data_query % (x['country'].lower().encode('utf8'), x['city'].lower().encode('utf8'))
    # generate current url
    current_url = '%s?%s' % (un_data_base_url, urllib.urlencode(un_data_querystr))
    # run it!
    current_data = json.loads(urllib2.urlopen(current_url).read())
    if current_data:
        city_pop = float(current_data[0]['Value'].replace(',', ''))
        city_workers_pct = 100. * float(x['workers']) / city_pop
        print 'At least %f%% of the population of %s, %s are employed by Nike' % (city_workers_pct, x['city'], x['country'])
        pass
    else:
        print 'No data for %s, %s' % (x['city'], x['country'])
