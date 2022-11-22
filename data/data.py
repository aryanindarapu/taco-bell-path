import requests
import csv
from bs4 import BeautifulSoup
from functions import *

HTML = """<li class="Directory-listItem"><a class="Directory-listLink" href="il/addison/555-w--lake-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Addison</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/alsip/11750-south-palaski-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Alsip</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/alton.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Alton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/anna/1195-e--vienna-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Anna</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/antioch/322-w-state-route-173.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Antioch</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/arlington-heights.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Arlington Heights</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/aurora.html" data-ya-track="directory_links" data-count="(4)"><span class="Directory-listLinkText">Aurora</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bartlett/960-s-state-route-59.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Bartlett</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/batavia/134-south-randall-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Batavia</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/belleville.html" data-ya-track="directory_links" data-count="(3)"><span class="Directory-listLinkText">Belleville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/belvidere.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Belvidere</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bensenville/1140-s-york-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Bensenville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/benton/634-west-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Benton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/berwyn/6956-ogden-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Berwyn</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bethalto/171-e--mcarthur-dr-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Bethalto</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bloomingdale/74-stratford-dr-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Bloomingdale</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bloomington.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Bloomington</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bolingbrook/444-n-bolingbrook-dr.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Bolingbrook</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/bourbonnais.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Bourbonnais</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/buffalo-grove/50-w-dundee-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Buffalo Grove</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/cahokia/1616-camp-jackson-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Cahokia</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/calumet-city/1501-river-oaks-dr.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Calumet City</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/calumet-park/12716-ashland-ave-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Calumet Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/canton/129-north-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Canton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/carbondale/1410-east-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Carbondale</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/carpentersville.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Carpentersville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/cary/660-northwest-highway.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Cary</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/caseyville/2413-n-89th-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Caseyville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/centralia/1077-w-broadway.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Centralia</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/champaign.html" data-ya-track="directory_links" data-count="(4)"><span class="Directory-listLinkText">Champaign</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/charleston/120-lincoln-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Charleston</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/chester/2235-state-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Chester</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/chicago.html" data-ya-track="directory_links" data-count="(35)"><span class="Directory-listLinkText">Chicago</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/chicago-heights/201-s-halstead-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Chicago Heights</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/chicago-ridge/444-chicago-ridge-mall.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Chicago Ridge</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/chillicothe/604-n--4th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Chillicothe</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/cicero/2225-s-cicero-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Cicero</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/collinsville/1001-belt-line-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Collinsville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/columbia/200-columbia-center.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Columbia</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/countryside/5611-s-la-grange-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Countryside</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/crest-hill/1818-plainfield-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Crest Hill</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/crestwood/13745-s-cicero.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Crestwood</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/crete/23210-volbrecht-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Crete</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/crystal-lake/420-virginia-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Crystal Lake</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/danville.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Danville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/darien/7419-s-cass-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Darien</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/de-kalb/1209-w-lincoln-hwy.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">De Kalb</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/decatur.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Decatur</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/des-plaines.html" data-ya-track="directory_links" data-count="(3)"><span class="Directory-listLinkText">Des Plaines</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/diamond/2780-division-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Diamond</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/dixon/1312-north-galena-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Dixon</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/dolton/1323-sibley-boulevard.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Dolton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/downers-grove/7451-lemont-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Downers Grove</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/du-quoin/31-southtowne-shopping-center.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Du Quoin</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/east-alton/101-niagara-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">East Alton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/east-peoria/108-w-camp-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">East Peoria</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/east-saint-louis/699-state-route-203.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">East Saint Louis</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/edwardsville/1710-troy-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Edwardsville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/effingham/1201-n-keller.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Effingham</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/elburn/1075-n-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Elburn</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/elgin.html" data-ya-track="directory_links" data-count="(3)"><span class="Directory-listLinkText">Elgin</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/elk-grove-village.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Elk Grove Village</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/fairview-heights/6599-n-illinois-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Fairview Heights</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/flora/1442-worthey-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Flora</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/forest-park.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Forest Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/forsyth/1400-hickory-point-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Forsyth</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/fox-lake/54-s-us-highway-12.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Fox Lake</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/frankfort/20160-lagrange-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Frankfort</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/franklin-park/2721-rose-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Franklin Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/freeport/1882-s-west-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Freeport</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/galesburg.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Galesburg</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/glen-ellyn/370-roosevelt-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Glen Ellyn</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/glendale-heights.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Glendale Heights</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/glenview/1757-waukegan.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Glenview</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/granite-city.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Granite City</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/grayslake/115-s--state-route-83.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Grayslake</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/great-lakes/540-cluverius-avenue--.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Great Lakes</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/greenville/1607-south-route-127.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Greenville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/gurnee/6360-grand-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Gurnee</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/hanover-park.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Hanover Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/harrisburg/712-s--commercial-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Harrisburg</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/harvard/325-s-division-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Harvard</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/harwood-heights/5050-n--harlem-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Harwood Heights</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/herrin/1709-s-park-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Herrin</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/hickory-hills/8760-w-95th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Hickory Hills</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/highland/1305-mercantile-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Highland</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/highland-park/2566-skokie-valley-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Highland Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/hinsdale/i-294-milepost-25.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Hinsdale</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/homer-glen/14348-s--bell-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Homer Glen</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/huntley/13320-s-highway-47.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Huntley</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/jacksonville/837-w-morton.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Jacksonville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/jerseyville/1400-s--state-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Jerseyville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/joliet.html" data-ya-track="directory_links" data-count="(3)"><span class="Directory-listLinkText">Joliet</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/kankakee/2942-riverstone-court.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Kankakee</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/kewanee/623-tenney-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Kewanee</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lake-forest/13783-west-oasis-service-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lake Forest</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lake-in-the-hills/231-n-randall-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lake In The Hills</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lake-zurich/801-w-main-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lake Zurich</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lemont/15663-127th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lemont</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/libertyville/1308-n-milwaukee-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Libertyville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lindenhurst/2081-east-grand-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lindenhurst</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lisle/1015-maple-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lisle</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/litchfield/1201-w-weir-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Litchfield</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/lockport/16616-w--159th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Lockport</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/loves-park.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Loves Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/machesney-park/1297-west-lane-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Machesney Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/macomb/420-west-jackson.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Macomb</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/manteno/195-south-creek-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Manteno</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/marengo/19800-us-route-20.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Marengo</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/marion.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Marion</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/markham/2945-west-159th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Markham</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/marshall/107-w-trefz.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Marshall</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/mattoon/105-swords-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Mattoon</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/mchenry/4112-w-elm-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">McHenry</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/melrose-park/825-w-north-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Melrose Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/mendota/1009-steve-bowne-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Mendota</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/minooka/501-bob-blair-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Minooka</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/moline.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Moline</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/monee/5737-w--monee-manhattan-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Monee</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/monmouth/201-maple-city-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Monmouth</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/montgomery/1950-douglas-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Montgomery</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/morris/1820-n-division-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Morris</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/morton/100-west-ashland-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Morton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/morton-grove/8840-waukegan-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Morton Grove</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/mount-vernon.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Mount Vernon</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/mundelein.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Mundelein</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/murphysboro/515-walnut.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Murphysboro</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/naperville.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Naperville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/new-lenox/420-w-maple-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">New Lenox</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/niles/7535-n-harlem-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Niles</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/normal/1527-e-college-ave.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Normal</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/north-aurora/2060-west-orchard-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">North Aurora</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/north-chicago/2222-green-bay-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">North Chicago</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/north-riverside/7501-w-cermak-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">North Riverside</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/northlake/51-w--north-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Northlake</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/o-fallon.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">O&#39;Fallon</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/oak-lawn/6049-west-95th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Oak Lawn</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/olney/908-east-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Olney</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/orland-hills/9281-159th-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Orland Hills</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/orland-park/364-orland-square-drive.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Orland Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/oswego/3423-orchard-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Oswego</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/ottawa/4109-columbus-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Ottawa</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/palatine.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Palatine</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/palos-hills/7601-w-111th-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Palos Hills</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/paris/528-e--jasper-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Paris</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/park-forest/413-sauk-trail.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Park Forest</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/pekin/1920-court-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Pekin</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/peoria.html" data-ya-track="directory_links" data-count="(4)"><span class="Directory-listLinkText">Peoria</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/peru/5257-trompeter-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Peru</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/pontiac/1600-w-reynolds-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Pontiac</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/quincy.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Quincy</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/rantoul/629-champaign-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Rantoul</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/richmond/10710-main-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Richmond</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/robinson/1414-east-main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Robinson</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/rochelle/1221-n-caron-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Rochelle</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/rock-island/1533-38th-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Rock Island</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/rockford.html" data-ya-track="directory_links" data-count="(6)"><span class="Directory-listLinkText">Rockford</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/romeoville/76-s--weber-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Romeoville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/roscoe/4638-e--rockton-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Roscoe</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/rosemont/9467-w-higgins-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Rosemont</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/round-lake-beach/306-w-rollins-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Round Lake Beach</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/saint-charles.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Saint Charles</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/salem/1431-west-main.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Salem</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/sandwich/130-duvick-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Sandwich</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/schaumburg.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Schaumburg</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/shelbyville/1000-w--main-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Shelbyville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/shorewood/996-brook-forest-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Shorewood</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/skokie/8329-skokie-blvd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Skokie</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/south-elgin/490-randall-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">South Elgin</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/sparta/1400-north-market-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Sparta</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/springfield.html" data-ya-track="directory_links" data-count="(4)"><span class="Directory-listLinkText">Springfield</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/sterling/405-locust-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Sterling</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/streamwood/665-s--sutton-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Streamwood</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/streator/2008-n-bloomington-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Streator</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/sycamore/1301-dekalb-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Sycamore</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/taylorville/610-n-webster-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Taylorville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/tinley-park/7224-w--191st-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Tinley Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/troy/908-edwardsville-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Troy</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/tuscola/1104-e--southline.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Tuscola</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/urbana/1003-university.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Urbana</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/vandalia/2737-veterans-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Vandalia</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/vernon-hills/906-hawthorn-center.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Vernon Hills</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/villa-park/125-w-roosevelt-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Villa Park</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/washington/1896-washington-rd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Washington</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/waterloo/918-n-market-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Waterloo</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/watseka/1530-e-walnut-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Watseka</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/wauconda/705-w-liberty-st.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Wauconda</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/waukegan.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Waukegan</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/west-chicago/335-neltnor-blvd-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">West Chicago</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/west-frankfort/832-factory-outlet-dr-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">West Frankfort</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/westchester/3063-s-wolf-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Westchester</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/westmont/13-w-ogden-avenue.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Westmont</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/wheaton/345-rice-lake-square.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Wheaton</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/wheeling/150-e--dundee-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Wheeling</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/winnebago/805-cannell-puri-court.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Winnebago</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/wood-dale/322-w-irving-park-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Wood Dale</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/wood-river/1850-memorial-lane.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Wood River</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/woodstock/400-s-eastwood-dr.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Woodstock</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/yorkville/221-w--veterans-parkway.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Yorkville</span></a></li>
                     <li class="Directory-listItem"><a class="Directory-listLink" href="il/zion/1913-sheridan-rd.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Zion</span></a></li>"""


