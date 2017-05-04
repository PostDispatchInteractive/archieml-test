import archieml_pd as archieml
from collections import OrderedDict as OrderedDict


data = archieml.load('data/copy.txt')

with open('data/copy.txt') as f:
	data = archieml.load(f)

print data.content.project_name


d = OrderedDict(
    [
        (u'headline', u'Bait and Switch, a Common Ploy of Patriots and Seahawks' ),
        (u'leadin', u'The Patriots and the Seahawks share a knack for the trick play, making it look like something tht the defense recognizes. But when the defense reacts, these teams turn the play into something entirely different.'),
        (u'sections', 
            [
                OrderedDict(
                    [
                        (u'kicker',u'New England Patriots'),
                        (u'hed',u'Patriots vs. Ravens, Jan. 10'),
                        (u'intro',u'REceiver Julian Edelman is dangerous any time he touches the ball, and the Patriots find creative ways to use him. Here, the Patriots throw whatlooks like a wide-receiverscreen to Edelman. But looks can be deceiving -- just ask the Ravens.'),
                        (u'video',u'http://int.nyt.com/data/videotape/finished/2015/01/1422654167/Patriots_v6-{{size}}.{{format}}'),
                        (u'image', u'c-pats')
                    ]
                ),
                OrderedDict(
                    [
                        (u'kicker', u'Seattle Seahawks'),
                        (u'hed', u'Seahawks vs. Eagles, Dec. 7'),
                        (u'intro', u"The Seahawks' one-two punch of quarterback Russell Wilson and running back Marshawn Lynch can give defenses fits. Wilson is as dangerous with his legs as with his arm, which can cause defenses to overreact to his every move."),
                        (u'video',u'http://int.nyt.com/data/videotape/finished/2015/01/1422659383/seahawks_v1_4-{{size}}.{{format}}'),
                        (u'image', u'c-seahawks')
                    ]
                )
            ]
        ),

        (u'content', 
            OrderedDict(
                [
                    (u'project_name', u'ArchieML test'),
                    (u'project_url', u'http://localhost:8000/'),
                    (u'cdn_url', u'http://localhost:8000/'),
                    (u'headline',u'This is a test of connecting ArchieML to the NPR app-template'),
                    (u'Description',u'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus vel nibh non libero porta sodales a quis lectus. Donec consequat auctor mollis.'),
                    (u'election_date', u'May 4, 2017'),
                ]
            )
        ),

        (u'share',
            OrderedDict(
                [
                    (u'meta_description', u'Cool stuff for St. Louis city, St. Louis County, St. Charles County, Jefferson County, Franklin County, Lincoln County, and Warren County.'),
                    (u'meta_keywords',u'St. Louis, STL, Saint Louis, St Louis, Missouri, MO, St. Louis Post-Dispatch, stltoday, www.stltoday.com'),
                    (u'share_url', u'http://graphics.stltoday.com/apps/elections/'),
                    (u'twitter_handle', u'@stltoday'),
                    (u'twitter_text',u'Cool stuff for St. Louis city, St. Louis County, St. Charles County, Jefferson County, Franklin County, Lincoln County, and Warren County.'),
                    (u'twitter_image_url',u'http://graphics.stltoday.com/apps/elections/img/elections-preview.jpg'),
                    (u'twitter_title', u'ArchieML test'),
                    (u'facebook_title', u'ArchieML test'),
                    (u'facebook_url', u'http://graphics.stltoday.com/apps/elections/'),
                    (u'facebook_text', u'Cool stuff for St. Louis city, St. Louis County, St. Charles County, Jefferson County, Franklin County, Lincoln County, and Warren County.'),
                    (u'facebook_image_url', u'http://graphics.stltoday.com/apps/elections/img/elections-preview.jpg'),
                    (u'facebook_site_name', u'STLtoday.com'),
                    (u'facebook_article_publisher', u'https://www.facebook.com/STLPD'),
                    (u'facebook_app_id', u'205112096200104'),

                ]
            )
        )
    ]
)

