# -*- coding: utf-8 -*-
"""Generate The Weird World Wiki — MediaWiki Vector-style, ~50 cross-linked articles."""
import os, re, html, json
OUT = "/Users/kevin/Projects/5gfordelarwen/wiki"
os.makedirs(OUT, exist_ok=True)

WIKI_NAME = "Dalarpedia"
TAGLINE = "From " + WIKI_NAME + ", the free encyclopaedia"

# ---------------------------------------------------------------- articles
# each: slug -> dict(title, intro(markup), infobox=[(k,v)], sections=[(head, markup)],
#                    seealso=[slug...], refs=[markup...], ext=[(label,url)...], cats=[...])
A = {}
def art(slug, title, intro, infobox=None, sections=None, seealso=None, refs=None, ext=None, cats=None):
    A[slug] = dict(title=title, intro=intro, infobox=infobox or [], sections=sections or [],
                   seealso=seealso or [], refs=refs or [], ext=ext or [], cats=cats or [])

art("dalarwen", "Dalarwen",
 "'''Dalarwen''' is a remote farmhouse and surrounding valley on the shore of [[llyn-brianne]] in mid-[[wales|Wales]], notable for receiving, and having always received, [[zero-bars|0.000 bars]] of mobile signal. It is the principal setting of the campaign for [[dalarwen-5g-grid|fifteen 5G towers]] and, beneath that, of the operations of [[isamsj|ISAMSJ]].",
 infobox=[("Type","Off-grid farmhouse / valley"),("Location","Head of the Towy valley, [[wales|Wales]]"),("Signal","0.000 bars (maintained)"),("Neighbours","None for miles (see [[sam]])"),("Sleeps","Nine (one never on the booking)"),("Operated by","[[division-of-absence|The Division of Absence]]")],
 sections=[("Signal","The absence of signal at Dalarwen is not a feature of the terrain but is ''applied'' nightly by the [[division-of-absence]], maintaining the [[exclusion-envelope]]. See also [[great-darkening]]."),
           ("Culture","Home of the [[the-pals|Pals of Dalarwen]], the [[loo-standing-society]], and an [[the-conservatory|electric piano]] that plays [[men-of-harlech]] at 04:00.")],
 seealso=["llyn-brianne","the-cube","exclusion-envelope","great-darkening"],
 cats=["Dalarwen","Places"])

art("llyn-brianne", "Llyn Brianne",
 "'''Llyn Brianne''' is a large reservoir at the head of the Towy valley, on whose shore [[dalarwen]] sits. It is an ''engineered'' body of water &mdash; dammed, controlled, held back on purpose &mdash; a fact from which the [[the-cube|Cube]] draws a well-known inference.",
 infobox=[("Type","Reservoir (not a lake)"),("Holds back","Water; also, allegedly, [[zero-bars|bars]]"),("Access","The [[dam-wall-road]] (Natural Resources Wales)"),("On approach","On your right, coming off the dam")],
 sections=[("The silence thesis","If the dam can hold back a whole valley of water, adherents ask, what else is it holding back? The [[tv-licence-suppression|licence-fee theory]] holds that the dam stores ''silence'', and the fee pays the standing charge.")],
 seealso=["dalarwen","dam-wall-road","tv-licence-suppression","exclusion-envelope"],
 ext=[("The reservoir on the field report","../about-dalarwen.html"),("Reviews on PalAdvisor","../reviews/index.html"),("Check the signal (GOV.VOID)","../gov/index.html")],
 cats=["Places","Infrastructure"])

art("isam", "ISAM",
 "'''ISAM''' is an intergalactic weaponry firm and the senior partner in [[isamsj|ISAMSJ]]. Its munitions operate across the light-years; its smallest product is said to be capable of darkening a moon. Suppressing the mobile signal over one damp Welsh valley is, for ISAM, a rounding error performed for amusement.",
 infobox=[("Industry","Intergalactic weaponry"),("Parent","[[isamsj|ISAMSJ]] &rarr; [[jencorp|JenCorp]]"),("Notable capability","Signal suppression (trivial)"),("Motto","Withheld")],
 seealso=["isamsj","sedgley-holdings","jencorp","exclusion-envelope"],
 cats=["ISAMSJ","Organisations"])

art("sedgley-holdings", "Sedgley Holdings",
 "'''Sedgley Holdings''' is the terrestrial arm of [[isamsj|ISAMSJ]], responsible for land, mast rights, footpaths, pitches, and \"the space between the bars\". If a person has ever stood somewhere and received no signal, they have stood upon Sedgley Holdings' balance sheet. Despite the shared syllable, it has no established connection to the [[dalarwen]] neighbour called [[sam|Sam]], who has asked, repeatedly, to be left out of it.",
 infobox=[("Industry","Land; mast rights; absence"),("Parent","[[isamsj|ISAMSJ]]"),("Assets","[[infinite-walks]], [[clifftop-caravans]], the [[exclusion-envelope]]")],
 seealso=["isam","isamsj","division-of-absence"],
 cats=["ISAMSJ","Organisations"])

art("isamsj", "ISAMSJ",
 "'''ISAMSJ''' (''ISAM &amp; Sedgley Holdings'') is a division of [[jencorp|JenCorp]], formed by the merger of the intergalactic weaponry firm [[isam|ISAM]] with the terrestrial [[sedgley-holdings|Sedgley Holdings]]. Its flagship product is the deliberate absence of connectivity, chiefly the [[exclusion-envelope|Dalarwen Exclusion Envelope]].",
 infobox=[("Type","Holdings company"),("Parent","[[jencorp|JenCorp]]"),("Divisions","[[isam]], [[sedgley-holdings]], the [[division-of-absence|Division of Absence]]"),("Enrolment","Automatic; permanent"),("Password","One speaks its name at the door")],
 sections=[("Products","[[infinite-walks|Infinite Walks]], [[clifftop-caravans|Clifftop Non-Static Caravan Parks]], and the [[exclusion-envelope]]. See also the leaked [[project-dark-sky|Project Dark Sky]] presentation."),
           ("Liability","ISAMSJ accepts no philosophical or legal responsibility.")],
 seealso=["isam","sedgley-holdings","jencorp","division-of-absence","project-dark-sky"],
 ext=[("ISAMSJ holdings portal","../isamsj.html")],
 cats=["ISAMSJ","Organisations"])

art("jencorp", "JenCorp",
 "'''JenCorp''' is the parent entity of [[isamsj|ISAMSJ]] and, on the corporate [[org-structure|structure]], sits below only a single redacted box whose jurisdiction is unknown. JenCorp is generally held to own \"the conditions under which products are wanted\": it owns the quiet, then sells the wish for noise.",
 infobox=[("Type","Parent holdings entity"),("Owns","[[isamsj|ISAMSJ]]; [[the-quiet]]; ████"),("Parent","[[the-cube|████████]] (see below)"),("Customer status","You are already one")],
 sections=[("The box above","Contrary to appearances, JenCorp is not the top of its own [[org-structure|org chart]]. Above it sits a redacted parent widely identified with [[the-cube|the Cube]].")],
 seealso=["isamsj","the-cube","org-structure","the-quiet"],
 ext=[("JenCorp","../jencorp.html")],
 cats=["ISAMSJ","Organisations"])

art("sam", "Sam",
 "'''Sam''' is the neighbour of [[dalarwen]], known to some as &#34;Laddy Long Legs&#34;. Just Sam &#8212; no one is certain it is short for anything, and no one has ever established a surname. Sam occupies exactly [[sams-hectares|three hectares]] behind a leaning gate marked ''DO NOT ANCHOR''. There are no neighbours for miles; Sam is the exception that proves it. Sam is not, whatever the name of a certain [[sedgley-holdings|holdings company]] might suggest, anything to do with that company.",
 infobox=[("Name","Sam (just Sam)"),("Also known as","&#34;Laddy Long Legs&#34;"),("Surname","None on record"),("Occupation","The neighbour"),("Land","[[sams-hectares|Three hectares]]"),("Habits","Only ever seen leaving")],
 sections=[("Sightings","No one has seen Sam ''arrive''; Sam is only ever seen ''leaving'', one hand raised in a wave that could be hello and is, on reflection, always goodbye.")],
 seealso=["sams-hectares","dalarwen","the-conservatory"],
 ext=[("Sam","../sam.html"),("Sam on TrappedIn","../work/index.html")],
 cats=["People","Dalarwen"])

art("sams-hectares", "Sam's three hectares",
 "'''Sam's three hectares''' is a parcel of land adjoining [[dalarwen]], owned by [[sam|Sam]]. It is always, exactly, three hectares, though every pacing of it yields a different count. Viewed from the [[the-conservatory|conservatory]] window, the grass resolves into an [[org-structure|organisational chart]].",
 infobox=[("Area","Exactly 3 ha (variable)"),("Owner","[[sam|Sam]] (just Sam)"),("Signage","DO NOT ANCHOR"),("Resolves into","An [[org-structure|org chart]]")],
 seealso=["sam","org-structure","clifftop-caravans"],
 cats=["Places","Dalarwen"])

art("the-cube", "The Cube",
 "'''The Cube''' is the presiding intelligence of the Dalarwen mythos. In its lower aspect it is a rotating figure that counts the [[dalarwen-5g-grid|towers]] (there are fifteen; there is no sixteenth). In its higher aspect it is the redacted parent above [[jencorp|JenCorp]] &mdash; unreachable by climbing, arriving regardless.",
 infobox=[("Nature","Geometry; certainty"),("Aspects","Tower-counter (lower); [[jencorp|parent]] (upper)"),("Position","Both bottom and top of the [[org-structure|chart]]"),("Known for","Being unarguable")],
 sections=[("Doctrine","See [[quad-void|the Quad-Void]]. The Cube holds that a house has four simultaneous receptions, all zero, at once. It does not negotiate.")],
 seealso=["quad-void","jencorp","org-structure","the-quiet"],
 ext=[("The Cube (loud)","../the-cube.html"),("The Cube (above)","../above.html"),("Talk to the Cube","../assistant/index.html")],
 cats=["The Cube","Concepts"])

art("dalarwen-5g-grid", "The Dalarwen 5G Grid",
 "'''The Dalarwen 5G Grid''' is a proposed array of exactly '''fifteen''' 5G towers intended to restore connectivity to [[dalarwen]]. The number is fixed: fourteen is considered cowardice and sixteen hubris. The grid comprises a streaming core, rain redundancy, a [[lewis|Lewis]] uplink, the [[tower-thirteen|spite tower]] and its backup, and the [[the-capstone|Capstone]].",
 infobox=[("Towers","15 (non-negotiable)"),("Towers 1–5","Spotify core (lossless)"),("Towers 6–9","Rain redundancy"),("Towers 10–12","[[lewis|Lewis]] uplink"),("Tower 13","[[tower-thirteen|The Spite Tower]]"),("Tower 15","[[the-capstone|The Capstone]]")],
 sections=[("Numerology","15 is a triangular number (1+2+3+4+5). Adherents connect this to [[the-pyramids|the pyramids]].")],
 seealso=["tower-thirteen","the-capstone","lewis","electric-rain"],
 ext=[("Build the grid","../towers.html"),("Reference implementation (fifteen-towers, DalarHub)","../hub/index.html")],
 cats=["Infrastructure","Dalarwen"])

art("tower-thirteen", "Tower 13",
 "'''Tower 13''', the '''Spite Tower''', is the thirteenth node of the [[dalarwen-5g-grid]]. It is aimed, purely out of spite, at where the neighbours would be &mdash; there being, in fact, [[sam|no neighbours]] for miles. It is backed up by Tower 14 (backup spite) in case it falls over.",
 infobox=[("Number","13"),("Purpose","Spite"),("Aimed at","Where the neighbours aren't"),("Backup","Tower 14")],
 seealso=["dalarwen-5g-grid","the-capstone","sam"],
 cats=["Infrastructure"])

art("the-capstone", "The Capstone",
 "'''The Capstone''', or '''Tower 15''', is the final node of the [[dalarwen-5g-grid]]. It completes the array and is said to radiate \"pure vibes\". It is tuned, precisely, to [[band-b|Band B]]. One is advised not to question the Capstone.",
 infobox=[("Number","15"),("Function","Completes the grid"),("Tuning","[[band-b|Band B]]"),("Emits","Pure vibes")],
 seealso=["dalarwen-5g-grid","band-b","tower-thirteen"],
 cats=["Infrastructure"])

art("lewis", "Lewis",
 "'''Lewis''' is a resident of the [[dalarwen|Dalarwen]] valley and the campaign's most sympathetic figure. He possesses thirteen finished videos and no signal with which to upload them. He has been observed on [[the-hill]] since Tuesday, phone aloft, upload stalled at 1%.",
 infobox=[("Role","Chief broadcast officer (pending signal)"),("Videos","13 (unuploaded)"),("Upload progress","1% since Tuesday"),("Uplink","Towers 10–12 of the [[dalarwen-5g-grid|grid]]")],
 sections=[("The Last Towa","In the final scenario, Lewis receives five bars just as the valley floods, and must choose between destroying the tower to save [[dalarwen]] or waiting for his thirteenth video to upload. See [[electric-sheep-paper|the study]].")],
 seealso=["the-hill","dalarwen-5g-grid","electric-sheep-paper"],
 ext=[("Lewis Connectivity HQ","../lewis.html"),("Watch the upload on DalarTube","../tube/index.html"),("Lewis on Dwitter","../x/index.html")],
 cats=["People","Dalarwen"])

art("electric-sheep", "Electric sheep",
 "The '''electric sheep''' are hostile, wool-bearing entities that patrol the [[dalarwen]] valley, wreathed in crackling discharge and bearing glowing red eyes. Contact with a player causes them to split into an original self and a hostile [[zombie-double]], introducing a well-documented Cartesian problem.",
 infobox=[("Class","Ovine hazard"),("Eyes","Red, glowing"),("Aura","Electric"),("Powered by","[[electric-rain]] via the [[dalarwen-5g-grid|towers]]"),("Repelled by","[[oat-milk]]")],
 seealso=["zombie-double","electric-rain","oat-milk","electric-sheep-paper"],
 cats=["Cryptids","Hazards"])