# HTML = """<li class="Directory-listItem"><a class="Directory-listLink" href="il/addison/555-w--lake-st-.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Addison</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/alsip/11750-south-palaski-road.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Alsip</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/alton.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Alton</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/anna/1195-e--vienna-street.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Anna</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/antioch/322-w-state-route-173.html" data-ya-track="directory_links" data-count="(1)"><span class="Directory-listLinkText">Antioch</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/arlington-heights.html" data-ya-track="directory_links" data-count="(2)"><span class="Directory-listLinkText">Arlington Heights</span></a></li>
#                      <li class="Directory-listItem"><a class="Directory-listLink" href="il/aurora.html" data-ya-track="directory_links" data-count="(4)"><span class="Directory-listLinkText">Aurora</span></a></li>"""

URL_BASE = "http://locations.tacobell.com/"

# stores the location queries
locations = []


# create an array with the location queries
# ----- uncomment if you need to update "locations.csv"
# locations = get_locations(HTML)
# write_to_csv('locations.csv', locations)


# iterates through "locations.csv" to populate the locations array
with open('locations.csv') as locationsFile:
    reader = csv.reader(locationsFile)
    for location in reader:
        locations.append(location[0])


# get the coordinates for every location

# maps a lat;long to an address
locationCoordinateDict = {}

# maps current lat;long to nearby lat;longs
nearbyCoordinatesDict = {}
coordinates = []
for location in locations:
    testLocation = URL_BASE + location
    locationHTML = requests.get(testLocation).text
    get_coords(locationHTML, locationCoordinateDict, nearbyCoordinatesDict)



write_to_csv_new(locationCoordinateDict, nearbyCoordinatesDict)
