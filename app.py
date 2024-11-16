from flask import Flask, render_template

app = Flask(__name__)


# TODO: Restaurant List of Dictionaries
# image_url, restaurant_name, status, location, id
restaurants = [
    {
        "id": 1,
        "location": "Manila, Philippines",
        "restaurant_name": "Manam Comfort Filipino Food",
        "status": "Closed",
        "image_url": "https://www.rappler.com/tachyon/2020/11/manam.jpg"
    },
    {
        "id": 2,
        "location": "Taguig, Philippines",
        "restaurant_name": "Locavore",
        "status": "Open",
        "image_url": "https://cdn1.clickthecity.com/wp-content/uploads/2023/09/06160256/Locavore_Estancia_3-Thumb.jpg"
    },{
        "id": 3,
        "location": "Makati, Philippines",
        "restaurant_name": "Blackbird by Chef Colin Mackay",
        "status": "Open",
        "image_url": "https://i0.wp.com/farm4.staticflickr.com/3887/14655643787_cf802d0fb8_b.jpg?resize=1024%2C683&ssl=1"
    },{
        "id": 4,
        "location": "Pasay City, Philippines",
        "restaurant_name": "Vikings Luxury Buffet",
        "status": "Open",
        "image_url": "https://primer.com.ph/eat/wp-content/uploads/sites/4/2014/05/DSC_0481_2.jpg"
    },{
        "id": 5,
        "location": "Tagaytay",
        "restaurant_name": "Antonio’s",
        "status": "Open",
        "image_url": "https://uploads-ssl.webflow.com/6322ae7d33dd78948d865447/63b7efce438701304a75043b_meta%20image%20-%20Antonio's%20Tagaytay.webp"
    },{
        "id": 6,
        "location": "Cebu City, Philippines",
        "restaurant_name": "Samgyupsalamat",
        "status": "Closed",
        "image_url": "https://business.inquirer.net/files/2023/03/Samgyupsalamat-Photo-1.jpg"
    },
    {
        "id": 7,
        "location": "Quezon City, Philippines",
        "restaurant_name": "Ramen Nagi",
        "status": "Open",
        "image_url": "http://1.bp.blogspot.com/-zMgPawd2zuI/Vds2kVDZsII/AAAAAAAAB5w/aYjzycQD4qY/s1600/Ramen%2BNagi%2BWhere%2BYou%2BCan%2BFind%2Bthe%2BBest%2BRamen%2Bin%2BTown.jpg"
    },
    {
        "id": 8,
        "location": "Cebu City, Philippines",
        "restaurant_name": "The Pig & Palm",
        "status": "Open",
        "image_url": "https://c6.staticflickr.com/9/8474/29331940973_9f05d28ff2_b.jpg"
    },
    {
        "id": 9,
        "location": "Intramuros, Manila",
        "restaurant_name": "La Cathedral Café",
        "status": "Open",
        "image_url": "https://www.windowseat.ph/wp-content/uploads/2020/08/la-cathedral.jpg"
    },
    {
        "id": 10,
        "location": "BGC, Philippines",
        "restaurant_name": "Sunnies Café",
        "status": "Open",
        "image_url": "https://images.summitmedia-digital.com/spotph/images/2016/10/27/SunniesCafeMega_11.jpg"
    },
    {
        "id": 11,
        "location": "Manila, Philippines",
        "restaurant_name": "Din Tai Fung",
        "status": "Closed",
        "image_url": "https://www.rappler.com/tachyon/2022/08/din-tai-fung-moa-branch.jpg?resize=1280%2C720&zoom=1"
    },
    {
        "id": 12,
        "location": "Manila, Philippines",
        "restaurant_name": "The Aristocrat",
        "status": "Closed",
        "image_url": "https://mnltoday.ph/wp-content/uploads/2022/06/08481.jpg"
    },
    {
        "id": 13,
        "location": "Quezon City, Philippines",
        "restaurant_name": "Mango Tree",
        "status": "Open",
        "image_url": "https://www.thai2night.com/upload/shop/photo_cover/master/shop_shop_photo_cover_6705_1614878935.jpg"
    },
    {
        "id": 14,
        "location": "Pampanga, Philippines",
        "restaurant_name": "Abe",
        "status": "Open",
        "image_url": "http://media.tumblr.com/tumblr_lqqt5winYb1qmd4d7.jpg"
    },
    {
        "id": 15,
        "location": "Girona, Spain",
        "restaurant_name": "El Celler de Can Roca",
        "status": "Closed",
        "image_url": "https://www.ericvokel.com/blog/wp-content/uploads/2015/08/EL-CELLER-DE-CAN-ROCA-.jpg"
    },
    {
        "id": 16,
        "location": "Modena, Italy",
        "restaurant_name": "Osteria Francescana",
        "status": "Open",
        "image_url": "https://tse4.mm.bing.net/th?id=OIP.toqfPTYZ-WMv4QK-SlR1bAHaEO&pid=Api&P=0&h=180"
    },
    {
        "id": 17,
        "location": "Bangkok, Thailand",
        "restaurant_name": "Gaggan",
        "status": "Closed",
        "image_url": "https://bk.asia-city.com/sites/default/files/untitled_design-12.png"
    },
    {
        "id": 18,
        "location": "New York, USA",
        "restaurant_name": "Momofuku Ko",
        "status": "Open",
        "image_url": "https://cdn.vox-cdn.com/thumbor/KGtaNUj2lmdgLyfWA0mAuTUspIA=/0x57:1600x957/1600x900/cdn.vox-cdn.com/uploads/chorus_image/image/44346630/15411127903_96130c3a30_h.0.0.jpg"
    },
    {
        "id": 19,
        "location": "California, USA    ",
        "restaurant_name": "The French Laundry",
        "status": "Open",
        "image_url": "https://thefoodxp.com/wp-content/uploads/2019/11/40568609_2230848436956742_1053506704060186624_o.0-1.jpg"
    },
    {
        "id": 20,
        "location": "Tokyo, Japan",
        "restaurant_name": "Narisawa",
        "status": "Closed",
        "image_url": "https://www.gratinez.fr/wp-content/uploads/2017/05/narisawa-tokyo-theworlds50best-yoshihiro-restaurant.jpg"
    },
    {
        "id": 21,
        "location": "Tokyo, Japan",
        "restaurant_name": "Sukiyabashi Jiro",
        "status": "Open",
        "image_url": "https://tse2.mm.bing.net/th?id=OIP.gh8wWepCvdcruIrKWbiYYQHaFj&pid=Api&P=0&h=180"
    },
    {
        "id": 22,
        "location": "New York, USA",
        "restaurant_name": "Eleven Madison Park",
        "status": "Open",
        "image_url": "https://blogs-images.forbes.com/kristintablang/files/2017/10/New-Eleven-Madison-Park-1200x675.jpg"
    },
    {
        "id": 23,
        "location": "Menton, France",
        "restaurant_name": "Mirazur",
        "status": "Open",
        "image_url": "https://tse3.mm.bing.net/th?id=OIP.YdbPaiTayInUJztJcpcUxgHaEK&pid=Api&P=0&h=180"
    },
    {
        "id": 24,
        "location": "Melbourne, Australia",
        "restaurant_name": "Attica",
        "status": "Open",
        "image_url": "https://media.cntraveler.com/photos/5b8448d226856907ba2a9138/16:9/w_2560%2Cc_limit/Attica_Colin%252520Page_2018_Interior%2525202.jpg"
    },
    {
        "id": 25,
        "location": "Mexico City",
        "restaurant_name": "Pujol",
        "status": "Closed",
        "image_url": "https://tse4.mm.bing.net/th?id=OIP.LWamT5lpdFAFGcq60V-T3AHaE6&pid=Api&P=0&h=180"
    },
    {
    "id": 26,
    "location": "Lima, Peru",
    "restaurant_name": "Central",
    "status": "Open",
    "image_url": "https://viagemeturismo.abril.com.br/wp-content/uploads/2023/06/Sala-1-Central-By-Gustavo-Vivanco.jpg?quality=90&strip=info&w=1280&h=720&crop=1"
    },
    {
    "id": 27,
    "location": "Mexico City, Mexico",
    "restaurant_name": "Quintonil",
    "status": "Open",
    "image_url": "https://thevendry.com/cdn-cgi/image/height=1920,width=1920,fit=contain,metadata=none/https://s3.us-east-1.amazonaws.com/uploads.thevendry.co/23052/1682343802314_2022-08-18.jpg"
    },
    {
    "id": 28,
    "location": "Copenhagen, Denmark",
    "restaurant_name": "Geranium",
    "status": "Closed",
    "image_url": "https://settingmind.com/wp-content/uploads/geranium-dec18-34-scaled.jpg"
    },
    {
    "id": 29,
    "location": "Larrabetzu, Spain",
    "restaurant_name": "Azurmendi",
    "status": "Open",
    "image_url": "https://fichas-gr.s3.amazonaws.com/media/thumbnails/filer_public/34/80/3480b46d-f0b5-4e25-9693-dbaf1e1d54e9/azurmendi_2018_1_1284x850_q75_middle.jpg"
    },
    {
    "id": 30,
    "location": "New York, USA",
    "restaurant_name": "Le Bernardin",
    "status": "Closed",
    "image_url": "https://www.shawmut.com/assets/images/back_end/portfolio/1_1423232488_LeBernardin-NYC_4.jpg"
    },
    {
    "id": 31,
    "location": "New York, USA",
    "restaurant_name": "Blue Hill at Stone Barns",
    "status": "Open",
    "image_url": "https://pyxis.nymag.com/v1/imgs/3c6/112/8d0e3a03db6cbd7f63b559c42663254d0e-blue-hill-at-stone-barns-01.jpg"
    },
    {
    "id": 32,
    "location": "San Francisco, USA",
    "restaurant_name": "Benu",
    "status": "Open",
    "image_url": "https://theworldkeys.com/wp-content/uploads/2022/10/Benu-Restaurant-San-Francisco_theworldkeys.webp"
    },
    {
    "id": 33,
    "location": "Ouches, France",
    "restaurant_name": "Maison Troisgros",
    "status": "Closed",
    "image_url": "https://www.luxeat.com/wp-content/uploads/2020/06/cuisine-1-1440x600-1.jpg"
    },
    {
    "id": 34,
    "location": "London, UK",
    "restaurant_name": "The Ledbury",
    "status": "Open",
    "image_url": "https://media.timeout.com/images/105555340/750/422/image.jpg"
    },
    {
    "id": 35,
    "location": "Dubai, UAE",
    "restaurant_name": "Zuma",
    "status": "Open",
    "image_url": "https://assets-us-01.kc-usercontent.com/9e9a95c0-1d15-00d5-e878-50f070203f13/3dbb68aa-cfa6-4cb2-95c3-b2f2da725d18/zuma-restaurant-slider-1.jpg"
    },
    {
    "id": 36,
    "location": "San Sebastián, Spain",
    "restaurant_name": "Akelarre",
    "status": "Closed",
    "image_url": "https://u.tfstatic.com/restaurant_photos/861/11861/169/612/akelarre-akelarre-1-5e255.jpg"
    },
    {
    "id": 37,
    "location": "Lima, Peru",
    "restaurant_name": "Astrid y Gastón",
    "status": "Open",
    "image_url": "https://cdn.thespaces.com/wp-content/uploads/2022/07/Astrid-y-Gaston-restaurant-courtyard-interior-lima-peru-1478x985.jpg"
    },
    {
    "id": 38,
    "location": "Los Angeles, USA",
    "restaurant_name": "Nobu",
    "status": "Open",
    "image_url": "https://cms.robbreport.hk/wp-content/uploads/2023/12/00-Feature-image-scaled.jpeg"
    },
    {
    "id": 39,
    "location": "Bangkok, Thailand",
    "restaurant_name": "Sühring",
    "status": "Closed",
    "image_url": "https://media-cdn.tripadvisor.com/media/photo-s/0c/e4/1d/a6/suhring.jpg"
    },
    {
    "id": 40,
    "location": "Singapore",
    "restaurant_name": "Burnt Ends",
    "status": "Open",
    "image_url": "https://d3h1lg3ksw6i6b.cloudfront.net/media/image/2021/10/01/58fc46a2b0de4a5b941bc0933b9084d5_03+BE+Kitchen.jpg"
    },
    {
    "id": 41,
    "location": "Paris, France",
    "restaurant_name": "Arpège",
    "status": "Closed",
    "image_url": "https://www.paris.tourisme-ville.fr/wp-content/uploads/Arp%C3%A8ge-Int%C3%A9rieur-768x433.jpg"
    },
    {
    "id": 42,
    "location": "Kruishoutem, Belgium",
    "restaurant_name": "Hof Van Cleve",
    "status": "Open",
    "image_url": "https://njam.tv/sites/all/blog/annelies/interieur.jpg"
    },
    {
    "id": 43,
    "location": "San Sebastián, Spain",
    "restaurant_name": "Mugaritz",
    "status": "Open",
    "image_url": "https://media.cntraveler.com/photos/57600d13ba256ed2737af5f0/master/w_1200,c_limit/mugaritz-51C3380C.jpg?mbid=social_retweet"
    },
    {
    "id": 44,
    "location": "Moscow, Russia",
    "restaurant_name": "White Rabbit",
    "status": "Closed",
    "image_url": "https://cdni.rbth.com/rbthmedia/images/2018.06/article/5b2ba44e15e9f916c17e7e3d.jpg"
    },
    {
    "id": 45,
    "location": "Vienna, Austria",
    "restaurant_name": "Steirereck",
    "status": "Open",
    "image_url": "https://pillowandpepper.com/assets/product/i/a/ia_aussenansicht_steirereck_mit_meierei.jpeg"
    },
    {
    "id": 46,
    "location": "California, USA",
    "restaurant_name": "SingleThread",
    "status": "Closed",
    "image_url": "https://cdn.vox-cdn.com/thumbor/I4q2VMP1twL-iOrOHlptsHruSfc=/0x0:7360x4912/1200x0/filters:focal(0x0:7360x4912)/cdn.vox-cdn.com/uploads/chorus_asset/file/7572649/Eater_6478.jpg"
    },
    {
    "id": 47,
    "location": "Berlin, Germany",
    "restaurant_name": "Restaurant Tim Raue",
    "status": "Open",
    "image_url": "https://media.cntraveler.com/photos/5b917b6ae5b33d3889e6192f/16:9/w_1280%2Cc_limit/Restaurant-Tim-Raue_2018_Wolfgang-Stahr_Basement1.jpg"
    },
    {
    "id": 48,
    "location": "London, UK",
    "restaurant_name": "Dinner by Heston Blumenthal",
    "status": "Open",
    "image_url": "https://www.harpersbazaararabia.com/public/styles/square/public/images/2019/06/18/dinner-by-heston-blumenthal-7.jpg?itok=51SW5xB-"
    },
    {
    "id": 49,
    "location": "New York, USA",
    "restaurant_name": "Per Se",
    "status": "Closed",
    "image_url": "https://cdn.vox-cdn.com/thumbor/izOELxmchCAiIjYUQg20pgmU_4A=/55x0:941x665/1200x800/filters:focal(55x0:941x665)/cdn.vox-cdn.com/uploads/chorus_image/image/44255892/perse.0.0.jpg"
    },
    {
    "id": 50,
    "location": "Hong Kong, China",
    "restaurant_name": "Amber",
    "status": "Open",
    "image_url": "https://www.asia-bars.com/wp-content/uploads/2015/04/amber-2.jpg"
    }

]



@app.route('/')
def hello_world():  
    print(restaurants);
    return render_template('index.html', restaurants=restaurants)

if __name__ == '__main__':
    app.run(debug=True)