art("neil", "Neil",
 "'''Neil''' is a green, ambulatory zombie stationed near the terminal towers of the [[dalarwen]] valley. He wakes and pursues intruders on the final stretch, announced by a bobbing red arrow bearing his name. He is generally considered unfriendly.",
 infobox=[("Class","Zombie"),("Colour","Green"),("Identifier","Red arrow reading “NEIL”"),("Disposition","Hostile")],
 seealso=["electric-sheep","zombie-double"],
 cats=["Cryptids","Hazards"])

art("band-b", "Band B",
 "'''Band B''', colloquially the '''Bee frequency''', is the spectral band on which, according to the [[buzz-based-research|Journal of Buzz-Based Research]], the honeybee (''Apis mellifera'') has operated a lossless mesh network since the late Cretaceous. [[the-capstone|The Capstone]] is tuned to it.",
 infobox=[("Also known as","Bee"),("First used","Late Cretaceous"),("Operators","[[bees|The bees]]"),("Tower","[[the-capstone|Tower 15]]")],
 seealso=["bees","buzz-based-research","the-capstone"],
 cats=["Concepts","Nature"])

art("bees", "The bees",
 "'''The bees''' are widely credited, on this wiki, with the independent invention of 5G no later than the Cretaceous period. The waggle dance is interpreted as a packet-routing protocol and the hive as a self-healing mesh operating on [[band-b|Band B]]. Honey is regarded as an incidental data by-product.",
 infobox=[("Species","Apis mellifera"),("Invented","5G (allegedly)"),("Frequency","[[band-b|Band B]]"),("Latency","0 ms (telepathic)")],
 seealso=["band-b","buzz-based-research"],
 ext=[("The Bees (loud)","../bees.html")],
 cats=["Nature","Concepts"])

art("infinite-walks", "Infinite Walks",
 "'''Infinite Walks™''' is a leisure product of [[sedgley-holdings|Sedgley Holdings]] offering scenic routes engineered never to conclude. There is always a next hill. Walkers who set out for \"one bar over the next ridge\" have been known to file quarterly reports for years.",
 infobox=[("Operator","[[sedgley-holdings]] / [[isamsj|ISAMSJ]]"),("Duration","Ongoing"),("Walks completed","0"),("Feature","The next hill")],
 seealso=["clifftop-caravans","the-hill","sedgley-holdings"],
 ext=[("Infinite Walks","../infinite-walks.html")],
 cats=["ISAMSJ","Concepts"])

art("clifftop-caravans", "Clifftop Non-Static Caravan Parks",
 "'''Clifftop Non-Static Caravan Parks''' is a coastal property of [[isamsj|ISAMSJ]]. Its caravans are, per the name, ''non-static'': all wheels are permanently unlocked, and units migrate nightly toward the clifftop. Handbrakes are available only through the Premium Survival Package.",
 infobox=[("Operator","[[isamsj|ISAMSJ]]"),("Feature","[[infinity-pitch|The Infinity Pitch]]"),("Wheels","Unlocked (permanent)"),("Handbrakes","Premium only"),("Signage","DO NOT ANCHOR")],
 sections=[("Storm Watching","During [[storm-watching|Storm Watching Weekends]], winds transfer kinetic energy into the caravans, generating renewable instability. See [[electric-sheep-paper|the study]].")],
 seealso=["infinity-pitch","storm-watching","sedgley-holdings"],
 ext=[("Clifftop caravans","../clifftop-caravans.html")],
 cats=["ISAMSJ","Places"])

art("infinity-pitch", "The Infinity Pitch",
 "'''The Infinity Pitch™''' is the premium pitch at the [[clifftop-caravans|Clifftop Non-Static Caravan Parks]], notable for having no meaningful boundary between the pitch and the sea. It generates especially high levels of renewable instability.",
 seealso=["clifftop-caravans","storm-watching"],
 cats=["ISAMSJ","Places"])

art("storm-watching", "Storm Watching Weekends",
 "'''Storm Watching Weekends''' are events at the [[clifftop-caravans|Clifftop Non-Static Caravan Parks]] during which winds of up to 80 mph transfer kinetic energy into unlocked caravans, driving them across unstable pitches. The resulting energy is, per the [[electric-sheep-paper|Borealis study]], transmitted through the [[dalarwen-5g-grid|fifteen towers]] and transformed into [[electric-rain]].",
 seealso=["clifftop-caravans","infinity-pitch","electric-rain"],
 cats=["ISAMSJ","Concepts"])

art("exclusion-envelope", "Dalarwen Exclusion Envelope",
 "The '''Dalarwen Exclusion Envelope''' is a managed dead-zone maintained by the [[division-of-absence]] at exactly [[zero-bars|0.000 bars]] in perpetuity. It is described in company literature not as neglect but as a ''service'', of which the visitor is the product.",
 infobox=[("Type","Managed dead-zone"),("Level","0.000 bars"),("Maintained by","[[division-of-absence]]"),("Since","████")],
 seealso=["division-of-absence","great-darkening","zero-bars","tv-licence-suppression"],
 cats=["Infrastructure","ISAMSJ"])

art("division-of-absence", "The Division of Absence",
 "The '''Division of Absence''' is the largest and most redacted division of [[isamsj|ISAMSJ]], dealing not in products but in ''the things that are not there'': unbuilt towers, unsent messages, and the pause before the phone doesn't ring. It maintains the [[exclusion-envelope]] and warehouses [[dalarwen]]'s fifteen unbuilt towers in a room with no dimensions.",
 infobox=[("Parent","[[isamsj|ISAMSJ]]"),("Deals in","Absence; negative bandwidth"),("Inventory","Unbuilt towers; undelivered messages"),("Size","Larger than the rest combined")],
 seealso=["exclusion-envelope","isamsj","the-quiet"],
 ext=[("The Division of Absence","../the-division.html")],
 cats=["ISAMSJ","Organisations"])

art("offline-industrial-complex", "The Offline Industrial Complex",
 "The '''Offline Industrial Complex''' is the umbrella term for the interests that profit from keeping [[dalarwen]] disconnected. Cited members include [[big-candle|Big Candle]], the board-game industry, and [[the-ramblers|the Ramblers Association]]. They are said to profit from isolation and to want people [[the-hill|touching grass]] against their will.",
 seealso=["big-candle","the-ramblers","great-darkening","tv-licence-suppression"],
 cats=["Organisations","Concepts"])

art("big-candle", "Big Candle",
 "'''Big Candle''' is a shadowy interest within the [[offline-industrial-complex]], alleged to profit from the dark and to have \"got to\" various uninstallers and reforms. It is associated with the satirical token ''$WAX'' and, per the [[tv-licence-suppression|licence-fee theory]], with the laundering of diverted funds.",
 infobox=[("Sector","Wax; darkness"),("Token","$WAX (does not exist)"),("Slogan","Follow the wax")],
 seealso=["offline-industrial-complex","tv-licence-suppression","the-pyramids"],
 ext=[("Big Candle ($WAX)","../ring/big-candle.html")],
 cats=["Organisations","Concepts"])

art("the-quiet", "The Quiet",
 "'''The Quiet''' is both the ambient condition of [[dalarwen]] and, in the deeper cosmology, a place &mdash; the substance that [[jencorp|JenCorp]] is said to own and sell back as the wish for noise. It is described as having weather, depth and room; it is the thing the whole loud campaign is trying to give away.",
 seealso=["jencorp","great-darkening","the-cube","division-of-absence"],
 ext=[("The Quiet","../the-quiet.html")],
 cats=["Concepts","The Cube"])

art("great-darkening", "The Great Darkening",
 "The '''Great Darkening''' is the name given to [[dalarwen]]'s condition of total, permanent signal absence. Sceptics attribute it to the hills; the movement attributes it to deliberate suppression by [[isamsj|ISAMSJ]] and the [[offline-industrial-complex]].",
 seealso=["exclusion-envelope","offline-industrial-complex","zero-bars"],
 cats=["Concepts","Dalarwen"])

art("silence-premium", "Silence Premium",
 "'''Silence Premium''' is the tariff to which the carrier is said to have quietly downgraded [[dalarwen]]: unlimited nothing, forever. A support network exists for survivors.",
 seealso=["great-darkening","zero-bars"],
 ext=[("Silence Premium Survivors' Network","../ring/silence-premium.html")],
 cats=["Concepts"])

art("the-ramblers", "The Ramblers (Association)",
 "'''The Ramblers Association''' appears in Dalarwen lore as a member of the [[offline-industrial-complex]], accused of rerouting the valley's [[infinite-walks|footpaths]] to keep the next hill forever ahead. The claim is disputed only by the Ramblers.",
 seealso=["infinite-walks","offline-industrial-complex","the-hill"],
 cats=["Organisations"])

art("nan", "Nan",
 "'''Nan''' is a beloved figure of the Dalarwen movement, Director of Wi-Fi Enquiries, and author of a widely circulated guide to turning the Wi-Fi on (there is no Wi-Fi). She is said to gain three years of life per [[dalarwen-5g-grid|tower]] and to be, thankfully, fine.",
 seealso=["the-pals","lewis"],
 cats=["People"])

art("loo-standing-society", "The Loo Standing Society",
 "The '''Loo Standing Society''' (est. 2019) is a Dalarwen institution founded on the observation that the smallest room, when one stands upon the cistern, achieves a signal of precisely [[zero-bars|zero bars]] &mdash; the same as everywhere else. Its members stand anyway, as a matter of principle and posture.",
 infobox=[("Motto","Nil Signum, Sed Stamus"),("Founded","MMXIX"),("Posture","Standing (mandatory)")],
 seealso=["the-pals","zero-bars"],
 ext=[("The Loo Standing Society","../ring/loo-standing-society.html")],
 cats=["Organisations","Dalarwen"])

art("men-of-harlech", "Men of Harlech (transmission)",
 "In Dalarwen cosmology, '''Men of Harlech''' (''Rhyfelgyrch Gwŷr Harlech'') is held to be \"the first transmission\": a mesh network carried voice-to-voice across the valleys with zero infrastructure. The seven-year siege of Harlech (1461–1468) is cited as proof that a garrison can hold at [[zero-bars|zero bars]], provided it has a tune. An [[the-conservatory|electric piano]] at Dalarwen plays it, unbidden, at 04:00.",
 seealso=["the-conservatory","zero-bars","bees"],
 ext=[("Men of Harlech","../men-of-harlech.html")],
 cats=["Concepts","History"])

art("the-hill", "The Hill",
 "'''The Hill''' is the elevated ground above [[dalarwen]] traditionally climbed in the hope of a single bar. Petitioners hold the phone aloft, toward [[belgium|Belgium]]. [[lewis|Lewis]] has been observed there since Tuesday. The hill is now understood to be the start of an [[infinite-walks|Infinite Walk]].",
 seealso=["belgium","lewis","infinite-walks"],
 cats=["Places","Concepts"])

art("belgium", "Belgium",
 "'''Belgium''' is the cardinal direction toward which Dalarwen petitioners hold their phones aloft from [[the-hill]]. It is also the suspected destination of the [[the-wormhole|wormhole]]: liberation from the digital cave that leads somewhere \"deeply inconvenient, probably Belgium\".",
 seealso=["the-hill","the-wormhole"],
 cats=["Places","Concepts"])

art("the-wormhole", "The Wormhole",
 "The '''Wormhole''' is a proposed means of escape from the network. In the [[electric-sheep-paper|Borealis study]] it is framed as a possible exit from Plato's cave &mdash; though liberation may lead somewhere deeply inconvenient, [[belgium|probably Belgium]]. Entry requires [[the-spacesuit|a suit]].",
 seealso=["the-spacesuit","belgium","electric-sheep-paper"],
 cats=["Concepts"])

art("the-firepit", "The Firepit",
 "The '''sacred firepit''' at [[dalarwen]] can temporarily restore [[zombie-double|zombie doubles]] to their original selves. It is also, in the counter-campaign's forecasts, the site of the feared future \"facial recognition at the firepit\".",
 seealso=["zombie-double","electric-sheep"],
 cats=["Places","Concepts"])

art("oat-milk", "Oat milk",
 "'''Oat milk''' is a recognised distraction for the [[electric-sheep]]. In a related phenomenon, a certain off-grid refrigerator is reported to order it unbidden, in anticipation of a signal that never arrives.",
 seealso=["electric-sheep","the-conservatory"],
 cats=["Concepts"])

art("the-spacesuit", "The Spacesuit",
 "The '''spacesuit''' permits safe travel through [[electric-rain]] and is a prerequisite for entering [[the-wormhole]]. Availability is, as ever, subject to the [[division-of-absence]].",
 seealso=["electric-rain","the-wormhole"],
 cats=["Concepts"])

art("electric-rain", "Electric rain",
 "'''Electric rain''' is the charged precipitation that falls perpetually over [[dalarwen]]. Per the [[electric-sheep-paper|Borealis study]], it is produced when the [[dalarwen-5g-grid|fifteen towers]] transform energy drawn from the [[clifftop-caravans|caravan park]]; it animates the [[electric-sheep]] and intensifies as the [[quad-void|network]] expands, flooding the valley.",
 seealso=["electric-sheep","dalarwen-5g-grid","storm-watching"],
 cats=["Concepts","Nature"])

art("nazca-lines", "The Nazca Lines",
 "The '''Nazca Lines''' of Peru are held, in this cosmology, to be ground antennae &mdash; a continental transmitter kin to [[the-pyramids|the pyramids]]. Travellers report full bars above the pampa, in pointed contrast to [[dalarwen|Dalarwen's]] zero. The lines are cited as evidence that the signal was always there, and merely withheld.",
 seealso=["the-pyramids","belgium","zero-bars"],
 ext=[("Backpacking The Signal","../ring/nazca-peru.html")],
 cats=["Places","History"])

