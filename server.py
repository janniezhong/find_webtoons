from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

current_id = 11
data = {"1": {
            "id": "1",
            "title": "Gourmet Hound",
            "image":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1515943982i/37933386._UY809_SS809_.jpg",
            "summary": "Lucy, a woman with an uncanny sense of taste and smell, discovers that her favorite restaurant has changed kitchen staff. Worst of all, she does not know the identity of the chef whose cooking she's loved for years! When a lucky accident leads her to two former chefs at Dimanche, she decides that she will do her utmost to track down each of their old colleagues in order to rediscover that ‘perfect taste’. It won’t be easy — all the chefs at Dimanche seem to have scattered far and wide, almost like they’re all avoiding each other. Will Lucy be able to find her chef?",
            "author": "Leehama",
	        "rating": "9.82",
            "reviews": ["The art of Gourmet Hound is absolutely adorable. It has a bright and refreshing colour scheme and the character designs are very unique and diverse. The foods featured are always drawn so beautifully that one would get hungry from just looking at it.", "hello my name is Sana and this webcomic Exists and warms every part of my soul and body.", "I LOVE AND ADORE GOURMET HOUND WITH MY WHOLE HEART! For real, this is my favourite webcomic and you should all read it. NOW.", "this might be my most favorite webcomic of all time!!!", "omg this was TOO cute"],
	        "complete": "true",
            "ep1":"https://www.webtoons.com/en/drama/gourmet-hound/ep-1-chopped-onions/viewer?title_no=1245&episode_no=1",
            "art_img":["https://cdn.anime-planet.com/characters/primary/lucy-fuji-1.jpg?t=1625890978", "http://pm1.narvii.com/7163/a67693d613d0c42d2bee8d8770c91060b62659c5r1-255-381v2_00.jpg","https://64.media.tumblr.com/41181c74eb569bca956923a734c48671/856474ead789de05-7d/s640x960/255e9f7bade89fe33789cd28a64e847b7ba7cf2a.jpg"],
            "more_like_this":["3", "6", "8"],
	       },
        "2": {
            "id": "2",
            "title": "Your Throne",
            "image":"https://swebtoon-phinf.pstatic.net/20200513_169/1589334371783aBm6j_JPEG/04_EC9E91ED9288EC8381EC84B8_mobile.jpg?type=crop540_540",
            "summary": "Tensions are brewing under the seemingly calm surface of the Vasilios Empire, a kingdom ruled by the Imperial Family and the Temple. The Solons are the most influential family in Vasilios, and Lady Medea Solon is mastermind behind it all. In a twist of fate, she loses her place next to Crown Prince Eros, but resolves to do whatever it will take to win back what's rightfully hers. Will she reclaim her throne?",
            "author": "SAM",
	        "rating": "9.82",
            "reviews": ["You might be looking at the synopsis and thinking, 'Eh, it’s another royalty-revenge story cliché,' but don’t be so quick to write it off and judge it as just that. I’ve read many other manga that have a similar synopsis, but Your Throne stands out and comes out on top of the others.", "What a pleasant piece of work, a mysterious and captivating story about two characters whose personnalities are in opposition and yet share a fate so intertwined with one another.", "I am absolutely in love with Your Throne. Words cannot describe the depth of my... like I said, no words. I love the psychological warfare going on between the characters. I love the complexity of their schemes. I love the constant character development. I love all of the 4 main characters. The plot is so intriguing! Their background stories are heart-wrenching ㅠㅠ The art is so beautiful <3 Whenever I think about an update I get uncharacteristically giddy and (mildly) obsessed. Pls give it a read on Webtoon to support the author."],
	        "complete": "false",
            "ep1":"https://www.webtoons.com/en/fantasy/your-throne/ep-1-the-two-ladies-of-rumor-1/viewer?title_no=2009&episode_no=1",
            "art_img":["https://cdn.myanimelist.net/images/manga/1/236523.jpg", "https://i.pinimg.com/originals/f7/c8/49/f7c8493fed8ea091ba06ddcd5344e14a.png", "https://i.pinimg.com/736x/13/6d/2a/136d2af8232e68a869cb7c34c53d5109.jpg", "https://static.tvtropes.org/pmwiki/pub/images/d8358e7e5590e9e22743060c8dc3f018.jpg"],
            "more_like_this":["4", "7", "9"],
	       },
        "3": {
            "id": "3",
            "title": "Toaster Dude",
            "image":"https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/hostedimages/1623203269i/31461530.png",
            "summary": "All his life, Dude has had one simple dream. And that was to own a toaster. And, he’s finally done it. Nothing could possibly go wrong... right?",
            "author": "little bobler",
	        "rating": "9.77",
            "reviews": ["incredible. amazing. aesthetically on point. made me genuinely laugh out loud which is an Achievement.","Bruh this is just hilarious and So damn interesting inspite of having a blunt plot at the start. But I assure you YOUR OPINION ON COMICS WILL CHANGE!","absurdly hilarious", "Just a simple dude who dreams of owning his very own toaster - how much more wholesome can you get?", "amazing i loved it so much i read it in a day"],
	        "complete": "true",
            "ep1": "https://www.webtoons.com/en/comedy/toaster-dude/ep-1/viewer?title_no=1983&episode_no=1",
            "art_img":["https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1630758740l/58923056.jpg","https://cdn.anime-planet.com/manga/primary/toaster-dude-1.jpg?t=1625864617", "https://img.manganato.info/image/2020/11/14/Toaster-Dude-EP-24-6.jpg"],
            "more_like_this":["1", "6", "8"],
	       },
        "4": {
            "id": "4",
            "title": "Purple Hyacinth",
            "image":"https://swebtoon-phinf.pstatic.net/20220222_275/1645494592231vzfkq_JPEG/4PurpleHyacinth_landingpage_mobile.jpg?type=crop540_540",
            "summary": "Her ability to detect lies has made her an outstanding officer of the law. Yet still, she remains haunted by her inability to save the ones she loved from a gruesome fate many years ago. Now, she uses her powerful gift to defend the defenseless at any cost – even if it means teaming up with a deadly assassin to fight evil in a world gone mad.",
            "author": "Ephemerys",
	        "rating": "9.91",
            "reviews": ["Just finished the first season and it was amazing. The art was beautiful and the characters were entertaining and mysterious. And although there's a lot of blood and stuff, there are some funny parts too. There was also music in some of the episodes and the music fit really well with the story. I'm excited for season 2.", "This is possibly one of the best webtoons I have read to date. The story has a mature flair to it and the characters are well fleshed out (and exceptionally gorgeous to look at!) with an extremely fun banter-ridden dynamic. The narrative also has amazing pacing and keeps you on  the edge of your seat. A must for anyone who loves the thriller/suspense genre.", "This is one of the best webtoons I have read. Just read the prologue and I bet you would become interested!! Read it on Line Webtoon only so that you can enjoy the chapter specific music", "I love this manga. It has such an amazing plot, beautiful art and I honestly think it's one of the best webtoons I've ever read. Definetely recommend this."],
	        "complete": "false",
            "ep1": "https://www.webtoons.com/en/mystery/purple-hyacinth/ep-0-prologue/viewer?title_no=1621&episode_no=1",
            "art_img":["https://i.pinimg.com/originals/07/b0/61/07b0617971d5ae51c43e30cb17e4d737.jpg", "https://preview.redd.it/mmwwy2lh6d251.jpg?width=640&crop=smart&auto=webp&s=d7e7051425d2a7fcb267276347a9e1df21617974", "https://i.pinimg.com/736x/b0/6b/17/b06b17586a4b9ea711ca324b662e82bb.jpg"],
            "more_like_this":["2", "5", "7"],
	       },
        "5": {
            "id": "5",
            "title": "Eleceed",
            "image":"https://swebtoon-phinf.pstatic.net/20210410_276/1618006860453g7PCa_JPEG/804_EC9E91ED9288EC8381EC84B8_mobile.jpg?type=crop540_540",
            "summary": "Jiwoo is a kind-hearted young man who harnesses the lightning quick reflexes of a cat to secretly make the world a better place – one saved little child or foster pet at a time. Kayden is a secret agent on the run, who finds himself stuck in the body of a…um…decidedly fat old fluffy cat. Together, armed with Jiwoo’s super powers and Kayden’s uber-smarts, they’re out to fight those forces who would let evil rule this world. That is, if they can stand each other long enough to get the job done.",
            "author": "Jeho Son",
	        "rating": "9.95",
            "reviews": ["This is really brilliant and just keeps improving with each chapter. Now this is expected because it is charcter-driven story and once the characters grow upon you your enjoyment in the story will keep increasing.", "This is the funniest, cutest, most enjoyable supernatural manga I have ever read.", "I LOVE ELECEED! The story is great! and Kayden (casien nitrate) IS SO CUTE XD ITs great and the art is so pretty! I totally reccomend this its available on webtoon!", "Highly recommend reading.  Very enjoyable and super funny.", "I mean what can i say. This manga is so good, i literally couldn't stop reading it  , it took me 3 days to finish it  , if i didn't give the story a 10/10 for the reason that we haven't  seen a lot about the outside world and stuff, im hoping that in the near future we get a good world-building event"],
	        "complete": "false",
            "ep1": "https://www.webtoons.com/en/action/eleceed/episode-1/viewer?title_no=1571&episode_no=1",
            "art_img":["https://preview.redd.it/hh3jefr2d9h71.png?width=640&crop=smart&auto=webp&s=04cdfb57944fe02c7f76e7466353494dbb90d1ea","https://preview.redd.it/dzbh5puhewu61.jpg?width=640&crop=smart&auto=webp&s=bf2ee99410b0e986dad3d220b93a34eee088aff7","https://i.pinimg.com/564x/4b/14/d9/4b14d9a4dd85d898088647976c222706.jpg"],
            "more_like_this":["1", "3", "6"],
	       },
        "6": {
            "id": "6",
            "title": "Let's Play",
            "image":"https://swebtoon-phinf.pstatic.net/20210629_204/1624917440082pN0q6_PNG/3Let27sPlay_mobile_landingpage.png?type=crop540_540",
            "summary": "She’s young, single and about to achieve her dream of creating incredible videogames. But then life throws her a one-two punch: a popular streamer gives her first game a scathing review. Even worse she finds out that same troublesome critic is now her new neighbor! A funny, sexy and all-too-real story about gaming, memes and social anxiety. Come for the plot, stay for the doggo.",
            "author": "Mongie",
	        "rating": "9.6",
            "reviews": ["Let’s play is my all time favorite webtoon, beating true beauty by a hair. I can’t wait for the new installments, but every creator deserves a good break so I’ll wait patiently", "THIS HAD ME SQUEALIN Y’ALL I LOVE IT", "There are so many good things to say about this comic that I don't even know where to start. The diverse/lgbtq/disability rep, the mental health awareness, the relatable MC who suffers from anxiety, the gamer battling depression, the many amazing representations of women dealing with issues like aging, healing oneself from trauma, normalizing women who watch porn and play games and are strong in their own ways, constantly breaking gender expectations-", "Hands down to Mongié for giving birth to a webtoon so beautiful, it watered all the crops, my skin is cleared, my depression is cured, my wig is snatched, my mind is blown and my hands are thrown."],
	        "complete": "false",
            "ep1": "https://www.webtoons.com/en/romance/letsplay/ep-1-/viewer?title_no=1218&episode_no=1",
            "art_img":["https://i.pinimg.com/originals/1d/b7/72/1db7724ac541e9bddd507a59c6bc5745.jpg", "http://wiki.letsplaycomic.com/images/3/3c/Marshall-01.jpg", "http://wiki.letsplaycomic.com/images/8/86/Charles-02.jpg"],
            "more_like_this":["1", "3", "8"],
	       },
        "7": {
            "id": "7",
            "title": "Freaking Romance",
            "image":"https://swebtoon-phinf.pstatic.net/20181021_205/1540083365479ETvSn_JPEG/04_EC9E91ED9288EC8381EC84B8_mobile.jpg?type=crop540_540",
            "summary": "A sexy supernatural story about being out on your own, finding your dream apartment and discovering that your new place is haunted by a handsome spectral stranger from another dimension. Sure, HE can’t see you and YOU can’t touch him, but who said every relationship starts out perfectly? It'll be fine, right?",
            "author": "Snailords",
	        "rating": "9.76",
            "reviews": ["Oh my damn, this went from 0 to 100 with batshit speed. A sexy romance with a crazy horror-ish twist? OH YEAH","how is everyone in this comic so good-looking", "Hella cute plot and characters! Zylith is my spirit animal and I love her fiestyness.", "absolutely love the concept and characters", "Super cute! The art is stunningly gorgeous and the plot is just too cute. Can't wait for more to come out!"],
	        "complete": "true",
            "ep1": "https://www.webtoons.com/en/romance/freaking-romance/episode-1/viewer?title_no=1467&episode_no=1",
            "art_img":["https://pbs.twimg.com/ext_tw_video_thumb/1112319619077935105/pu/img/PfYjxAe-VtJLZl0g.jpg", "https://i.pinimg.com/originals/a5/18/d3/a518d31508026f16ac5f2169803b3a4b.jpg", "https://pbs.twimg.com/media/DvPgMqNWkAAzDu1.jpg", "https://i.pinimg.com/736x/ed/9b/77/ed9b77c6b09429953ed92f750b8c2462.jpg"],
            "more_like_this":["2", "4", "5"],
	       },
        "8": {
            "id": "8",
            "title": "Tori and Samuel",
            "image":"https://swebtoon-phinf.pstatic.net/20190819_278/1566225613919x8skv_JPEG/thumbnail.jpg",
            "summary": "Best friends for life: The story of an eager corgi and a sardonic munchkin cat. Join them as they go through life together — meeting friends, friends, and more friends on the way.",
            "author": "Bobblejot",
	        "rating": "9.91",
            "reviews": ["I just picked this up like 5 minutes ago but the art is so adorable and the characters are really funny, highly recommend!! Centered around a corgi and a cat so yeah definitely gonna be reading this more."],
	        "complete": "false",
            "ep1": "https://www.webtoons.com/en/challenge/tori-and-samuel/supermodel-legs/viewer?title_no=327950&episode_no=1",
            "art_img":["https://youthopia.sg/wp-content/uploads/2021/02/tori_and_samuel.jpg", "https://static.manta.net/2021-09-03/E4/E4IY2vV7VVvxWll5.jpg", "https://static.boredpanda.com/blog/wp-content/uploads/2019/12/cute-cat-comics-tori-and-samuel-bobblejot-25-5e01d22edd8d9__700.jpg"],
            "more_like_this":["1","6", "3"],
	       },
        "9": {
            "id": "9",
            "title": "Bastard",
            "image":"https://swebtoon-phinf.pstatic.net/20150608_96/1433732722146JfafB_JPEG/EC9E91ED9288EC8381EC84B8_mobile.jpg?type=crop540_540",
            "summary": "There is nowhere that Seon Jin can find solace. At school, he is ruthlessly bullied due to his unsettlingly quiet nature and weak appearance. However, this is not the source of Jin's insurmountable terror: the thing that he fears more than anything else is his own father. To most, Jin's father is a successful businessman, good samaritan, and doting parent. But that is merely a facade; in truth, he is a deranged serial killer—and Jin is his unwilling accomplice. For years, they have been carrying out this ruse with the police being none the wiser. However, when his father takes an interest in the pretty transfer student Yoon Kyun, Jin must make a decision—be the coward who sends her to the gallows like all the rest, or be the bastard of a son who defies his wicked parent.",
            "author": "Carnby Kim ",
	        "rating": "9.87",
            "reviews": ["I honestly cannot remember the last time I’ve gotten so mind fucked. I’m never recovering from this. So brilliant. The plot was so gripping, unpredictable, dark and twisted, the pacing was literally PERFECT, the dialogue was clever and realistic and don’t even get me started on the CHARACTERS. So complex, so unique, so flawed yet so likable... I never expected to see a work of such quality among webcomics. 10/10 would recommend.", "WICKED, in every sense of the word.", "This was truly an awesome psychological thriller that can f*ck with your mind (plus the artwork totally suits the story). If you're for something like that to read, I highly recommend Bastard.", "WOW! This was intense and gripping and mind-blowing and so scary. I need time to process everything but oh damn this webcomic is one in a kind.", "despite being utterly terrified by that one panel four episodes in and will probably have that one image haunt me for the rest of my life, i absolutely //loved// every second of this webtoon from start to end and has got to be one of the best ones i've read next to dice."],
	        "complete": "true",
            "ep1": "https://www.webtoons.com/en/thriller/bastard/ep-0/viewer?title_no=485&episode_no=1",
            "art_img":["https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1445459094i/27250890._UY612_SS612_.jpg", "http://pm1.narvii.com/6176/3542b3832aa293c7bfcd41812352324dd5b22179_00.jpg", "https://i.pinimg.com/originals/04/b8/0c/04b80c4b75cc4ca947347aab062d31b1.jpg"],
            "more_like_this":["2"],
	       },
        "10": {
            "id": "10",
            "title": "True Beauty",
            "image":"https://swebtoon-phinf.pstatic.net/20210129_254/1611875610116c2Tub_JPEG/304_EC9E91ED9288EC8381EC84B8_mobile.jpg?type=crop540_540",
            "summary": "After binge-watching beauty videos online, a shy comic book fan masters the art of makeup and sees her social standing skyrocket as she becomes her school’s prettiest pretty girl overnight. But will her elite status be short-lived? How long can she keep her real self a secret? And what about that cute boy who knows her secret?",
            "author": "Yaongyi",
	        "rating": "9.54",
            "reviews": ["As a micro influencer who loves horror and makeup, I’ve been obsessed with this series for over a year and the obsession hasn’t diminished in the least", "enjoyed the first few chapters but now the plot's not going anywhere ://", "AH this webtoon was extremely addictive. Like, I got through 128 episodes in less than 24 hours AHH. Anyways, the art is really good, but the plot is ....shallow and tbh is there really any plot?", "The premise is quite cliched but the art is gorgeous and the love interests are decent and incredibly likeable, which is a rarity in these sorts of comics."],
	        "complete": "false",
            "ep1": "https://www.webtoons.com/en/romance/truebeauty/episode-0-/viewer?title_no=1436&episode_no=1",
            "art_img":["https://i0.wp.com/i.pinimg.com/736x/5a/cc/4f/5acc4f7654ed782443ff2d4b44641de3.jpg?resize=280%2C432&ssl=1", "https://i0.wp.com/giaallana.com/wp-content/uploads/2021/02/rgszg.jpg?resize=730%2C766&ssl=1", "https://img3.pillowfort.social/posts/1fdd6bbbca0e_true%20beauty%20ch%2023%202.PNG"],
            "more_like_this":["2", "4", "7"],
	       },
        }

