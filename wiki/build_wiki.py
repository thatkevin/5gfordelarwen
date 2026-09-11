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
 ext=[("The reservoir on the field report","../about-dalarwen.html")],
 cats=["Places","Infrastructure"])

art("isam", "ISAM",
 "'''ISAM''' is an intergalactic weaponry firm and the senior partner in [[isamsj|ISAMSJ]]. Its munitions operate across the light-years; its smallest product is said to be capable of darkening a moon. Suppressing the mobile signal over one damp Welsh valley is, for ISAM, a rounding error performed for amusement.",
 infobox=[("Industry","Intergalactic weaponry"),("Parent","[[isamsj|ISAMSJ]] &rarr; [[jencorp|JenCorp]]"),("Notable capability","Signal suppression (trivial)"),("Motto","Withheld")],
 seealso=["isamsj","sedgley-holdings","jencorp","exclusion-envelope"],
 cats=["ISAMSJ","Organisations"])

art("sedgley-holdings", "Sedgley Holdings",
 "'''Sedgley Holdings''' is the terrestrial arm of [[isamsj|ISAMSJ]], responsible for land, mast rights, footpaths, pitches, and \"the space between the bars\". If a person has ever stood somewhere and received no signal, they have stood upon Sedgley Holdings' balance sheet. It is closely associated with the figure known as [[sam]].",
 infobox=[("Industry","Land; mast rights; absence"),("Parent","[[isamsj|ISAMSJ]]"),("Key figure","[[sam|S. Sedgley]]"),("Assets","[[infinite-walks]], [[clifftop-caravans]], the [[exclusion-envelope]]")],
 seealso=["isam","isamsj","sam","division-of-absence"],
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

art("sam", "Sam (Sedgley)",
 "'''Sam''', signed ''S. Sedgley'', is the neighbour of [[dalarwen]] and the personification of the terrestrial \"S\" in [[isamsj|ISAMSJ]]. Sam occupies exactly [[sams-hectares|three hectares]] behind a leaning gate marked ''DO NOT ANCHOR''. There are no neighbours for miles; Sam is the exception that proves it.",
 infobox=[("Full name","S. Sedgley"),("Occupation","The neighbour; land"),("Land","[[sams-hectares|Three hectares]]"),("Habits","Only ever seen leaving"),("Affiliation","[[sedgley-holdings]]")],
 sections=[("Sightings","No one has seen Sam ''arrive''; Sam is only ever seen ''leaving'', one hand raised in a wave that could be hello and is, on reflection, always goodbye.")],
 seealso=["sedgley-holdings","sams-hectares","isamsj","org-structure"],
 ext=[("Sam","../sam.html")],
 cats=["People","ISAMSJ"])

art("sams-hectares", "Sam's three hectares",
 "'''Sam's three hectares''' is a parcel of land adjoining [[dalarwen]], owned by [[sam|S. Sedgley]]. It is always, exactly, three hectares, though every pacing of it yields a different count. Viewed from the [[the-conservatory|conservatory]] window, the grass resolves into an [[org-structure|organisational chart]].",
 infobox=[("Area","Exactly 3 ha (variable)"),("Signage","DO NOT ANCHOR"),("Resolves into","An [[org-structure|org chart]]")],
 seealso=["sam","org-structure","clifftop-caravans"],
 cats=["Places","ISAMSJ"])

art("the-cube", "The Cube",
 "'''The Cube''' is the presiding intelligence of the Dalarwen mythos. In its lower aspect it is a rotating figure that counts the [[dalarwen-5g-grid|towers]] (there are fifteen; there is no sixteenth). In its higher aspect it is the redacted parent above [[jencorp|JenCorp]] &mdash; unreachable by climbing, arriving regardless.",
 infobox=[("Nature","Geometry; certainty"),("Aspects","Tower-counter (lower); [[jencorp|parent]] (upper)"),("Position","Both bottom and top of the [[org-structure|chart]]"),("Known for","Being unarguable")],
 sections=[("Doctrine","See [[quad-void|the Quad-Void]]. The Cube holds that a house has four simultaneous receptions, all zero, at once. It does not negotiate.")],
 seealso=["quad-void","jencorp","org-structure","the-quiet"],
 ext=[("The Cube (loud)","../the-cube.html"),("The Cube (above)","../above.html")],
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
 ext=[("Lewis Connectivity HQ","../lewis.html")],
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
 ext=[("Follow the Licence Fee","../tv-licence.html")],
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
            '<li><a class="new" title="Talk (does not exist)">Talk</a></li></ul>'
            '<ul class="tabs-right"><li class="selected"><a>Read</a></li>'
            '<li><a class="new" title="Editing is disabled">Edit</a></li>'
            '<li><a class="new" title="No history is kept">View history</a></li></ul></div>') % slug
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

# write files
for slug, a in A.items():
    open(os.path.join(OUT, slug + ".html"), "w", encoding="utf-8").write(dedupe_article(page(slug, a)))
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(dedupe_article(main_page()))

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