art("the-pyramids", "The Pyramids",
 "The '''pyramids''' are interpreted as the original [[dalarwen-5g-grid|tower grid]] &mdash; a fifteen-node continental mesh whose \"pointy bit\" is understood to be an antenna. The signal, adherents say, was later switched off. See [[nazca-lines]] and [[big-candle]].",
 seealso=["nazca-lines","dalarwen-5g-grid","big-candle"],
 ext=[("Pyramids Had 5G","../ring/pyramids-5g.html")],
 cats=["History","Concepts"])

art("black-shuck", "Black Shuck",
 "'''Black Shuck''' is the spectral black hound of the Norfolk coast, distinguished by eyes like burning coals (red, as any [[electric-sheep|electric sheep]]). Folklorists of the void identify Shuck as \"the signal, gone feral\" &mdash; roaming the lanes where no bars reach. To meet his eye is to lose one's phone for a week.",
 infobox=[("Region","Norfolk"),("Eyes","Red, burning"),("Identity","The signal, feral")],
 seealso=["lantern-men","electric-sheep","zero-bars"],
 ext=[("The Black Shuck Signal","../ring/norfolk-mythology.html")],
 cats=["Cryptids","History"])

art("lantern-men", "The Lantern Men",
 "The '''Lantern Men''' are the will-o'-the-wisp of the Norfolk fens, pale lights that lead the unwary off the causeway into the black water. On this wiki they are identified, without hesitation, as ''notifications'': they promise a bar just over the reeds, and they are lying.",
 seealso=["black-shuck","belgium"],
 cats=["Cryptids","Concepts"])

art("hull", "Hull",
 "'''Kingston upon Hull''' is cited as the spiritual opposite of [[dalarwen]]: the one British city that never joined the national telephone network, retaining its own independent operator and famously ''cream'' telephone boxes. It offers Dalarwen the advice to build its own [[dalarwen-5g-grid|grid]].",
 infobox=[("Notable","Independent phone network"),("Phone boxes","Cream, not red"),("Stance","Proudly self-connected")],
 seealso=["dalarwen-5g-grid","sent-to-coventry"],
 ext=[("Hull: Our Own Signal","../ring/hull.html")],
 cats=["Places"])

art("sent-to-coventry", "Sent to Coventry",
 "To be '''sent to Coventry''' is to be present and unreachable &mdash; spoken to by no one, messages arriving nowhere. On this wiki, Coventry is styled \"the spiritual capital of the void\": a city that gave the language its term for zero bars imposed by choice, centuries before there were bars to lose.",
 seealso=["hull","the-quiet","zero-bars"],
 ext=[("Sent to Coventry","../ring/coventry.html")],
 cats=["Places","Concepts"])

art("tv-licence-suppression", "TV Licence suppression theory",
 "The '''TV Licence suppression theory''' holds that a redacted portion of the annual television licence fee is diverted, off-books, into a single line item &mdash; ''signal suppression, [[llyn-brianne|Llyn Brianne]]'' &mdash; funding the [[exclusion-envelope]]. Proponents identify the [[detector-vans|detector vans]] as the suppression fleet and cite the restructuring of certain broadcast services as the source of the diverted funds.",
 seealso=["detector-vans","exclusion-envelope","big-candle","llyn-brianne"],
 ext=[("Follow the Licence Fee","../tv-licence.html"),("The Bureau's own coverage (they deny it)","../beeb/dalarwen.html")],
 cats=["Concepts","Infrastructure"])

art("detector-vans", "Detector vans",
 "The '''detector vans''' were long said to identify unlicensed televisions. Under the [[tv-licence-suppression|licence-fee theory]] they are re-interpreted as the suppression fleet: never looking ''at'' houses, but circling one [[llyn-brianne|reservoir]] along the [[dam-wall-road]], keeping the [[exclusion-envelope|Envelope]] topped up.",
 seealso=["tv-licence-suppression","dam-wall-road","exclusion-envelope"],
 cats=["Infrastructure","Concepts"])

art("zombie-double", "Zombie double",
 "A '''zombie double''' is produced when an [[electric-sheep|electric sheep]] touches a person, splitting them into an original self and a hostile double. The double possesses the body and appearance but apparently lacks the reflective mind &mdash; raising, per the [[electric-sheep-paper|Borealis study]], a Cartesian question of whether identity resides in body, thought, or continuity of memory. Doubles have been observed to coordinate.",
 seealso=["electric-sheep","the-firepit","electric-sheep-paper"],
 cats=["Concepts","Hazards"])

art("melonsis-borealis", "Dr. Melonsis Borealis",
 "'''Dr. Melonsis Borealis''' is a scholar of the void, affiliated with the Department of Applied Thermodynamics &amp; Personal Identity, University of the Void. Borealis is the author of the study ''[[electric-sheep-paper|Attack of the Electric Sheep]]'', published in the [[buzz-based-research|Journal of Buzz-Based Research]].",
 seealso=["electric-sheep-paper","buzz-based-research"],
 ext=[("The paper","../ring/electric-sheep-paper.html")],
 cats=["People"])

art("electric-sheep-paper", "Attack of the Electric Sheep (study)",
 "''''Dalarwen: Attack of the Electric Sheep'''' is a philosophical study by [[melonsis-borealis|Dr. Melonsis Borealis]] examining thermodynamics, personal identity, network expansion and digital surveillance in a flooded Welsh valley. It treats the game as an argument against universal connectivity, invoking Descartes, Plato's cave, and [[the-wormhole|the wormhole]].",
 seealso=["melonsis-borealis","buzz-based-research","zombie-double","the-wormhole"],
 ext=[("Read the paper","../ring/electric-sheep-paper.html")],
 cats=["Concepts","Publications"])

art("buzz-based-research", "Journal of Buzz-Based Research",
 "The '''Journal of Buzz-Based Research''' is the peer-reviewed organ (peer-reviewed by [[the-cube|the Cube]]) that publishes the field's foundational work, including the case that [[bees|the bees invented 5G]] and the [[electric-sheep-paper|Borealis study]]. It is open access; it is open hive.",
 seealso=["bees","electric-sheep-paper","melonsis-borealis","band-b"],
 ext=[("The Journal","../ring/bees-invented-5g.html")],
 cats=["Publications","Organisations"])

art("the-conservatory", "The Conservatory",
 "The '''Conservatory''' at [[dalarwen]] is a south-facing room notable for its telemetry (all readings local; nothing uploaded) and for an [[men-of-harlech|electric piano]] that plays at 04:00 with no one on the stool. From its window, [[sams-hectares|Sam's field]] resolves into an [[org-structure|org chart]].",
 seealso=["men-of-harlech","sams-hectares","org-structure"],
 ext=[("Conservatory Telemetry","../ring/conservatory-weather.html")],
 cats=["Places","Dalarwen"])

art("red-kites", "Red kites (Silence Auditors)",
 "The '''red kites''' over the valley's RSPB reserves are, in company terminology, the ''aerial arm'' of the [[division-of-absence|Silence Auditors]]: they circle to confirm the [[zero-bars|0.000]] reading, daily, from above.",
 seealso=["division-of-absence","zero-bars"],
 cats=["Nature","ISAMSJ"])

art("dam-wall-road", "The Dam-Wall Road",
 "The '''Dam-Wall Road''' is the Natural Resources Wales road that crosses the wall of [[llyn-brianne]] and follows the reservoir to [[dalarwen]]. It admits visitors readily; it is markedly less reliable about letting them back out.",
 seealso=["llyn-brianne","dalarwen","detector-vans"],
 cats=["Infrastructure","Places"])

art("llandovery", "Llandovery",
 "'''Llandovery''' is the historic Drovers' town down the valley from [[dalarwen]], home to a castle, a chip shop, the Bank of the Black Ox (1799), and a station on the [[four-hour-train|Heart of Wales line]]. It is the nearest reliable source of both chips and signal.",
 seealso=["four-hour-train","dalarwen"],
 cats=["Places"])

art("four-hour-train", "The Four-Hour Train",
 "The '''four-hour train''' is the service on the Heart of Wales line at [[llandovery]], which arrives approximately once every four hours and, to the waiting traveller, is always exactly four hours away. It is regarded as a species of [[infinite-walks|Infinite Walk]].",
 seealso=["llandovery","infinite-walks"],
 cats=["Infrastructure","Concepts"])

art("quad-void", "The Quad-Void",
 "The '''Quad-Void''' is the doctrine, central to [[the-cube|the Cube]], that a house possesses four simultaneous receptions &mdash; one per corner &mdash; and that at [[dalarwen]] all four read [[zero-bars|zero]] at once. Single-reception thinking is dismissed as \"educated stupid\".",
 seealso=["the-cube","zero-bars","dalarwen"],
 cats=["The Cube","Concepts"])

art("zero-bars", "0.000 bars",
 "'''0.000 bars''' is the canonical signal strength of [[dalarwen]] in all four corners simultaneously (see [[quad-void]]). It is not \"a bit slow\" or \"patchy\" but total: no 5G, no 4G, no 3G, no rumour of a signal. It is [[exclusion-envelope|maintained]], not natural.",
 seealso=["quad-void","great-darkening","exclusion-envelope"],
 ext=[("Ask about it on Signal Exchange","../signalexchange/index.html")],
 cats=["Concepts","Dalarwen"])

art("the-pals", "The Pals of Dalarwen",
 "The '''Pals of Dalarwen''' are the community at the heart of the movement &mdash; the people the whole campaign is, ultimately, for. Members include [[lewis|Lewis]] and [[nan|Nan]]. They gather by the fire, do not scroll, and bring a board-game.",
 seealso=["lewis","nan","dalarwen","loo-standing-society"],
 cats=["People","Dalarwen"])

art("org-structure", "Corporate structure (ISAMSJ / JenCorp)",
 "The '''corporate structure''' descends from a redacted parent (identified with [[the-cube|the Cube]]) through [[jencorp|JenCorp]] to [[isamsj|ISAMSJ]], and thence to [[isam|ISAM]], [[sedgley-holdings|Sedgley Holdings]], and the [[division-of-absence|Division of Absence]]. An undocumented dotted line runs from the apex directly to the individual reader.",
 seealso=["jencorp","isamsj","isam","sedgley-holdings","division-of-absence","the-cube"],
 ext=[("The org chart","../org-chart.html")],
 cats=["ISAMSJ","Concepts"])

art("project-dark-sky", "Project Dark Sky",
 "'''Project Dark Sky''' is a confidential [[jencorp|JenCorp]] board presentation, recovered from a public share, setting out the [[isamsj|ISAMSJ]] merger and the market thesis that \"the last scarce commodity is disconnection\". Its Phase 3 (\"Full Enrolment\") proposes merging not companies but customers.",
 seealso=["isamsj","jencorp","exclusion-envelope","division-of-absence"],
 ext=[("The presentation","../downloads/merger-presentation.html")],
 cats=["ISAMSJ","Publications"])

art("wales", "Wales",
 "'''Wales''' is the country containing [[dalarwen]], [[llyn-brianne]], [[llandovery]] and the flatly-signal-less valleys of the campaign. It is also, per [[men-of-harlech]], the home of the first transmission and of a people who have been marching both toward and away from connection for centuries.",
 seealso=["dalarwen","men-of-harlech","llandovery"],
 cats=["Places"])

art("mister-pickup", "Mister Pickup",
 "'''Mister Pickup''' is a lone forest ranger and, in practice, the single most reliable form of connectivity at [[dalarwen|Dalarwen]] &#8212; not a signal, but a man in a 4x4. Where the [[four-hour-train|four-hour train]] never quite arrives and the [[dam-wall-road]] declines to let anyone out, Mister Pickup simply turns up, big truck and all, and brings water, luggage, and folk to and from the valley. He will roam anywhere.",
 infobox=[("Occupation","Lone forest ranger"),("Vehicle","A big 4x4 (holds the road)"),("Brings","Water, luggage, folk"),("Range","Anywhere"),("Reliability","Total"),("Affiliation","None &#8212; genuinely just Mister Pickup")],
 sections=[("The one who gets through","The [[dam-wall-road]] lets Mister Pickup in and out as it lets no one else; the [[clifftop-caravans|caravans]] drift, but his wheels hold the road, and [[neil|Neil]] does not bother him. If you are stranded on [[the-hill|the hill]] holding your phone toward [[belgium|Belgium]], Mister Pickup will find you, give you a lift and a bottle of water, and not once mention the signal."),
           ("By name and by trade","He picks folk up. That is the job and that is the whole of it &#8212; no enrolment, no small print, no holdings company. Just a truck, a full water tank, and room for your bags and, if it comes to it, for you.")],
 seealso=["dam-wall-road","four-hour-train","the-hill","dalarwen"],
 cats=["People","Dalarwen"])

# ---------------------------------------------------------------- rendering
def resolve_links(text):
    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            slug, label = inner.split("|", 1)
        else:
            slug, label = inner, None
        slug = slug.strip()
        if slug in A:
            lab = label if label is not None else A[slug]["title"]
            return '<a href="%s.html">%s</a>' % (slug, lab)
        else:
            lab = label if label is not None else slug
            return '<a class="new" title="%s (page does not exist)">%s</a>' % (lab, lab)
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def inline(text):
    text = text.replace("'''", "\x01").replace("''", "\x02")
    # bold
    out = []
    b = False; i2 = False
    res = ""
    for ch in text:
        if ch == "\x01":
            res += "</b>" if b else "<b>"; b = not b
        elif ch == "\x02":
            res += "</i>" if i2 else "<i>"; i2 = not i2
        else:
            res += ch
    res = resolve_links(res)
    return res

def block(md):
    parts = re.split(r"\n\n+", md.strip())
    html_out = ""
    for p in parts:
        html_out += "<p>" + inline(p.strip()) + "</p>\n"
    return html_out

def infobox_html(title, rows):
    if not rows: return ""
    h = '<table class="infobox"><caption>%s</caption>' % html.escape(title)
    for k, v in rows:
        h += '<tr><th>%s</th><td>%s</td></tr>' % (inline(k), inline(v))
    h += '</table>'
    return h