def string_match (string1, string2):
    return string1.casefold() == string2.casefold()

def case_insensitive_in(string1, string2):
    # returns true if string2 is in string 1
    return string2.lower() in string1.lower()


# ROUTES

@app.route('/')
def home():
    global data
    most_popular = [data["1"], data["2"], data["3"]]
    return render_template('index.html', most_popular=most_popular) 

@app.route('/add')
def add():
    return render_template('add.html') 

@app.route('/edit/<id>')
def edit(id=None):
    global data
    item_info= data[id]

    more_titles=[]
    for i in item_info["more_like_this"]:
        more_titles.append(data[i]["title"])
    
    print(item_info)
    return render_template('edit.html', item_info=item_info, more_titles=more_titles) 


@app.route('/search_results', methods=['GET'])
def display_search_results():
    global data
    search_string = request.args["searchinput"]
    search_results = []

    for i in data:
        if case_insensitive_in(data[i]["title"], search_string) or case_insensitive_in(data[i]["author"], search_string) or case_insensitive_in(data[i]["summary"], search_string) or case_insensitive_in(data[i]["complete"], search_string):
            search_results.append(data[i])
    
    num_results=len(search_results)

    return render_template('search_results.html', search_string=search_string, search_results=search_results, num_results=num_results)

@app.route('/view/<id>')
def item_view(id=None):
    global data
    item_info= data[id]

    return render_template('item.html', item_info=item_info)  




