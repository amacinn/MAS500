#Andrew MacInnes

import mediacloud, datetime, logging, unittest

logging.basicConfig(filename="logger.log", filemode = 'w', level=logging.INFO)

def activateNow():

	mc = mediacloud.api.MediaCloud('API goes here')
	logging.info('Successful implementation.')
	#Find the annual number of sentences in US mainstream media containing Facebook between the years 2000 and 2015.
	res2000 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(1999,12,31), datetime.date(2000,12,31) ), 		'media_sets_id:1' ])
	res2001 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2000,12,31), datetime.date(2001,12,31) ), 'media_sets_id:1' ])
	res2002 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2001,12,31), datetime.date(2002,12,31) ), 'media_sets_id:1' ])
	res2003 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2002,12,31), datetime.date(2003,12,31) ), 'media_sets_id:1' ])
	res2004 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2003,12,31), datetime.date(2004,12,31) ), 'media_sets_id:1' ])
	res2005 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2004,12,31), datetime.date(2005,12,31) ), 'media_sets_id:1' ])
	res2006 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2005,12,31), datetime.date(2006,12,31) ), 'media_sets_id:1' ])
	res2007 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2006,12,31), datetime.date(2007,12,31) ), 'media_sets_id:1' ])
	res2008 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2007,12,31), datetime.date(2008,12,31) ), 'media_sets_id:1' ])
	res2009 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2008,12,31), datetime.date(2009,12,31) ), 'media_sets_id:1' ])
	res2010 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2009,12,31), datetime.date(2010,12,31) ), 'media_sets_id:1' ])
	res2011 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2010,12,31), datetime.date(2011,12,31) ), 'media_sets_id:1' ])
	res2012 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2011,12,31), datetime.date(2012,12,31) ), 'media_sets_id:1' ])
	res2013 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2012,12,31), datetime.date(2013,12,31) ), 'media_sets_id:1' ])
	res2014 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2013,12,31), datetime.date(2014,12,31) ), 'media_sets_id:1' ])
	res2015 = mc.sentenceCount('(Facebook)', solr_filter=[mc.publish_date_query( datetime.date(2014,12,31), datetime.date(2015,11,18) ), 'media_sets_id:1' ])
	return(res2000, res2001, res2002, res2003, res2004, res2005, res2006, res2007, res2008, res2009, res2010, res2011, res2012, res2013, res2014, res2015)

res2000, res2001, res2002, res2003, res2004, res2005, res2006, res2007, res2008, res2009, res2010, res2011, res2012, res2013, res2014, res2015 = activateNow()

print "2000 %s " % res2000['count']
print "2001 %s " % res2001['count']
print "2002 %s " % res2002['count']
print "2003 %s " % res2003['count']
print "2004 %s " % res2004['count']
print "2005 %s " % res2005['count']
print "2006 %s " % res2006['count']
print "2007 %s " % res2007['count']
print "2008 %s " % res2008['count']
print "2009 %s " % res2009['count']
print "2010 %s " % res2010['count']
print "2011 %s " % res2011['count']
print "2012 %s " % res2012['count']
print "2013 %s " % res2013['count']
print "2014 %s " % res2014['count']
print "2015 %s " % res2015['count']