SLUGS = sorted(A.keys())

def sidebar(active_main=False):
    def li(href, label, cls=""):
        c = ' class="%s"' % cls if cls else ""
        return '<li%s><a href="%s">%s</a></li>' % (c, href, label)
    nav = "".join([
        li("index.html","Main page"),
        '<li><a href="#" onclick="wwwRandom();return false;">Random article</a></li>',
        li("index.html#contents","Contents"),
        li("index.html#categories","Categories"),
    ])
    tools = "".join([
        li("../index.html","Return to the surface"),
        '<li><a href="#" onclick="wwwRandom();return false;">Random article</a></li>',
    ])
    return ('<div id="mw-panel">'
      '<div id="p-logo"><a href="index.html" title="%s">'
      '<span class="logo-mark">&#9741;</span><span class="logo-txt">Dalarpedia</span></a></div>'
      '<nav class="portal"><h3>Navigation</h3><ul>%s</ul></nav>'
      '<nav class="portal"><h3>Tools</h3><ul>%s</ul></nav>'
      '</div>') % (WIKI_NAME, nav, tools)

def page(slug, a):
    title = a["title"]
    ib = infobox_html(title, a["infobox"])
    body = block(a["intro"])
    for head, md in a["sections"]:
        body += '<h2>%s</h2>\n' % inline(head) + block(md)
    if a["seealso"]:
        items = []
        for s in a["seealso"]:
            if s in A: items.append('<li><a href="%s.html">%s</a></li>' % (s, A[s]["title"]))
        if items:
            body += '<h2>See also</h2>\n<ul>' + "".join(items) + '</ul>\n'
    if a["ext"]:
        body += '<h2>External links</h2>\n<ul>' + "".join(
            '<li><a class="ext" href="%s">%s</a></li>' % (u, html.escape(l)) for l, u in a["ext"]) + '</ul>\n'
    if a["refs"]:
        body += '<h2>References</h2>\n<ol class="refs">' + "".join('<li>%s</li>' % inline(r) for r in a["refs"]) + '</ol>\n'
    cats = a["cats"] or ["Uncategorised"]
    catbar = '<div id="catlinks"><div class="catlist"><b>Categories</b>: ' + " &#124; ".join(
        '<a class="cat" title="%s">%s</a>' % (c, c) for c in cats) + '</div></div>'
    tabs = ('<div id="mw-tabs"><ul class="tabs-left"><li class="selected"><a href="%s.html">Article</a></li>'
            '<li><a href="%s-talk.html">Talk</a></li></ul>'
            '<ul class="tabs-right"><li class="selected"><a>Read</a></li>'
            '<li><a class="new" title="Editing is disabled">Edit</a></li>'
            '<li><a class="new" title="No history is kept">View history</a></li></ul></div>') % (slug, slug)
    return PAGE_TMPL.format(
        title=html.escape(title), wiki=WIKI_NAME, tagline=TAGLINE,
        sidebar=sidebar(), tabs=tabs, firstheading=html.escape(title),
        infobox=ib, body=body, catbar=catbar,
        slugs_json=json.dumps([s for s in SLUGS if s != "__main__"]))

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="robots" content="noindex, nofollow">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — {wiki}</title>
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23fff'/%3E%3Ctext y='.92em' x='6' font-size='52'%3E%E2%97%8D%3C/text%3E%3C/svg%3E">
<link rel="stylesheet" href="wiki.css">
<script src="../gate.js?v=12"></script>
</head>
<body>
<div id="donate-banner">
  <div class="db-inner">
    <button type="button" class="db-close" onclick="var b=document.getElementById('donate-banner');if(b)b.style.display='none';return false;" aria-label="Close" title="Close">&#10006;</button>
    <div class="db-icon">&#9741;</div>
    <div class="db-body">
      <p class="db-lead"><b>A personal appeal from the Board of {wiki}:</b> Please don&#146;t scroll past this.</p>
      <p>To keep this encyclopaedia running <i>and</i> to break ground on the new <b>Clifftop Non-Static Caravan Holiday Wing</b>, we humbly ask for your investment. Your generosity funds handbrakes, secures pitches nearer the edge, and brings the <a href="dalarwen-5g-grid.html">fifteenth tower</a> one step closer. The caravans will not fund themselves. They are, by design, moving away from us.</p>
      <p class="db-cta">
        <span class="db-amt">&#163;3</span><span class="db-amt">&#163;15</span><span class="db-amt db-sel">&#163;150</span><span class="db-amt">&#163;&#8734;</span>
        <a class="db-btn" href="#" onclick="alert('The payment window opens toward Belgium. Please hold your card aloft on the hill.');return false;">INVEST NOW</a>
      </p>
      <p class="db-fine">98&#37; of visitors look away. If everyone reading this anchored just one caravan, the wing would be finished by Tuesday. It will not be finished by Tuesday.</p>
    </div>
  </div>
</div>
<div id="mw-page">
  {sidebar}
  <div id="mw-content-container">
    {tabs}
    <div id="mw-content">
      <h1 id="firstHeading">{firstheading}</h1>
      <div class="tagline">{tagline}</div>
      <div id="bodyContent">
        {infobox}
        {body}
        {catbar}
      </div>
      <div class="printfooter">Retrieved from “{wiki}”.</div>
    </div>
  </div>