# ajax

@app.route('/get_more_like_this', methods=['POST'])
def get_more_like_this():
    global data 

    json_data = request.get_json()   
    id = json_data["id"] 

    item_info= data[id]
    more_like_this = []
    for s in item_info["more_like_this"]:
        more_id = data[s]["id"]
        more_title = data[s]["title"]
        more_image = data[s]["image"]
        print(more_image)
        more_like_this.append({
            "id":more_id,
            "title":more_title,
            "image":more_image,
        })
    return jsonify(more_like_this=more_like_this)


@app.route('/add_data', methods=['POST'])
def add_data():
    global data, current_id
    json_data = request.get_json() 
    print(json_data) 
    new_id = str(current_id)

    more_like_this = []
    
    print(json_data["more_like_this"])
    for i in json_data["more_like_this"]:
        print(i)
        for j in data:
            if string_match(i, data[j]["title"]):
                more_like_this.append(j)

    print(more_like_this)

    new_data = {
        "id": new_id,
        "title": json_data["title"],
        "image": json_data["image"],
        "summary": json_data["summary"],
        "author": json_data["author"],
        "rating": str(json_data["rating"]),
        "reviews": json_data["reviews"],
        "complete": json_data["complete"],
        "ep1": json_data["ep1"],
        "art_img": json_data["art_img"],
        "more_like_this": more_like_this,
    }
    data[new_id] = new_data
    print(data[new_id])


    current_id+=1
    return jsonify(new_id=new_id)

@app.route('/edit_data', methods=['POST'])
def edit_data():
    global data
    json_data = request.get_json() 
    id = json_data["id"]
    more_like_this = []
    
    print(json_data["more_like_this"])
    for i in json_data["more_like_this"]:
        print(i)
        for j in data:
            if string_match(i, data[j]["title"]):
                more_like_this.append(j)

    new_data = {
        "id": json_data["id"],
        "title": json_data["title"],
        "image": json_data["image"],
        "summary": json_data["summary"],
        "author": json_data["author"],
        "rating": str(json_data["rating"]),
        "reviews": json_data["reviews"],
        "complete": json_data["complete"],
        "ep1": json_data["ep1"],
        "art_img": json_data["art_img"],
        "more_like_this": more_like_this,
    }
    data[id] = new_data
    return jsonify(id=id)



if __name__ == '__main__':
   app.run(debug = True)




