import numpy as np
import psycopg2

# database
conn = psycopg2.connect(
    database="mapBot",
    user="postgres",
    password="54321",
    host="localhost",
    port=5432
)

# connecting to SQL
print("connected to postgres SQL MAPS DB")
# select all maps
allMaps = conn.cursor()
data = allMaps.execute("SELECT map_name, download_link, map_count FROM maps ORDER BY map_id")
maps = allMaps.fetchall()

# select all maps with map_count = 3
maps3 = conn.cursor()
data3 = maps3.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 3 ORDER BY map_id")
mapsThree = maps3.fetchall()

# select all maps with map_count = 4
maps4 = conn.cursor()
data4 = maps4.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 4 ORDER BY map_id")
mapsFour = maps4.fetchall()

# select all maps with map_count = 5
maps5 = conn.cursor()
data5 = maps5.execute("SELECT map_name, download_link, map_count FROM maps WHERE map_count = 5 ORDER BY map_id")
mapsFive = maps5.fetchall()

# turn query into array
vsmapsdb3 = np.array(mapsThree)
vsmapsdb4 = np.array(mapsFour)
vsmapsdb5 = np.array(mapsFive)
vsmapsdb = np.array(maps)

# USING DB - not used
# vsmaps = np.array(["1. 2 Evil Eyes: http://www.spirit.hosted.nfoservers.com/2evileyes.rar",
#                    "2. 25 To Life: http://www.spirit.hosted.nfoservers.com/25tolife.rar",
#                    "3. Back To School: http://www.spirit.hosted.nfoservers.com/bts_l4d2.rar",
#                    "4. Blood Tracks: http://www.spirit.hosted.nfoservers.com/bloodtracks.rar",
#                    "5. Bloody Moors: http://www.spirit.hosted.nfoservers.com/l4d2_thebloodymoors.rar",
#                    "6. BigWat: http://www.spirit.hosted.nfoservers.com/bigwat.rar",
#                    "7. Carried Off: http://www.spirit.hosted.nfoservers.com/carriedoff.rar",
#                    "8. City 17: http://www.spirit.hosted.nfoservers.com/city17l4d2.rar",
#                    "9. Damit 2: http://www.spirit.hosted.nfoservers.com/damit2dc_v1.rar",
#                    "10 . Dark Blood: http://www.spirit.hosted.nfoservers.com/darkblood2_v3.rar",
#                    "11. Dark Carnival Remix: http://www.spirit.hosted.nfoservers.com/dark%20carnival%20remix.zip",
#                    "12. Dark Mesa: http://www.spirit.hosted.nfoservers.com/pitchdarkmesa.rar",
#                    "13. Dark Parish: http://www.spirit.hosted.nfoservers.com/thedarkparish_av3.rar",
#                    "14. Daybreak: http://www.spirit.hosted.nfoservers.com/daybreak_v2.rar",
#                    "15. DeadBeat Escape: http://www.spirit.hosted.nfoservers.com/deadbeatescape.rar",
#                    "16. Dead Before Dawn 2: http://www.spirit.hosted.nfoservers.com/deadbeforedawn2_dc.rar",
#                    "17. Dead City: http://www.spirit.hosted.nfoservers.com/deadcity2.rar",
#                    "18. Dead Echo: http://www.spirit.hosted.nfoservers.com/echo.rar",
#                    "19. Dead On Time: http://www.spirit.hosted.nfoservers.com/deadontime2.rar  (Finale scoring is broken)",
#                    "20. Dead Series: http://www.spirit.hosted.nfoservers.com/deadseries.rar",
#                    "21. Death Aboard 2: http://www.spirit.hosted.nfoservers.com/deathaboard2.rar",
#                    "22. Death Sentence: http://www.spirit.hosted.nfoservers.com/deathsentence.rar  (Players crash constantly)",
#                    "23. Detour Ahead: http://www.spirit.hosted.nfoservers.com/detourahead.rar",
#                    "24. Diescraper Redux: http://www.spirit.hosted.nfoservers.com/l4d2_diescraper-redux_2413_v3_62.zip",
#                    "25. Dneipr: http://www.spirit.hosted.nfoservers.com/dniepr.rar",
#                    "26. Downtown Dine: http://www.spirit.hosted.nfoservers.com/downtowndine.rar",
#                    "27. Drop Dead Gorges: http://www.spirit.hosted.nfoservers.com/ddg_v2_1.rar",
#                    "28. Energy Crisis: http://www.spirit.hosted.nfoservers.com/energycrisis.zip",
#                    "29. Fall In Death: http://www.spirit.hosted.nfoservers.com/fallindeath.rar",
#                    "30. Fallen: http://www.spirit.hosted.nfoservers.com/l4d2_fallen-l4d2_6352_v10_0.zip",
#                    "31. Fatal Freight: http://www.spirit.hosted.nfoservers.com/l4d2_fatal-freight-fixed.zip",
#                    "32. Freezer Burn: http://www.spirit.hosted.nfoservers.com/l4d2_freezer_burn_8.0.zip  (Tank spawns right out of the saferoom)",
#                    "33. Gas Fever: http://www.spirit.hosted.nfoservers.com/gasfever.zip",
#                    "34. Golden Eye 4 Dead: http://www.spirit.hosted.nfoservers.com/goldeneye.rar",
#                    "35. Haunted Forest: http://www.spirit.hosted.nfoservers.com/hauntedforest_v3.rar",
#                    "36. Heaven Can Wait: http://www.spirit.hosted.nfoservers.com/heavencanwaitl4d2.rar (Finale has fps drops due to lights)",
#                    "37. I Hate Mountains 2: http://www.spirit.hosted.nfoservers.com/ihatemountains2.rar",
#                    "38. Kokiri Forest: http://www.spirit.hosted.nfoservers.com/oot.rar",
#                    "39. Last Summer: http://www.spirit.hosted.nfoservers.com/l4d2lastsummer5.rar",
#                    "40. Left 4 Duluth: http://www.spirit.hosted.nfoservers.com/left4duluth.rar",
#                    "41. Left 4 Mario: http://www.spirit.hosted.nfoservers.com/mario2.rar",
#                    "42. Lost: http://www.spirit.hosted.nfoservers.com/lostv2_fixed.rar",
#                    "43. One 4 Nine: http://www.spirit.hosted.nfoservers.com/l4d2_one4nine.rar",
#                    "44. Open Road: http://www.spirit.hosted.nfoservers.com/openroad.rar",
#                    "45. Plan B: http://www.spirit.hosted.nfoservers.com/l4d2_plan_b_v051.rar",
#                    "46. Precinct 84: http://www.spirit.hosted.nfoservers.com/precinct84_l4d2.rar",
#                    "47. Ravenholm: http://www.spirit.hosted.nfoservers.com/l4d2_ravenholmwar.rar",
#                    "48. RMS Titanic: http://www.spirit.hosted.nfoservers.com/rmstitanic.rar",
#                    "49. Road to Nowhere: http://www.spirit.hosted.nfoservers.com/roadtonowhere2.rar",
#                    "51. Run to The Hills: http://www.spirit.hosted.nfoservers.com/runtothehills.rar",
#                    "52. Silent Hill: Other Side of Life http://www.spirit.hosted.nfoservers.com/silenthillool_4_7.rar",
#                    "53. Suicide Blitz 2: http://www.spirit.hosted.nfoservers.com/suicideblitz2.rar",
#                    "54. Surrounded By Dead: http://www.spirit.hosted.nfoservers.com/sbtd_l4d2.rar",
#                    "55. The Last Volt: http://www.spirit.hosted.nfoservers.com/thelastvolt.zip",
#                    "56. Tour of Terror: http://www.spirit.hosted.nfoservers.com/tourofterror.rar",
#                    "57. True Fangshi: http://www.spirit.hosted.nfoservers.com/true_fangshi.rar",
#                    "58. Urban Flight: http://www.spirit.hosted.nfoservers.com/urbanflight.rar",
#                    "59. Wan li: http://www.spirit.hosted.nfoservers.com/wanli_v4.rar",
#                    "60. Warcelona: http://www.spirit.hosted.nfoservers.com/warcelona.rar",
#                    "61. Whispers of Winter: http://www.spirit.hosted.nfoservers.com/l4d2_whispers-of-winter_20760_v1_4.zip",
#                    "62. White Forest: http://www.spirit.hosted.nfoservers.com/white_forest.rar",
#                    "63. Wild Ride1: http://www.spirit.hosted.nfoservers.com/wildride.zip",
#                    "64. Wild Ride2: http://www.spirit.hosted.nfoservers.com/wildride.z0",
#                    "65. Yama: http://www.spirit.hosted.nfoservers.com/l4d_yama_v6.rar (Finale requires plugins to be turned off)"])