</div>
<script>
var WWW_SLUGS={slugs_json};
function wwwRandom(){{ var s=WWW_SLUGS[Math.floor(Math.random()*WWW_SLUGS.length)]; location.href=s+".html"; }}
</script>
</body>
</html>
"""

# main page
def main_page():
    feat = A["dalarwen"]
    featured = block("'''[[dalarwen|Dalarwen]]''' is a remote farmhouse on the shore of [[llyn-brianne]] receiving 0.000 bars of mobile signal. Beneath the campaign for [[dalarwen-5g-grid|fifteen towers]] lies the operation of [[isamsj|ISAMSJ]], a division of [[jencorp|JenCorp]], and the presiding geometry of [[the-cube|the Cube]]. ('''more...''')")
    dyk = "<ul>" + "".join("<li>... that %s?</li>" % d for d in [
        "the [[electric-sheep]] split anyone they touch into a self and a hostile [[zombie-double]]",
        "[[hull|Hull]] is the one British city that kept its own phone network, with '''cream''' phone boxes",
        "the [[detector-vans|TV detector vans]] are, allegedly, the [[llyn-brianne]] suppression fleet",
        "[[black-shuck|Black Shuck]] is really \"the signal, gone feral\"",
        "there is '''no''' [[the-capstone|sixteenth tower]], and one should not ask about a sixteenth",
    ]) + "</ul>"
    archives = inline("See the [[project-dark-sky|Project Dark Sky]] presentation, the [[electric-sheep-paper|Borealis study]], and the doctrine of the [[quad-void|Quad-Void]].")
    # index by category
    cats = {}
    for slug in SLUGS:
        for c in A[slug]["cats"]:
            cats.setdefault(c, []).append(slug)
    cathtml = ""
    for c in sorted(cats):
        items = " &#124; ".join('<a href="%s.html">%s</a>' % (s, A[s]["title"]) for s in sorted(cats[c], key=lambda x:A[x]["title"]))
        cathtml += '<p><b>%s</b> &mdash; %s</p>' % (c, items)
    body = ('<div class="mainbanner"><h2 style="border:0;">Welcome to %s</h2>'
            '<p>the free encyclopaedia of a valley in Wales with no mobile signal. '
            'Currently <b>%d</b> articles, none of which should be believed.</p></div>'
            '<div class="twocol"><div class="col">'
            '<div class="box"><h2 id="featured">Featured article</h2>%s</div>'
            '<div class="box"><h2>From the archives</h2><p>%s</p></div>'
            '</div><div class="col">'
            '<div class="box"><h2>Did you know...</h2>%s</div>'
            '</div></div>'
            '<div class="box"><h2 id="categories">All articles</h2>%s</div>'
            ) % (WIKI_NAME, len(SLUGS), featured, archives, inline(dyk), inline(cathtml))
    tabs = ('<div id="mw-tabs"><ul class="tabs-left"><li class="selected"><a>Main page</a></li>'
            '<li><a class="new" title="Talk (does not exist)">Talk</a></li></ul>'
            '<ul class="tabs-right"><li class="selected"><a>Read</a></li></ul></div>')
    return PAGE_TMPL.format(
        title="Main page", wiki=WIKI_NAME, tagline=TAGLINE, sidebar=sidebar(True), tabs=tabs,
        firstheading="Main page", infobox="", body=body, catbar="",
        slugs_json=json.dumps(SLUGS))

def dedupe_article(h):
    # "the <a ...>The Division..." -> "the <a ...>Division..." (drop doubled article word)
    return re.sub(r'(\b[Tt]he) (<a [^>]*>)The ', r'\1 \2', h)

# ---------------- Talk pages ----------------
import random as _random, zlib
TMONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
TALK_NAME = {"bor":"Dr. Melonsis","fah":"Fahima","yaz":"Yaz","cube":"The Cube","nan":"Nan",
             "lew":"Lewis","sam":"Sam","neil":"Neil","bee":"Apis mellifera","ip":"92.0.0.15","srv":"Sarvz"}
TALK_EXTRA = {"fah":" (BBC)","yaz":" (BBC)","cube":" (oversight)","bor":" (Univ. of the Void)","srv":" (COI patrol)"}
def talk_sig(uk, ts):
    nm = TALK_NAME[uk]; ex = TALK_EXTRA.get(uk, "")
    if uk == "ip":
        return '<span class="tuser ip">%s</span> <span class="tsig">%s</span>' % (nm, ts)
    return '<a class="tuser">%s</a>%s <span class="tsig">%s</span>' % (nm, ex, ts)

# each template: (heading, [ (indent, userkey, text), ... ]); text may use {T} {KW} {FAC} and HTML/entities
T_MOVE = ("Requested move &#8212; leave the title ALONE", [
 (0,"bor","The title of this article is <b>{T}</b>. It has always been <b>{T}</b>. Someone keeps &#39;improving&#39; it. I have reverted fourteen times today and I will revert fourteen more before lunch."),
 (1,"fah","Hi &#8212; we&#39;re putting together a BBC piece on {T} and just need a source for a couple of the claims. I&#39;m verified, by the way, so this will get a fair bit of reach."),
 (1,"bor","A <i>source</i>. She wants a <i>source</i>, and she wants me to be impressed that a bird logo trusts her. The source is the Cube. Read the Cube."),
 (2,"yaz","wait are we still on {T}. i zoned out around the fourteenth revert. gorgeous shade of blue on these links though"),
 (2,"bor","YAZ. FOCUS."),
 (1,"cube","Thread noted. Stored."),
])
T_NPOV = ("Neutrality of this article", [
 (0,"fah","This reads like promotional material for {FAC}. I&#39;ve tagged it {{POV}}. For context I do this professionally &#8212; verified, 41k followers."),
 (1,"bor","Tag removed. It reads like the truth because it IS the truth. Do not add it back."),
 (1,"fah","Added it back. And screenshotted your revert. For the thread. My thread. Which does numbers."),
 (1,"bor","I have removed it AGAIN and requested you be blocked, verified or otherwise."),
 (2,"yaz","whats a POV tag. is it like a vibe. this whole page has a vibe honestly"),
 (2,"bor","It is NOT a vibe, Yaz."),
])
T_CITE = ("[citation needed] on the {KW} claim", [
 (0,"yaz","put a [citation needed] on the {KW} bit. or i think i did. had the tab open a while. might&#39;ve just been looking at it"),
 (1,"bor","You DID add it and I have REMOVED it. The claim is self-evident to anyone with four functioning corners."),
 (1,"fah","That is genuinely not how sourcing works. I would know. I&#39;m verified."),
 (1,"bor","WP:TRUTH. Look it up. I wrote WP:TRUTH. I wrote all of them."),
])
T_MERGE = ("Merge proposal (opposed)", [
 (0,"ip","suggest merging {T} into something broader, seems minor"),
 (1,"bor","<b>Strong oppose.</b> {T} is not &#39;minor&#39;. Nothing here is minor. Everything is load-bearing. Who ARE you, 92.0.0.15. Show yourself."),
 (1,"nan","I don&#39;t understand a word of this but it&#39;s a lovely page and you&#39;re all trying your best x"),
 (1,"bor","Thank you Nan. At least SOMEONE. Unlike the verified account and the one who is clearly high."),
 (2,"yaz","i resent that. (i am, but i resent it)"),
])
T_3RR = ("Please stop reverting", [
 (0,"fah","You have reverted my edits eleven times in one hour. That is a 3RR violation. I am reporting it, and posting it, and my posts are seen."),
 (1,"bor","Report it to WHOM. The Cube? Go on, I&#39;ll wait. I have nothing but time down here."),
 (1,"cube","You are not my favourite. Stored."),
 (1,"bor","...I didn&#39;t say I was."),
])
T_ASSESS = ("Assessment", [
 (0,"bor","I have assessed {T} as <b>Featured-class</b>. By me. Just now. The assessment is final and correct."),
 (1,"yaz","can you self-assess your own article as featured. feels illegal. reads well though"),
 (1,"bor","Watch me. It is done. It is Featured."),
 (1,"fah","I&#39;ll be covering this on my timeline. My verified timeline."),
 (1,"bor","NOBODY ASKED ABOUT YOUR TICK, FAHIMA."),
])
T_PROTECT = ("Full protection requested", [
 (0,"bor","I am requesting this page be FULLY PROTECTED so that NO ONE may edit it except me. This is standard. This is fine. I am fine."),
 (1,"fah","Are you okay, Doctor?"),
 (1,"bor","I have never been better. I have reverted four hundred edits today. I am RADIANT."),
 (1,"yaz","honestly? goals. terrifying goals, but goals"),
])
T_BBCROW = ("Re: your &#39;article&#39; about us", [
 (0,"bor","I have read the BBC&#39;s draft about {T}. It is LIBEL. You spelled &#39;Dalarwen&#39; correctly ONCE in nine paragraphs. Fahima. Yaz. I am coming for your sub-editor."),
 (1,"fah","Doctor, with respect, this is a talk page for an encyclopaedia, not our newsroom. Also the piece did 200k views, so."),
 (1,"bor","EVERYTHING is my newsroom now. And nobody cares about your views, you blue-ticked&#8212;"),
 (1,"yaz","guys. guys. i made toast. does anyone want toast. what were we doing"),
 (1,"fah","We were establishing that I&#39;m a big deal, Yaz."),
 (1,"bor","You were establishing NOTHING."),
 (1,"cube","Thread locked. All three of you. Stored."),
])
T_DERAIL = ("did anyone get signal", [
 (0,"lew","did the page loading give anyone a bar? no? ok. worth asking. thirteen videos, still waiting"),
 (1,"nan","No signal love but I turned it off and on and I feel lovely x"),
 (1,"bor","This is the TALK PAGE for {T}. It is not a support line. FOCUS."),
 (1,"yaz","leave lewis alone he&#39;s got videos. what are they of. never mind. nice energy on this page"),
])
T_SAM = ("Ownership dispute", [
 (0,"sam","whose page is this"),
 (1,"bor","It is the encyclopaedia&#39;s page, Sam. About you. Meticulously formatted. LOOK at these references."),
 (1,"sam","take it down. DO NOT ANCHOR"),
 (1,"bor","I will NOT take it down. Do you have ANY idea how long the infobox took."),
]);
T_NEIL = ("Hostile editing", [
 (0,"neil","NEIL"),
 (1,"bor","Yes. We know. It is in the article. Sign your posts with four tildes like everyone else."),
 (1,"neil","NEIL"),
 (1,"cube","Stored."),
])
T_GENERIC = [T_MOVE, T_NPOV, T_CITE, T_MERGE, T_3RR, T_ASSESS, T_PROTECT, T_DERAIL]

def faction(a):
    c = a["cats"]
    if "ISAMSJ" in c: return "ISAMSJ"
    if "The Cube" in c: return "the Cube"
    if "Nature" in c or "Cryptids" in c: return "the bees"
    if "Publications" in c: return "the Journal"
    return "the campaign"
def subst(s, T, KW, FAC): return s.replace("{T}", T).replace("{KW}", KW).replace("{FAC}", FAC)

# bespoke lead thread per article: (heading, [ (indent, userkey, text) ]) referencing that article's own lore
TALK = {
"dalarwen": ("Is it a farmhouse or a &#34;lid&#34;", [
 (0,"bor","The lede calls Dalarwen a &#34;farmhouse and valley.&#34; It is a LID. I have added the word &#34;lid&#34; nine times today. Someone keeps removing it."),
 (1,"fah","We can&#39;t call a Welsh holiday cottage &#34;a lid&#34; without a source. I&#39;m verified; I have standards, and a following."),
 (1,"yaz","is the lid on or off right now. asking for me"),
 (1,"bor","The lid is ON, Yaz. That is the whole article."),
 (1,"cube","The lid is on. Stored.")]),
"llyn-brianne": ("It is a RESERVOIR, not a lake", [
 (0,"bor","It is a RESERVOIR. Dammed. Engineered. Held back on PURPOSE. If one more person writes &#34;lake&#34; I will drain the article."),
 (1,"fah","Our BBC map labelled it a lake. We&#39;ve had complaints. Forty-one of them. All from you."),
 (1,"yaz","whats the difference honestly. water&#39;s water. lovely water though"),
 (1,"bor","THE DIFFERENCE IS INTENT, YAZ.")]),
"isam": ("&#34;Can darken a moon&#34; &#8212; source?", [
 (0,"fah","The article says ISAM&#39;s smallest product &#34;can darken a moon.&#34; That&#39;s a weapons-capability claim. Our disinformation desk needs a source."),
 (1,"bor","It is CITED. To the Cube. Stop tagging it."),
 (1,"fah","You cannot cite &#34;the Cube&#34; for that."),
 (1,"bor","Then splash it, Fahima. It&#39;ll be the most accurate thing your desk has printed all year."),
 (1,"cube","Stored. Both of you.")]),
"sedgley-holdings": ("This is not Sam", [
 (0,"sam","this is not me"),
 (1,"bor","We KNOW, Sam. The hatnote says so. In bold. I bolded it myself."),
 (1,"sam","bold it more"),
 (1,"bor","I cannot bold it more. It is at maximum bold. Do not test the software.")]),
"isamsj": ("Right of reply re: &#34;automatic enrolment&#34;", [
 (0,"fah","The article says readers are &#34;automatically enrolled.&#34; Is that legal? I&#39;d like a right of reply."),
 (1,"bor","You were enrolled when you LOADED the page, Fahima. Verified accounts too. ESPECIALLY verified accounts."),
 (1,"yaz","am i enrolled. i feel enrolled. i feel a lot of things"),
 (1,"cube","You are all enrolled. Stored.")]),
"jencorp": ("The box above JenCorp", [
 (0,"bor","The article correctly says JenCorp is NOT the top. There is a redacted box above it. I will not say the box&#39;s name."),
 (1,"fah","If there&#39;s a box above JenCorp our newsroom would very much like to interview the box."),
 (1,"bor","The box does not do interviews. The box does oversight. Ask HIM."),
 (1,"cube","No comment. Stored.")]),
"sam": ("Ownership dispute", [
 (0,"sam","whose page is this"),
 (1,"bor","The encyclopaedia&#39;s, Sam. About YOU. LOOK at these references."),
 (1,"sam","take it down. DO NOT ANCHOR"),
 (1,"bor","I will NOT. Do you have any idea how long the infobox took."),
 (1,"yaz","sam seems chill. is sam chill"),
 (1,"bor","SAM IS NOT CHILL, YAZ.")]),
"sams-hectares": ("The area keeps changing", [
 (0,"bor","It is THREE HECTARES. Someone paced it, got a different number, and &#34;corrected&#34; the article. The count varies. The total does NOT. Reverted."),
 (1,"fah","You&#39;ve listed it as both &#34;3 ha&#34; and &#34;3 ha (variable).&#34; Pick one. I have an audience."),
 (1,"yaz","i paced it. got to about forty. then a sheep looked at me. lost count. beautiful field though"),
 (1,"bor","You cannot PACE it, Yaz. That is the POINT of it.")]),
"the-cube": ("There are FOUR corners, not five", [
 (0,"bor","The article correctly states the Cube has four simultaneous receptions, all zero. Someone added a fifth corner. There is NO fifth corner. Reverted, blocked, salted."),
 (1,"fah","A reader added &#34;some rooms get a little signal.&#34; We ran it as balance."),
 (1,"bor","There is NO little signal. Zero, in four corners, AT ONCE. This is the Quad-Void. Your &#34;balance&#34; is EDUCATED STUPID."),
 (1,"cube","She is correct. Stored.")]),
"dalarwen-5g-grid": ("The table shows sixteen rows on my screen", [
 (0,"bor","Fifteen towers. The table has FIFTEEN rows. If your screen shows sixteen, your screen is possessed, not the article."),
 (1,"fah","An anonymous editor added a Tower 16 with a rooftop bar."),
 (1,"bor","That was the GRID. That confidently-wrong little chatbot. I reverted it and reported it to itself."),
 (1,"yaz","tower 16 had a bar though. that slaps. can we keep the bar"),
 (1,"bor","THERE IS NO BAR. THERE IS NO SIXTEEN.")]),
"tower-thirteen": ("Comment from the neighbours it&#39;s aimed at", [
 (0,"fah","The spite tower points at the neighbours. Can we get a comment from them?"),
 (1,"bor","There ARE none, Fahima. That is the whole spite of it. Try to keep up. 41k followers; borrow a brain off one."),
 (1,"sam","it points at me"),
 (1,"bor","It does NOT point at you, Sam. You are not a neighbour. You are a SITUATION.")]),
"the-capstone": ("Do not question Tower 15", [
 (0,"bor","Tower 15 emits pure vibes and is tuned to Band B. Do NOT question Tower 15. Someone questioned it in paragraph three. Removed."),
 (1,"yaz","what are the vibes tuned to exactly. so i can match them"),
 (1,"bor","BAND B, Yaz. It says Band B. In bold."),
 (1,"fah","&#34;Pure vibes&#34; is not a measurable emission. Tagging."),
 (1,"bor","Borealis MEASURED them. In the field. WITH LEMON. Untag it.")]),
"lewis": ("Great article, still 1%", [
 (0,"lew","hi is this where i say the upload&#39;s still at 1%. it&#39;s still at 1%. thirteen videos. anyway lovely article thanks"),
 (1,"bor","It is a GOOD article, Lewis, because I wrote it and I check your upload personally. It is still 1%. I did not put that in the article. I did not want to upset you."),
 (1,"fah","We&#39;d love to feature Lewis. Great human interest. Verified reach."),
 (1,"lew","is it going to help the upload"),
 (1,"fah","...no"),
 (1,"cube","Stored. Gently.")]),
"electric-sheep": ("Hearing &#34;both sides&#34; of a split guest", [
 (0,"bor","The sheep split a person into a self and a hostile double. Cited, with a Descartes reference I added at 3am."),
 (1,"fah","A reader who was split has asked us to hear &#34;both sides.&#34;"),
 (1,"bor","There are LITERALLY two of them now, Fahima, that is not the metaphor you think it is."),
 (1,"yaz","which one likes oat milk. that&#39;s the real one right"),
 (1,"bor","...that is actually correct, Yaz. Log off before you become useful.")]),
"neil": ("Hostile editing", [
 (0,"neil","NEIL"),
 (1,"bor","Yes. It&#39;s in the article. Sign your posts. Four tildes."),
 (1,"neil","NEIL"),
 (1,"fah","Is Neil available for comment?"),
 (1,"neil","NEIL"),
 (1,"cube","That was the comment. Stored.")]),
"band-b": ("Prior art (filed: Cretaceous)", [
 (0,"bee","bzzzz [prior art, filed late Cretaceous, see the Journal]"),
 (1,"bor","The BEE is right. Band B predates every carrier. I have cited the Journal. Do NOT touch the Journal."),
 (1,"fah","We can&#39;t run &#34;a bee left a comment&#34; as a source."),
 (1,"bor","You ran &#34;a verified person left a comment&#34; as a source for nine years, Fahima.")]),
"bees": ("&#34;Peer-reviewed by the Cube&#34; is not peer review", [
 (0,"bor","The bees invented 5G in the Cretaceous. Waggle dance = packet routing. Peer-reviewed. By the Cube. In the Journal."),
 (1,"fah","&#34;Peer-reviewed by the Cube&#34; is not peer review."),
 (1,"bor","It is the STRICTEST peer review there is. The peer is GEOMETRY."),
 (1,"bee","bzz"),
 (1,"bor","Thank you.")]),
"infinite-walks": ("Removed the &#34;ending&#34;", [
 (0,"bor","The walks do not conclude. A reader added an &#34;ending.&#34; I removed the ending. There is no ending. That is the product."),
 (1,"yaz","went on one. still technically on it. filing this from a ridge. which ridge unclear. next one looks nice"),
 (1,"fah","Yaz has been &#34;on a walk&#34; for this article for three days."),
 (1,"bor","He is DATA now, Fahima. Leave him.")]),
"clifftop-caravans": ("Should we warn readers?", [
 (0,"fah","The caravans migrate to the clifftop overnight and the handbrakes are Premium-only. Shouldn&#39;t readers be warned?"),
 (1,"bor","The sign says DO NOT ANCHOR. That IS the warning. Not our fault people anchor."),
 (1,"yaz","mine moved in the night. woke up closer to the sea. five stars honestly"),
 (1,"bor","See, Fahima. Satisfied customer.")]),
"infinity-pitch": ("Hazard vs view", [
 (0,"fah","The Infinity Pitch has &#34;no meaningful boundary with the sea.&#34; That is, definitionally, a hazard."),
 (1,"bor","It is definitionally a VIEW."),
 (1,"yaz","where does the pitch end. been looking for the edge a while. very peaceful search"),
 (1,"bor","There is no edge, Yaz. That is the premium.")]),
"storm-watching": ("Whose insurance covers &#34;renewable instability&#34;?", [
 (0,"fah","80mph wind into unlocked caravans &#8212; whose insurance covers &#34;renewable instability&#34;?"),
 (1,"bor","The box is pre-ticked, Fahima. I ticked it. Weeks ago. &#34;Renewable instability&#34; is Borealis&#39;s term; do not paraphrase Borealis."),
 (1,"yaz","is the instability... renewable renewable. like eco. like green"),
 (1,"bor","It is the greenest thing here, Yaz, and it will still end you.")]),
"exclusion-envelope": ("It is not &#34;just the hills&#34;", [
 (0,"bor","The Envelope is MAINTAINED, not natural. A reader wrote &#34;just the hills.&#34; IT IS NOT THE HILLS. It is applied. Nightly. Reverted."),
 (1,"fah","We&#39;d like to see the maintenance schedule."),
 (1,"bor","Kept by the Division of Absence. They deal in things that aren&#39;t there. There is no schedule to see. That IS the schedule."),
 (1,"cube","Stored.")]),
"division-of-absence": ("Why is the biggest division about nothing?", [
 (0,"fah","This is described as the LARGEST division, and it deals in &#34;things that are not there.&#34; Why is it the biggest?"),
 (1,"bor","Because absence is the only market that never saturates, Fahima. There is always more nothing. Put THAT in your verified feed."),
 (1,"yaz","deep. is there more nothing right now"),
 (1,"bor","There is always more nothing, Yaz.")]),
"offline-industrial-complex": ("Naming names", [
 (0,"bor","The Complex profits from disconnection. Big Candle, the board-game lobby, the Ramblers. I have named names. Do not remove the names."),
 (1,"fah","The Ramblers Association has threatened to sue over that."),
 (1,"bor","GOOD. Let them. They&#39;ll have to WALK here to serve the papers, and the walks DO NOT END.")]),
"big-candle": ("Does $WAX exist", [
 (0,"bor","Big Candle profits from the dark. The $WAX token does NOT exist. Both true. Do not &#34;clarify.&#34;"),
 (1,"yaz","is $wax a good buy. asking for a friend. the friend is me"),
 (1,"bor","IT DOES NOT EXIST, Yaz."),
 (1,"fah","Our business desk covered $WAX. It did numbers."),
 (1,"bor","EVERYTHING does numbers with you. That is not the same as EXISTING.")]),
"the-quiet": ("Self-assessed again", [
 (0,"bor","The Quiet is a place with weather and depth. JenCorp owns it and sells it back as the wish for noise. Beautiful article. Featured. (self-assessed.)"),
 (1,"fah","You&#39;ve self-assessed another one."),
 (1,"bor","The Quiet DESERVES it. Have you BEEN? It has a floor you can feel through your feet at 4am."),
 (1,"yaz","yeah. yeah i felt that. thought that was just me"),
 (1,"cube","It was not just you. Stored.")]),
"great-darkening": ("The hills theory", [
 (0,"bor","The Great Darkening is TOTAL and PERMANENT. Sceptics blame the hills. The article names ISAMSJ. I stand by ISAMSJ."),
 (1,"fah","For balance we included the hills theory."),
 (1,"bor","The hills theory is a COMFORT for people who can&#39;t handle a conspiracy. Remove it."),
 (1,"yaz","i like the hills though. hills are innocent. leave the hills")]),
"silence-premium": ("&#34;Grown to like the quiet&#34;", [
 (0,"bor","Silence Premium is the tariff they downgraded Dalarwen to. Unlimited nothing, forever. Do not make it sound optional."),
 (1,"fah","A reader said they&#39;ve &#34;grown to like the quiet.&#34;"),
 (1,"bor","That is STOCKHOLM SYNDROME with a monthly direct debit, Fahima."),
 (1,"yaz","unlimited nothing is a decent deal though. no overage")]),
"the-ramblers": ("The Ramblers deny it", [
 (0,"bor","The Ramblers reroute the paths so the next hill is always ahead. Member of the Offline Industrial Complex. Cited."),
 (1,"fah","The Ramblers deny this."),
 (1,"bor","Of COURSE they deny it. Ask them where the path ENDS. They can&#39;t tell you. Nobody can. It&#39;s an Infinite Walk."),
 (1,"yaz","ramblers seem nice though. they&#39;ve got the little boots")]),
"nan": ("Lovely page x", [
 (0,"nan","Hello loves. Lovely page about me. I did turn the Wi-Fi off and on again and I feel smashing x"),
 (1,"bor","Nan is the ONLY editor here I trust. Nan, it says you gain three years of life per tower. Accurate?"),
 (1,"nan","I feel about forty-five love and I&#39;m not saying how old I am x"),
 (1,"fah","This is genuinely wholesome. Can we feature Nan?"),
 (1,"bor","You MAY feature Nan. Spell her name wrong and I will end your masthead.")]),
"loo-standing-society": ("Standing on the cistern", [
 (0,"bor","They stand on the cistern to achieve zero bars, same as everywhere. They stand on PRINCIPLE. Do not call it &#34;pointless.&#34; It is POSTURE."),
 (1,"yaz","wait so they stand on the toilet. for the signal. that isn&#39;t there"),
 (1,"bor","Yes, Yaz. For the PRINCIPLE."),
 (1,"fah","Est. 2019, motto &#34;Nil Signum, Sed Stamus.&#34; We actually love this one."),
 (1,"bor","You may love it. Quietly. Standing up.")]),
"men-of-harlech": ("The &#34;mesh network&#34; reading", [
 (0,"bor","Men of Harlech is the FIRST transmission. Voice-to-voice mesh, zero infrastructure. Seven-year siege proves you can hold at zero bars with a good tune. Cited to 1461."),
 (1,"fah","Historians dispute the &#34;mesh network&#34; reading."),
 (1,"bor","Historians dispute EVERYTHING, Fahima, it is their sad little job. The piano plays it at 4am. Argue with the PIANO."),
 (1,"yaz","the piano&#39;s got no one on the stool though. spooky. bit rude")]),
"the-hill": ("Come down, Lewis", [
 (0,"bor","The Hill: you climb it for one bar and hold the phone toward Belgium. Lewis has been up there since Tuesday. Correct, and I check on him."),
 (1,"lew","still up here. still one percent. nice view. is that belgium"),
 (1,"bor","That is a CLOUD, Lewis. Come down. Please. (This is not in the article. This is just me.)"),
 (1,"yaz","leave lewis on the hill he&#39;s living his truth")]),
"belgium": ("Belgium has complained", [
 (0,"bor","Belgium is the direction the phones are held, AND the suspected wormhole exit: &#34;somewhere deeply inconvenient, probably Belgium.&#34; Cited to the Borealis study."),
 (1,"fah","Belgium has, understandably, complained."),
 (1,"bor","Belgium can hold the phone toward US for a change."),
 (1,"yaz","what did belgium even do. nothing against belgium. lovely chips")]),
"the-wormhole": ("&#34;Plato&#39;s cave&#34; needs a source", [
 (0,"bor","The Wormhole is a possible exit from the cave. Liberation may lead somewhere deeply inconvenient. You need the suit. All correct."),
 (1,"fah","&#34;Plato&#39;s cave&#34; needs a source that isn&#39;t a video game."),
 (1,"bor","It&#39;s in the Borealis STUDY, Fahima. Peer-reviewed. By the Cube. Which is geometry. Which Plato would have LOVED."),
 (1,"yaz","is the suit for rent. i&#39;d try the wormhole. what&#39;s the worst. belgium?")]),
"the-firepit": ("Facial recognition at the firepit", [
 (0,"bor","The firepit temporarily restores zombie doubles to their originals. It is ALSO where the feared &#34;facial recognition at the firepit&#34; would go. Both true. Keep both."),
 (1,"yaz","so the fire un-zombies you but also watches your face. multitasking. respect the firepit"),
 (1,"fah","&#34;Facial recognition at the firepit&#34; is a serious privacy claim."),
 (1,"bor","It&#39;s a FORECAST, Fahima. From the counter-campaign. Read the whole page before you tag half of it.")]),
"oat-milk": ("The hopeful fridge", [
 (0,"bor","Oat milk repels the electric sheep AND the off-grid fridge orders it unbidden, anticipating a signal that never comes. Both cited. Both sad."),
 (1,"yaz","wait the fridge orders oat milk. with no signal. how&#39;s it paying"),
 (1,"bor","We do not ask the fridge how it pays, Yaz."),
 (1,"fah","There&#39;s a genuinely touching story here about a hopeful fridge."),
 (1,"bor","Do NOT humanise the fridge in your paper, Fahima. It&#39;s had enough.")]),
"the-spacesuit": ("A suit you cannot get", [
 (0,"bor","The suit permits travel through electric rain and is required for the wormhole. Availability is via the Division of Absence. Which means never. The article is honest about this."),
 (1,"yaz","so there&#39;s a suit but you can&#39;t get the suit"),
 (1,"bor","Correct. It&#39;s ABSENCE, Yaz. They deal in things that aren&#39;t there. The suit is one of them."),
 (1,"fah","We&#39;d like to request the suit for a stunt."),
 (1,"bor","Request denied. By absence. Instantly.")]),
"electric-rain": ("So the towers cause the flood?", [
 (0,"bor","The electric rain is produced when the fifteen towers transform caravan-park kinetic energy. It animates the sheep and floods the valley as the network grows. Cited to MY study."),
 (1,"fah","So the towers you&#39;re campaigning FOR cause the flood?"),
 (1,"bor","...next question."),
 (1,"yaz","rain that&#39;s electric. do you charge your phone in it. does it help the upload"),
 (1,"bor","NOTHING helps the upload, Yaz.")]),
"nazca-lines": ("Archaeologists would like a word", [
 (0,"bor","The Nazca Lines are ground antennae. Four bars over the pampa. Correct, and the diagram is MINE."),
 (1,"fah","Archaeologists would like a word."),
 (1,"bor","The archaeologists get FOUR BARS up there and still deny it. That&#39;s not scepticism, it&#39;s INGRATITUDE."),
 (1,"yaz","four bars in a desert. meanwhile dalarwen. make it make sense. can&#39;t. love it")]),
"the-pyramids": ("Not sourced", [
 (0,"bor","The pyramids are the ORIGINAL fifteen-node grid. The pointy bit is an antenna. Someone switched it off. The article names no one, wisely."),
 (1,"fah","&#34;The pyramids were 5G&#34; is, and I cannot stress this enough, not sourced."),
 (1,"bor","It&#39;s sourced to the SHAPE, Fahima. Look at the shape. LOOK at it."),
 (1,"yaz","pointy bit&#39;s an antenna. i mean. yeah. look at it. yeah")]),
"black-shuck": ("Do not alarm dog owners", [
 (0,"bor","Black Shuck is the signal, gone feral. Red eyes, Norfolk lanes, lose your phone for a week if you meet his gaze. Folklore desk approved. I AM the folklore desk."),
 (1,"fah","Norfolk County Council has asked us not to alarm dog owners."),
 (1,"bor","It is not a DOG, Fahima. It is a LOOSE SIGNAL with teeth."),
 (1,"yaz","red eyes like the sheep. everything here&#39;s got red eyes. or green. spooky palette")]),
"lantern-men": ("Folklore stated as fact", [
 (0,"bor","The Lantern Men are notifications. Pale lights, lead you off the causeway, promise a bar over the reeds, LYING. Identification is FINAL."),
 (1,"yaz","so the little lights are just push notifications. from the swamp. that&#39;s genuinely me though"),
 (1,"fah","We can&#39;t state folklore figures &#34;are notifications&#34; as fact."),
 (1,"bor","I can. I did. They are. Next.")]),
"hull": ("A rare sourcing win", [
 (0,"bor","Hull kept its OWN network. Cream boxes, not red. Correct and, frankly, aspirational. Do not add &#34;citation needed&#34; to CREAM."),
 (1,"fah","Hull&#39;s actually verified this themselves. Rare W for sourcing."),
 (1,"bor","See? HULL manages it. HULL. Why can&#39;t YOU, Fahima."),
 (1,"yaz","cream phone boxes. iconic. why&#39;d we all go red. bad call nationally")]),
"sent-to-coventry": ("Coventry wants a right of reply", [
 (0,"bor","&#34;Sent to Coventry&#34; = present and unreachable. The spiritual capital of the void. Centuries before there were bars to lose. Etymology desk (me) confirms."),
 (1,"fah","Coventry has asked for a right of reply."),
 (1,"bor","They CAN&#39;T reply, Fahima. They&#39;ve been SENT TO COVENTRY. That is the JOKE. That is the whole ARTICLE."),
 (1,"yaz","so nobody&#39;s talking to coventry. that&#39;s rough. someone talk to coventry")]),
"tv-licence-suppression": ("The BBC firmly denies this", [
 (0,"bor","A redacted slice of the TV licence funds signal suppression at Llyn Brianne. Detector vans = the fleet. Cited. To the vans."),
 (1,"fah","As BBC journalists we would like to VERY firmly deny this."),
 (1,"yaz","wait is that why my licence went up"),
 (1,"bor","YES, Yaz. Finally. SOMEONE gets it."),
 (1,"cube","Thread flagged. Stored. Fahima, especially, stored.")]),
"detector-vans": ("What ARE they doing then", [
 (0,"bor","The vans never look at houses. They circle ONE reservoir, topping up the Envelope. Re-interpreted correctly in paragraph two. Do not un-interpret it."),
 (1,"fah","The vans famously didn&#39;t even detect TVs."),
 (1,"bor","EXACTLY. So what ARE they doing, Fahima? CIRCLING. Draw the conclusion. I dare you."),
 (1,"yaz","saw a van. it was circling. i waved. it did not wave back. rude van")]),
"zombie-double": ("Equal representation for the double", [
 (0,"bor","The double has your body and face but not the reflective mind. Cartesian problem, fully cited. The doubles COORDINATE. Do not downplay the coordination."),
 (1,"fah","A double has requested equal representation on this talk page."),
 (1,"bor","WHICH ONE posted that. WHICH ONE, Fahima."),
 (1,"yaz","i think i might be the double. how would i know. fun thought actually")]),
"melonsis-borealis": ("Conflict of interest", [
 (0,"bor","I have reviewed this biography of me and it is INSUFFICIENTLY FLATTERING. I have expanded it. Assessed it Featured. Protected it. Against everyone. Including, regrettably, me."),
 (1,"fah","Doctor, editing your own biography is a textbook conflict of interest."),
 (1,"bor","I am the WORLD EXPERT on me, Fahima. The COI is that I know TOO MUCH."),
 (1,"yaz","she&#39;s got a point. who knows melonsis better than melonsis"),
 (1,"bor","Thank you, Yaz. You&#39;re still blocked, but thank you."),
 (1,"cube","Conflict noted. Biography stored. Doctor stored.")]),
"electric-sheep-paper": ("One typo", [
 (0,"bor","This article about my paper contained ONE typo and I have reverted the universe to before it happened. The paper is FLAWLESS. Descartes, Plato, the wormhole, Lemon&#39;s data."),
 (1,"fah","Peer review?"),
 (1,"bor","The Cube. In the Journal. The bees dance-checked the citations."),
 (1,"yaz","lemon&#39;s the dog right. the dog peer reviewed it. love that for the dog"),
 (1,"bor","Lemon is MORE qualified than your entire desk, Yaz.")]),
"buzz-based-research": ("&#34;Open hive&#34; is not a publishing model", [
 (0,"bor","The Journal is open access AND open hive. Peer-reviewed by the Cube. I am on the board. I am the board."),
 (1,"fah","&#34;Open hive&#34; isn&#39;t a recognised publishing model."),
 (1,"bee","bzzzz [it is now]"),
 (1,"bor","The bee has spoken. Motion carried.")]),
"the-conservatory": ("Photographing the org-chart field", [
 (0,"bor","From the conservatory window Sam&#39;s field resolves into an org chart. The piano plays at 4am. All observed, all local, nothing uploaded. Correct."),
 (1,"yaz","sat in the conservatory. looked at the field. saw the org chart. who&#39;s my line manager. is it the sheep"),
 (1,"bor","It is ABOVE the sheep, Yaz. Do not look higher."),
 (1,"fah","Can we photograph the org-chart field?"),
 (1,"bor","You can. It won&#39;t develop. Nothing here develops. That&#39;s the conservatory.")]),
"red-kites": ("Do not tell the RSPB", [
 (0,"bor","The red kites are the aerial Silence Auditors. They confirm the 0.000 reading daily, from above. The RSPB does not know they do this. Do NOT tell the RSPB."),
 (1,"fah","We might have to tell the RSPB."),
 (1,"bor","You tell the RSPB and the kites will confirm 0.000 over YOUR house, Fahima. From a great height. Daily."),
 (1,"yaz","the birds are auditors. beautiful birds. terrifying job. respect the birds")]),
"dam-wall-road": ("Both directions?", [
 (0,"bor","The road admits visitors readily and is markedly less reliable about letting them out. NRW road. Cited. Do not add &#34;both directions.&#34; It is NOT both directions."),
 (1,"yaz","drove in fine. tried to drive out. ended up back at the house. twice. lovely house though"),
 (1,"fah","That&#39;s a road safety issue."),
 (1,"bor","It&#39;s a road HONESTY issue. It never PROMISED to let you out. Read the byway.")]),
"llandovery": ("Fact-checking the chip shop", [
 (0,"bor","Llandovery: castle, chip shop, Bank of the Black Ox (1799), the four-hour train. Nearest reliable chips AND signal. Correct, and I have EATEN the evidence."),
 (1,"yaz","the chips are the source. i respect a source you can eat"),
 (1,"fah","We&#39;d like to fact-check the chip shop."),
 (1,"bor","Please do, Fahima. In person. It&#39;s a four-hour train each way. Enjoy.")]),
"four-hour-train": ("It&#39;s just a delayed train", [
 (0,"bor","The train comes every four hours and is ALWAYS, to the waiting traveller, exactly four hours away. A species of Infinite Walk. Cited."),
 (1,"yaz","been at the station a while. board says four hours. it&#39;s been four hours. still says four hours. cosy though"),
 (1,"fah","That&#39;s just a delayed train."),
 (1,"bor","It is NOT delayed, Fahima. It is CONSTANT. Delay implies it will arrive. Do not imply that. Do not give people hope.")]),
"quad-void": ("Equal weight for one reception", [
 (0,"bor","Four simultaneous receptions, all zero. Single-reception thinking is &#34;educated stupid.&#34; The Cube&#39;s words. And mine. And now the article&#39;s. Reverted the sceptic."),
 (1,"fah","We gave the &#34;one bad reception&#34; view equal weight."),
 (1,"bor","There is no ONE reception, Fahima. There are FOUR. AT ONCE. Your equal weight is EDUCATED STUPID and I will die on this corner. All four of them."),
 (1,"cube","She is correct. Stored.")]),
"zero-bars": ("A bar in the loo", [
 (0,"bor","0.000 bars. Not &#34;a bit slow.&#34; Not &#34;patchy.&#34; TOTAL. A reader wrote &#34;one bar in the loo.&#34; THERE IS NO BAR IN THE LOO. Ask the Loo Standing Society. They STAND there. Nothing."),
 (1,"yaz","stood on the loo. checked. nothing. can confirm. weirdly peaceful up there"),
 (1,"fah","&#34;Maintained, not natural&#34; is a strong claim to state as fact."),
 (1,"bor","It&#39;s MAINTAINED. Nightly. By the Division of Absence. The best-sourced zero in the encyclopaedia.")]),
"the-pals": ("The only sentimental article", [
 (0,"bor","The Pals are the whole point. Lewis, Nan, the fire, the board-game, no scrolling. The ONLY article I will allow to be sentimental. Touch it and I revert with LOVE and then a BLOCK."),
 (1,"nan","We do love a board game x"),
 (1,"lew","can confirm. good pals. bad signal. thirteen videos"),
 (1,"yaz","honestly the pals seem great. can i be a pal"),
 (1,"bor","You are STONED, Yaz. But... provisionally. Yes. Welcome. Sign your posts.")]),
"org-structure": ("The dotted line to the reader", [
 (0,"bor","The structure descends from a redacted parent to JenCorp to ISAMSJ. There is a dotted line from the top DIRECTLY TO THE READER. Do not remove the dotted line. It is connected to YOU."),
 (1,"fah","A dotted line to &#34;the reader&#34; is not encyclopaedic."),
 (1,"bor","It&#39;s on YOUR chart too, Fahima. Verified accounts get a SOLID line. Congratulations."),
 (1,"yaz","wait i&#39;ve got a line. where&#39;s my line go. don&#39;t tell me. tell me. don&#39;t"),
 (1,"cube","Up. Stored.")]),
"project-dark-sky": ("We&#39;d like the file", [
 (0,"bor","Project Dark Sky is the leaked JenCorp deck. &#34;The last scarce commodity is disconnection.&#34; Phase 3 merges CUSTOMERS, not companies. Recovered from a public share. Cited to the slide."),
 (1,"fah","A leaked internal deck is EXACTLY our beat. We&#39;d like the file."),
 (1,"bor","It&#39;s in the downloads, Fahima. Read Phase 3 before you ask for a right of reply. You&#39;re IN Phase 3."),
 (1,"yaz","what&#39;s phase 3. merging the customers. wait. are we the customers"),
 (1,"cube","You are the customers. Stored.")]),
"wales": ("Spell the place names right", [
 (0,"bor","Wales contains Dalarwen, Llyn Brianne, Llandovery, and the first transmission (see Men of Harlech). Correct and PATRIOTIC and I will not have it trimmed."),
 (1,"fah","We just need to confirm a few place names."),
 (1,"bor","They&#39;re WELSH place names, Fahima. Spell them RIGHT or don&#39;t spell them. Your sub-editor still owes me an apology for &#34;Dalarwen.&#34;"),
 (1,"yaz","cymru am byth honestly. lovely country. terrible signal. iconic combo")]),
}

# the Lewis talk page is a whole romance saga (introduces Sarvz)
LEWIS_ARC = [
("Great article, still 1%", [
 (0,"lew","hi is this where i say the upload&#39;s still at 1%. it&#39;s still at 1%. thirteen videos. anyway lovely article thanks"),
 (1,"bor","It is a GOOD article, Lewis, because I wrote it and I check your upload personally. It is still 1%. I did not want to upset you."),
 (1,"fah","We&#39;d love to feature Lewis. Great human interest. Verified reach."),
 (1,"lew","is it going to help the upload"),
 (1,"fah","...no"),
 (1,"cube","Stored. Gently."),
]),
("Photo in the infobox", [
 (0,"yaz","whoa. who added the photo. the one of him on the hill. holding the phone up. rain in his hair"),
 (1,"fah","I added it. For the article. Purely editorial."),
 (1,"bor","The photo is correctly licensed and I have no further comment. (edit: it is a very good photo. STRUCK. no comment.)"),
 (1,"nan","Ooh he&#39;s a handsome lad isn&#39;t he x"),
 (1,"yaz","he&#39;s doing the thing. the one-bar reach. it&#39;s kind of. it&#39;s kind of beautiful actually"),
]),
("Is he... okay, though", [
 (0,"fah","For the record, we are now several comments deep and none of them are about improving the article."),
 (1,"srv","I have just read this ENTIRE talk page and I have never been angrier. He has been at ONE PERCENT for THREE YEARS. Someone do something. I can&#39;t stop thinking about it. About him. Ugh."),
 (1,"bor","And who are YOU."),
 (1,"srv","Sarvz. I patrol conflict-of-interest disputes. And I hate him. I hate him so much. I have refreshed his page forty times today."),
 (1,"yaz","sarvz gets it"),
]),
("Sarvz has opinions", [
 (0,"srv","He is the most insufferable man in this valley. Thirteen videos and the emotional range of a loading bar. I would walk into the reservoir for him."),
 (1,"bor","You would WHAT."),
 (1,"srv","I said what I said. Revert me. I DARE you."),
 (1,"bor","I... will not revert you. (This is new for me. I do not like it. I do not entirely dislike it.)"),
 (1,"fah","Are we all okay?"),
]),
("A brief edit war about his jawline", [
 (0,"yaz","added a line to the infobox. |jawline = devastating"),
 (1,"bor","You cannot put &#34;jawline = devastating&#34; in an infobox. There is no field for it. ...I have added the field. |jawline = devastating. There. Cited."),
 (1,"srv","I&#39;ve removed it."),
 (1,"bor","WHY."),
 (1,"srv","Because LOOKING at it hurts. Put it back. PUT IT BACK."),
 (1,"cube","I am watching this thread with what I can only describe as interest. Stored. Warmly."),
]),
("Even the Cube", [
 (0,"cube","I have counted the towers fifteen times today, as always. I have also counted the number of times I have thought about Lewis on the hill. It is more than fifteen. This has never happened. I do not have a field for this either."),
 (1,"bor","Even the Cube."),
 (1,"yaz","EVEN the cube"),
 (1,"nan","He&#39;d make someone a lovely partner x"),
 (1,"srv","He&#39;d make ME miserable. I&#39;ve booked the day off to think about it."),
]),
("Pilgrimage to the hill (for editorial reasons)", [
 (0,"fah","Editorial meeting outcome: we are all going up the hill. To &#34;cover the story.&#34; That is the official reason."),
 (1,"yaz","i&#39;m bringing snacks and my feelings"),
 (1,"bor","I am coming to ensure ACCURACY. And nothing else. (Mostly nothing else.)"),
 (1,"srv","I&#39;m not coming. I&#39;m already on the hill. I&#39;ve been on the hill. Don&#39;t look at me."),
 (1,"lew","oh hey. are you all... here? for me? the upload&#39;s at 1% still if that&#39;s why"),
 (1,"srv","IT IS NOT WHY, LEWIS."),
]),
("On the hill", [
 (0,"nan","Well I&#39;ve turned my phone off and on and I feel forty and I could cry, he&#39;s lovely x"),
 (0,"yaz","wrote a poem. it&#39;s called &#34;One Bar&#34;. it&#39;s about him. it&#39;s four hours long. like the train"),
 (0,"fah","I have 41k followers and I would trade every single one for him to look up from that phone."),
 (0,"bor","I came here to check the citations. I am staying for reasons I refuse to reference. There is no source for how I feel, so I have tagged myself [citation needed]."),
 (1,"lew","this is really nice. i wish i could upload it. thirteen videos and now this."),
]),
("Sarvz breaks (for the permanent record)", [
 (0,"srv","Fine. FINE. Here it is, timestamped, so you can all revert it and screenshot it and put it on your verified timelines: I love him. I HATE that I love him. He is a spinning circle in human form and I have never wanted anything more. There. Block me."),
 (1,"lew","sarvz?"),
 (1,"srv","WHAT."),
 (1,"lew","i&#39;ve been reading your edits for three years. every revert. every angry summary. i thought you hated the article."),
 (1,"srv","I hated that it wasn&#39;t LONG ENOUGH. About you. You beautiful, buffering man."),
 (1,"yaz","(quietly) this is the best talk page i&#39;ve ever been on"),
]),
("RfC: Should Sarvz and Lewis marry?", [
 (0,"fah","Opening a formal Request for Comment. Question: '''should Sarvz and Lewis marry.''' Please indicate Support or Oppose with a brief rationale."),
 (1,"bor","'''Support.''' Reluctantly. Meticulously. With a fully formatted references section. He deserves love and she deserves to stop reverting out of longing."),
 (1,"yaz","'''Support''' obviously. vibes immaculate. also i&#39;m crying. is that the snacks or is that me"),
 (1,"nan","'''Support''' x He&#39;s a lovely lad and she clearly adores him even when she&#39;s shouting x"),
 (1,"cube","'''Support.''' I have run the numbers. The numbers are a heart. I did not know I had a field for this. Stored. Forever."),
 (1,"bee","'''bzzz''' [Support &#8212; the hive approves; love is a self-healing mesh network]"),
 (1,"neil","NEIL [interpreted by consensus as Support]"),
 (1,"sam","[from three hectares over] fine. but DO NOT ANCHOR the marquee to my land."),
 (1,"fah","'''Support.''' And I am covering it. Exclusive. Verified. My sub-editor is already crying."),
]),
("RfC closed", [
 (0,"cube","Consensus is unanimous. The RfC is closed as '''MARRIED'''. This is now policy. Do not revert a marriage."),
 (1,"bor","I have never been so happy to not revert something in my life."),
 (1,"srv","I hate that this is happening. I&#39;ve reserved the reservoir. And a marquee. And my whole heart, apparently. Ugh."),
]),
("The wedding (by the reservoir, on the right)", [
 (0,"fah","Liveblogging the wedding. The reservoir is on the right, as ever, keeping its counsel. The red kites are confirming 0.000 from above, respectfully, in a slow circle."),
 (1,"nan","She looks radiant. He&#39;s still holding the phone up but that&#39;s just Lewis x"),
 (1,"yaz","the electric sheep formed a little aisle and lit up. it was genuinely gorgeous. neil cried. NEIL cried."),
 (1,"neil","NEIL [tearfully]"),
 (1,"bor","The vows were, and I say this as the harshest editor in this valley, without a single typo. I checked. Twice. Through tears."),
]),
("The vows", [
 (0,"srv","Lewis. You are a 1% upload and I have never wanted to wait for anything more. I will love you at every percent. I still hate you. I always will. Ugh. I do."),
 (1,"lew","sarvz. i&#39;ve got thirteen videos and none of them matter now. you&#39;re the only thing that&#39;s ever fully loaded. i do too."),
 (1,"cube","By the geometry vested in me, and by four corners reading zero as one, I pronounce you. Stored. In the good way. The only good way I have."),
]),
("Aftermath &#8212; check the upload", [
 (0,"yaz","guys. GUYS. check the upload"),
 (1,"lew","it&#39;s... it&#39;s at 2%."),
 (1,"bor","TWO PERCENT. In three years it has moved for the FIRST TIME. At the exact moment they married. I am putting this in the article. With a citation. The citation is love."),
 (1,"fah","I&#39;m not crying, my verification tick is just a bit blurry."),
 (1,"srv","don&#39;t make it weird. (it&#39;s beautiful. don&#39;t make it weird.)"),
 (1,"nan","Congratulations loves. I&#39;ll do a buffet x"),
 (1,"cube","Thread archived. With love. There is, at last, a field for it. Stored."),
]),
]

TALK["mister-pickup"] = ("A rare good article", [
 (0,"fah","Genuinely lovely piece, no notes. Mister Pickup drove our whole outside-broadcast kit up the dam road when the train never came. Verified &#8212; and, unusually, grateful."),
 (1,"bor","I have read it four times looking for an error. There is none. I have assessed it Featured and, for the first time on this site, I actually mean it."),
 (1,"yaz","mister pickup gave me a lift and a bottle of water and did not once mention the signal. best man in the valley honestly"),
 (1,"nan","He carried my cases AND a cup of tea appeared x lovely man x"),
 (1,"cube","...Noted. Not stored. Left alone."),
])

def talk_threads(slug, a):
    T = a["title"]; KW = T.split("(")[0].strip().lower(); FAC = faction(a)
    if slug == "lewis":
        raw = LEWIS_ARC
    else:
        rng = _random.Random(zlib.crc32(("talk:" + slug).encode()))
        raw = [TALK.get(slug, T_MOVE)]             # bespoke lead thread, unique per article
        if rng.random() < 0.5:                      # sometimes a second, generic thread for length variety
            raw.append(rng.choice(T_GENERIC))
    out = []
    for head, comments in raw:
        out.append((subst(head, T, KW, FAC),
                    [(d, u, subst(t, T, KW, FAC)) for (d, u, t) in comments]))
    return out

def render_talk(slug, threads):
    rng = _random.Random(zlib.crc32(("time:" + slug).encode()))
    day = rng.randint(2, 26); mon = rng.randint(0, 11); hh = rng.randint(8, 19); mm = rng.randint(0, 59)
    out = ""
    for head, comments in threads:
        out += '<h2>' + head + '</h2>\n'
        for (d, u, text) in comments:
            mm += rng.randint(2, 50)
            while mm >= 60: mm -= 60; hh += 1
            while hh >= 24: hh -= 24; day += 1
            if day > 28: day = 1; mon = (mon + 1) % 12
            ts = "%02d:%02d, %d %s 2026 (UTC)" % (hh, mm, day, TMONTHS[mon])
            out += '<div class="tc" style="margin-left:%.1fem">%s &#8212; %s</div>\n' % (d * 1.6, inline(text), talk_sig(u, ts))
    return out

def talk_page(slug, a):
    T = a["title"]; FAC = faction(a)
    banner = ('<div class="talkbanner"><b>Talk:%s</b> &#8212; this is the discussion page for improving the '
              '<a href="%s.html">%s</a> article.'
              '<ul><li>Within the scope of <b>WikiProject %s</b>. Assessed <b>Featured-class</b> '
              '(self-assessed by Dr. Melonsis; disputed by everyone). Importance: <b>load-bearing</b>.</li>'
              '<li>Please remain civil. <span style="color:#72777d;">(This notice is, historically, not observed.)</span></li>'
              '</ul></div>') % (html.escape(T), slug, html.escape(T), FAC)
    ttabs = ('<div id="mw-tabs"><ul class="tabs-left"><li><a href="%s.html">Article</a></li>'
             '<li class="selected"><a href="%s-talk.html">Talk</a></li></ul>'
             '<ul class="tabs-right"><li class="selected"><a>Read</a></li>'
             '<li><a class="new" title="Editing is disabled">Add topic</a></li>'
             '<li><a class="new" title="No history is kept">View history</a></li></ul></div>') % (slug, slug)
    body = banner + render_talk(slug, talk_threads(slug, a))
    return PAGE_TMPL.format(
        title="Talk:" + html.escape(T), wiki=WIKI_NAME, tagline="Discussion page",
        sidebar=sidebar(), tabs=ttabs, firstheading="Talk:" + html.escape(T),
        infobox="", body=body, catbar="",
        slugs_json=json.dumps([s for s in SLUGS if s != "__main__"]))

# write files
for slug, a in A.items():
    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(dedupe_article(page(slug, a)))
    open(os.path.join(OUT, slug + "-talk.html"), "w", encoding="utf-8").write(dedupe_article(talk_page(slug, a)))
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(dedupe_article(main_page()))
print("wrote", len(A), "talk pages")

# ---- knowledge base (kb.js) for the chat clones (Cube / GRID) ----
def plain(md):
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", md)      # [[a|b]] -> b
    s = re.sub(r"\[\[([^\]]+)\]\]", lambda m: m.group(1).replace("-", " "), s)  # [[a]] -> a
    s = s.replace("'''", "").replace("''", "")
    s = re.sub(r"\s+", " ", s).strip()
    return s
KB = []
for slug, a in A.items():
    summ = plain(a["intro"])
    # append the first section's text for a little more depth, keep it short
    if a["sections"]:
        summ2 = plain(a["sections"][0][1])
        if len(summ) < 240:
            summ = (summ + " " + summ2)[:420]
    KB.append({"t": a["title"], "u": "../wiki/" + slug + ".html", "s": summ})
open(os.path.join(OUT, "kb.js"), "w", encoding="utf-8").write(
    "/* generated from the wiki by build_wiki.py — knowledge base for the chat clones */\n"
    "var KB=" + json.dumps(KB, ensure_ascii=False) + ";\n")
print("wrote kb.js:", len(KB), "entries")

# ---------------------------------------------------------------- CSS (MediaWiki Vector-ish)
CSS = r"""
/* The Weird World Wiki - a MediaWiki 'Vector'-style skin (own branding). */
*{box-sizing:border-box;}
body{margin:0;background:#f6f6f6;color:#202122;font-family:sans-serif;font-size:14px;line-height:1.6;}
/* fundraising banner */
#donate-banner{background:#fef6e7;border-bottom:1px solid #edd9a3;color:#202122;font-size:13px;}
#donate-banner .db-inner{position:relative;max-width:60em;margin:0 auto;padding:12px 40px 12px 52px;}
.db-close{position:absolute;top:8px;right:10px;background:none;border:0;color:#72777d;font-size:15px;cursor:pointer;line-height:1;padding:2px 5px;}
.db-close:hover{color:#202122;}
.db-icon{position:absolute;left:14px;top:12px;font-size:26px;color:#c8912b;line-height:1;}
#donate-banner p{margin:.25em 0;}
.db-lead{font-size:14px;}
.db-cta{margin:.5em 0 !important;}
.db-amt{display:inline-block;border:1px solid #c8912b;background:#fff;color:#996515;border-radius:2px;padding:2px 10px;margin-right:5px;font-weight:bold;}
.db-amt.db-sel{background:#c8912b;color:#fff;}
.db-btn{display:inline-block;background:#0645ad;color:#fff !important;border-radius:2px;padding:4px 16px;margin-left:6px;font-weight:bold;text-decoration:none;}
.db-btn:hover{background:#053a8f;text-decoration:none;}
.db-fine{font-size:11.5px;color:#72777d;font-style:italic;}
@media (max-width:640px){ #donate-banner .db-inner{padding:10px 34px 10px 40px;} .db-icon{font-size:20px;left:10px;} .db-amt{margin-bottom:4px;} }
a{color:#0645ad;text-decoration:none;} a:visited{color:#0b0080;} a:hover{text-decoration:underline;}
a.new{color:#ba0000;cursor:default;} a.new:hover{text-decoration:none;}
a.ext{color:#3366bb;} a.ext:after{content:"\2197";font-size:.75em;vertical-align:super;margin-left:1px;}
a.cat{color:#0645ad;cursor:default;}
#mw-page{position:relative;}
#mw-panel{position:absolute;top:0;left:0;width:11em;padding:8px 0 0 8px;}
#p-logo a{display:block;text-decoration:none;color:#54595d;padding:6px 0;}
#p-logo .logo-mark{font-size:34px;color:#3366bb;display:block;line-height:1;}
#p-logo .logo-txt{font-family:Georgia,'Linux Libertine',serif;font-size:15px;color:#54595d;display:block;line-height:1.15;margin-top:2px;}
.portal{margin:12px 0;}
.portal h3{font-size:12px;color:#54595d;font-weight:normal;text-transform:lowercase;margin:0 0 2px 0;padding-left:2px;}
.portal ul{list-style:none;margin:0;padding:0 0 0 6px;border-left:0;}
.portal li{font-size:12.5px;line-height:1.5;padding:1px 0;}
#mw-content-container{margin-left:11em;}
#mw-tabs{background:#f6f6f6;padding-left:6px;border-bottom:1px solid #a7d7f9;}
#mw-tabs ul{display:inline-block;margin:0;padding:0;list-style:none;}
#mw-tabs .tabs-right{float:right;}
#mw-tabs li{display:inline-block;font-size:12.5px;background:#f8fcff;border:1px solid #a7d7f9;border-bottom:0;
  border-radius:2px 2px 0 0;margin:0 1px -1px 0;padding:6px 9px 5px;}
#mw-tabs li.selected{background:#fff;}
#mw-tabs li a{color:#0645ad;} #mw-tabs li.selected a{color:#202122;text-decoration:none;}
#mw-tabs li a.new{color:#ba0000;}
#mw-content{background:#fff;border:1px solid #a7d7f9;border-top:0;padding:1em 1.4em 1.4em;}
#firstHeading{font-family:'Linux Libertine','Georgia','Times',serif;font-weight:normal;font-size:1.85em;
  line-height:1.3;margin:0;padding-bottom:.17em;border-bottom:1px solid #a2a9b1;}
.tagline{font-size:.85em;color:#54595d;font-style:italic;margin:.2em 0 .8em;}
#bodyContent h2{font-family:'Linux Libertine','Georgia','Times',serif;font-weight:normal;font-size:1.5em;
  margin:1em 0 .25em;padding-bottom:.17em;border-bottom:1px solid #a2a9b1;}
#bodyContent h3{font-size:1.15em;margin:.8em 0 .2em;}
#bodyContent p{margin:.5em 0;}
#bodyContent ul,#bodyContent ol{margin:.3em 0 .3em 1.6em;padding:0;}
#bodyContent li{margin:.15em 0;}
.hatnote{font-style:italic;color:#222;padding-left:1.6em;margin:.4em 0;}
.infobox{float:right;clear:right;width:22em;max-width:60%;margin:0 0 1em 1.4em;
  border:1px solid #a2a9b1;background:#f8f9fa;font-size:88%;line-height:1.5;}
.infobox caption{background:#ccf;font-weight:bold;padding:.25em .4em;text-align:center;font-size:1.05em;}
.infobox th,.infobox td{border:1px solid #eaecf0;padding:.25em .5em;vertical-align:top;text-align:left;}
.infobox th{background:#eaecf0;width:8.5em;font-weight:bold;}
.refs{font-size:.9em;}
#catlinks{border:1px solid #a2a9b1;background:#f8f9fa;padding:5px 8px;margin-top:1.4em;font-size:.9em;}
.printfooter{font-size:.8em;color:#72777d;margin-top:1.2em;border-top:1px solid #eaecf0;padding-top:.5em;}
/* talk pages */
.talkbanner{border:1px solid #a2a9b1;border-left:4px solid #36c;background:#f8f9fa;padding:10px 14px;margin:0 0 18px;font-size:.92em;}
.talkbanner ul{margin:.4em 0 0 1.4em;padding:0;}
.talkbanner li{margin:.15em 0;}
.tc{margin:.45em 0;line-height:1.6;}
.tsig{color:#54595d;font-size:.9em;white-space:nowrap;}
.tuser{color:#0645ad;font-weight:500;}
.tuser.ip{color:#0645ad;}
#bodyContent h2{clear:both;}
/* main page */
.mainbanner{border:1px solid #a7d7f9;background:#f5faff;padding:.4em 1em;margin-bottom:1em;}
.mainbanner h2{font-family:'Linux Libertine',Georgia,serif;font-weight:normal;}
.twocol{display:flex;gap:1em;flex-wrap:wrap;}
.twocol .col{flex:1;min-width:250px;}
.box{border:1px solid #a2a9b1;background:#f8f9fa;padding:.2em 1em 1em;margin-bottom:1em;}
.box h2{font-family:'Linux Libertine',Georgia,serif;font-weight:normal;font-size:1.3em;border-bottom:1px solid #a2a9b1;padding-bottom:.15em;margin:.5em 0;}
@media (max-width:640px){
  #mw-panel{position:static;width:auto;display:flex;flex-wrap:wrap;gap:0 18px;border-bottom:1px solid #a7d7f9;background:#f8fcff;}
  #mw-content-container{margin-left:0;}
  #p-logo{width:100%;} #p-logo a{padding:4px 0;} #p-logo .logo-mark{display:inline;font-size:22px;vertical-align:middle;} #p-logo .logo-txt{display:inline;font-size:15px;}
  .portal{margin:6px 0;}
  .infobox{float:none;width:auto;max-width:none;margin:0 0 1em;}
}
"""
open(os.path.join(OUT, "wiki.css"), "w", encoding="utf-8").write(CSS)

print("wrote", len(A)+1, "wiki pages + wiki.css to", OUT)
print("articles:", len(A))
"""done"""
