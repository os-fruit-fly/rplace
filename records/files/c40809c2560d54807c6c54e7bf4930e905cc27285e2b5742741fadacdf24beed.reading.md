# When to stop, stage B1

Written by `tools/saturation.py report` at 2026-10-11T14:41:42Z. The rule: `saturation.py` docstring; J, 2026-09-29.

The thresholds (10 average rooms before a round, rounds of at most 25, three empty rounds to a marker, the check-in at 60% of the words) are this design's discovery heuristic, J's recorded choice (2026-09-29). The literature gives the rule its form, a run with nothing new after a base; it does not fix these numbers.

## Where the reading stands

| | |
|---|---:|
| rooms read | 705 of 705 |
| share of the words read | 100.0% |
| rooms left | 0 |
| words left, in average rooms (2604.4 words each) | 0.0 |
| kinds seen | 202 |
| coverage now | 0.9985 |
| unseen kinds estimated now | 20.03 |
| state | end |

## The markers

| marker | rooms read | average rooms read | coverage | unseen kinds | share of words |
|---|---:|---:|---:|---:|---:|
| 1: three empty rounds (the first stop) | 499 | 507.0 | 0.9974 | 18.58 | 71.9% |
| 2: three more empty rounds | 574 | 581.5 | 0.9979 | 20.01 | 82.5% |
| 3: the draw read | 660 | 656.4 | 0.9983 | 18.02 | 93.1% |
| check-in: 60% of the words read before marker 3 | 408 | 423.8 | 0.9962 | 21.07 | 60.1% |

Marker 1's empty run, from the last new kind (room 421, 434.9 average rooms) to marker 1: 72.1 average rooms and 78 rooms. It is the second pass's target, never fewer than 30 rooms.

## The draw

86 rooms drawn at random from the 131 unread at marker 2, 195182 words (the three rounds between the markers read 193932); 0 brought a new kind. With 95% confidence, 3 or more unread rooms carrying an unseen kind are ruled out.

What is left (0.0 average rooms) is no larger than the draw was (74.5): reading everything costs no more than the draw did.

## The rounds

| round | began at room | predicted next kind in | length (average rooms) | coverage | unseen | result |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 132 | 4.3 | 4.2 | 0.9829 | 28.05 | new |
| 2 | 155 | 5.0 | 5.2 | 0.9879 | 39.78 | new |
| 3 | 180 | 5.3 | 5.4 | 0.9886 | 38.32 | empty |
| 4 | 188 | 5.7 | 5.8 | 0.9894 | 41.66 | new |
| 5 | 217 | 6.8 | 6.6 | 0.991 | 36.4 | empty |
| 6 | 228 | 7.2 | 7.0 | 0.9913 | 36.41 | empty |
| 7 | 235 | 7.6 | 7.4 | 0.9918 | 34.18 | new |
| 8 | 284 | 9.2 | 9.0 | 0.9934 | 28.17 | empty |
| 9 | 290 | 9.7 | 9.7 | 0.9938 | 26.38 | empty |
| 10 | 301 | 10.1 | 10.0 (over 10) | 0.994 | 32.04 | new |
| 11 | 319 | 11.9 | 11.8 (over 10) | 0.9949 | 21.37 | new |
| 12 | 342 | 12.7 | 12.9 (over 10) | 0.9952 | 22.71 | new |
| 13 | 355 | 13.2 | 13.4 (over 10) | 0.9954 | 21.38 | new |
| 14 | 386 | 15.5 | 15.7 (over 10) | 0.9961 | 15.58 | new |
| 15 | 432 | 17.3 | 17.8 (over 10) | 0.9966 | 22.27 | empty |
| 16 | 459 | 20.9 | 21.1 (over 10) | 0.9972 | 16.1 | empty |
| 17 | 476 | 21.7 | 22.1 (over 10) | 0.9973 | 16.1 | empty |
| 18 | 499 | 22.7 | 23.1 (over 10) | 0.9974 | 18.58 | empty |
| 19 | 528 | 25.2 | 25 (over 10) | 0.9977 | 20.01 | empty |
| 20 | 548 | 26.1 | 25 (over 10) | 0.9978 | 20.01 | empty |

Resets (a new kind inside a round or the draw): 9.

## When each kind first came

| kind | room | rooms read | average rooms read |
|---|---|---:|---:|
| T3-007 | sixers | 1 | 1.0 |
| T3-019 | sixers | 1 | 1.0 |
| T3-018 | sixers | 1 | 1.0 |
| T3-011 | sixers | 1 | 1.0 |
| T3-005 | sixers | 1 | 1.0 |
| T3-003 | sixers | 1 | 1.0 |
| T3-010 | sixers | 1 | 1.0 |
| T3-002 | sixers | 1 | 1.0 |
| T3-012 | sixers | 1 | 1.0 |
| T3-008 | sixers | 1 | 1.0 |
| T3-006 | sixers | 1 | 1.0 |
| T3-013 | sixers | 1 | 1.0 |
| T3-016 | sixers | 1 | 1.0 |
| T3-009 | sixers | 1 | 1.0 |
| T3-004 | sixers | 1 | 1.0 |
| T3-017 | sixers | 1 | 1.0 |
| T3-014 | sixers | 1 | 1.0 |
| T3-001 | sixers | 1 | 1.0 |
| T3-015 | sixers | 1 | 1.0 |
| T3-025 | edmontonoilers | 2 | 2.1 |
| T3-023 | edmontonoilers | 2 | 2.1 |
| T3-028 | edmontonoilers | 2 | 2.1 |
| T3-026 | edmontonoilers | 2 | 2.1 |
| T3-020 | edmontonoilers | 2 | 2.1 |
| T3-022 | edmontonoilers | 2 | 2.1 |
| T3-021 | edmontonoilers | 2 | 2.1 |
| T3-029 | edmontonoilers | 2 | 2.1 |
| T3-027 | edmontonoilers | 2 | 2.1 |
| T3-024 | edmontonoilers | 2 | 2.1 |
| T3-030 | edmontonoilers | 2 | 2.1 |
| T3-036 | chess | 3 | 3.0 |
| T3-035 | chess | 3 | 3.0 |
| T3-032 | chess | 3 | 3.0 |
| T3-031 | chess | 3 | 3.0 |
| T3-033 | chess | 3 | 3.0 |
| T3-034 | chess | 3 | 3.0 |
| T3-037 | chess | 3 | 3.0 |
| T3-041 | lifeisstrange | 4 | 3.7 |
| T3-038 | lifeisstrange | 4 | 3.7 |
| T3-040 | lifeisstrange | 4 | 3.7 |
| T3-039 | lifeisstrange | 4 | 3.7 |
| T3-047 | worldpowers | 5 | 4.2 |
| T3-042 | worldpowers | 5 | 4.2 |
| T3-044 | worldpowers | 5 | 4.2 |
| T3-043 | worldpowers | 5 | 4.2 |
| T3-045 | worldpowers | 5 | 4.2 |
| T3-046 | worldpowers | 5 | 4.2 |
| T3-053 | leagueoflegends | 6 | 12.2 |
| T3-050 | leagueoflegends | 6 | 12.2 |
| T3-052 | leagueoflegends | 6 | 12.2 |
| T3-049 | leagueoflegends | 6 | 12.2 |
| T3-054 | leagueoflegends | 6 | 12.2 |
| T3-051 | leagueoflegends | 6 | 12.2 |
| T3-048 | leagueoflegends | 6 | 12.2 |
| T3-057 | rutgers | 7 | 13.7 |
| T3-059 | rutgers | 7 | 13.7 |
| T3-055 | rutgers | 7 | 13.7 |
| T3-058 | rutgers | 7 | 13.7 |
| T3-056 | rutgers | 7 | 13.7 |
| T3-060 | drugs | 8 | 14.9 |
| T3-063 | drugs | 8 | 14.9 |
| T3-064 | drugs | 8 | 14.9 |
| T3-061 | drugs | 8 | 14.9 |
| T3-062 | drugs | 8 | 14.9 |
| T3-067 | thailand | 9 | 16.1 |
| T3-066 | thailand | 9 | 16.1 |
| T3-068 | thailand | 9 | 16.1 |
| T3-065 | thailand | 9 | 16.1 |
| T3-070 | undertale | 10 | 17.9 |
| T3-069 | undertale | 10 | 17.9 |
| T3-071 | undertale | 10 | 17.9 |
| T3-073 | undertale | 10 | 17.9 |
| T3-072 | undertale | 10 | 17.9 |
| T3-075 | rpi | 11 | 18.7 |
| T3-074 | rpi | 11 | 18.7 |
| T3-077 | Mario | 12 | 18.9 |
| T3-076 | Mario | 12 | 18.9 |
| T3-078 | lithuania | 13 | 19.5 |
| T3-081 | lithuania | 13 | 19.5 |
| T3-079 | lithuania | 13 | 19.5 |
| T3-080 | lithuania | 13 | 19.5 |
| T3-082 | RelientK | 15 | 20.3 |
| T3-084 | faeria | 16 | 20.8 |
| T3-083 | faeria | 16 | 20.8 |
| T3-085 | bitcoin | 17 | 23.5 |
| T3-086 | bitcoin | 17 | 23.5 |
| T3-091 | criticalrole | 18 | 24.1 |
| T3-088 | criticalrole | 18 | 24.1 |
| T3-092 | criticalrole | 18 | 24.1 |
| T3-090 | criticalrole | 18 | 24.1 |
| T3-087 | criticalrole | 18 | 24.1 |
| T3-089 | criticalrole | 18 | 24.1 |
| T3-093 | seahawks | 19 | 25.1 |
| T3-094 | seahawks | 19 | 25.1 |
| split:T3-023+T3-048+T3-095 | minecraft | 20 | 26.7 |
| T3-096 | minecraft | 20 | 26.7 |
| T3-098 | minecraft | 20 | 26.7 |
| T3-095 | minecraft | 20 | 26.7 |
| T3-097 | minecraft | 20 | 26.7 |
| T3-099 | bretagne | 23 | 28.7 |
| T3-101 | mls | 24 | 31.1 |
| T3-100 | mls | 24 | 31.1 |
| T3-102 | nyjets | 25 | 32.1 |
| T3-104 | monalisaclan | 26 | 33.5 |
| T3-105 | monalisaclan | 26 | 33.5 |
| T3-103 | monalisaclan | 26 | 33.5 |
| T3-106 | samuraijack | 29 | 37.2 |
| T3-107 | samuraijack | 29 | 37.2 |
| T3-109 | archlinux | 30 | 39.0 |
| T3-108 | archlinux | 30 | 39.0 |
| T3-111 | pgang | 38 | 43.0 |
| T3-110 | pgang | 38 | 43.0 |
| T3-112 | warframe | 39 | 44.6 |
| T3-114 | norge | 41 | 47.3 |
| T3-113 | norge | 41 | 47.3 |
| T3-115 | radiohead | 43 | 49.8 |
| T3-116 | lakers | 44 | 51.5 |
| T3-117 | lakers | 44 | 51.5 |
| T3-118 | chelseafc | 46 | 53.7 |
| T3-120 | albania | 49 | 55.5 |
| T3-119 | albania | 49 | 55.5 |
| T3-121 | uoft | 50 | 56.7 |
| T3-122 | germany | 51 | 57.5 |
| T3-123 | placeportalpattern | 52 | 58.4 |
| T3-124 | southafrica | 54 | 59.5 |
| T3-125 | southafrica | 54 | 59.5 |
| T3-126 | harrypotter | 57 | 61.9 |
| T3-127 | gameattack | 60 | 63.1 |
| T3-128 | ice_poseidon | 62 | 65.1 |
| T3-129 | fxKorea | 65 | 67.5 |
| T3-130 | scotland | 66 | 68.7 |
| T3-131 | donaldglover | 69 | 70.6 |
| T3-132 | babymetal | 73 | 75.7 |
| T3-133 | PUBATTLEGROUNDS | 75 | 77.4 |
| T3-134 | Summit1G | 77 | 79.7 |
| T3-135 | fireemblem | 81 | 85.5 |
| T3-194 | ManningPlace | 86 | 87.8 |
| T3-136 | araragi | 95 | 96.6 |
| T3-137 | araragi | 95 | 96.6 |
| T3-169 | popheads | 97 | 98.4 |
| T3-138 | kamenrider | 99 | 99.1 |
| T3-139 | homelab | 100 | 99.7 |
| T3-140 | japan | 105 | 101.6 |
| T3-142 | canucks | 111 | 110.0 |
| T3-143 | canucks | 111 | 110.0 |
| T3-141 | canucks | 111 | 110.0 |
| T3-144 | loliconsunite | 114 | 113.7 |
| T3-145 | theitalyplace | 118 | 118.4 |
| T3-146 | PinkVomitMonster | 119 | 118.9 |
| T3-147 | starlightstage | 120 | 119.6 |
| T3-148 | pcmasterrace | 134 | 136.0 |
| T3-149 | formula1 | 141 | 142.6 |
| T3-151 | formula1 | 141 | 142.6 |
| T3-153 | formula1 | 141 | 142.6 |
| split:T3-014+T3-152+T3-153 | formula1 | 141 | 142.6 |
| T3-152 | formula1 | 141 | 142.6 |
| T3-154 | formula1 | 141 | 142.6 |
| T3-161 | formula1 | 141 | 142.6 |
| T3-160 | formula1 | 141 | 142.6 |
| T3-159 | formula1 | 141 | 142.6 |
| split:T3-009+T3-154+T3-155+T3-156+T3-157 | formula1 | 141 | 142.6 |
| T3-158 | formula1 | 141 | 142.6 |
| split:T3-010+T3-149+T3-150+T3-151 | formula1 | 141 | 142.6 |
| T3-156 | formula1 | 141 | 142.6 |
| T3-155 | formula1 | 141 | 142.6 |
| T3-150 | formula1 | 141 | 142.6 |
| T3-157 | formula1 | 141 | 142.6 |
| T3-162 | greenlattice | 143 | 148.2 |
| T3-163 | greenlattice | 143 | 148.2 |
| T3-164 | traaaaaaannnnnnnnnns | 157 | 161.8 |
| T3-166 | greece | 158 | 162.9 |
| T3-165 | greece | 158 | 162.9 |
| T3-167 | dbz | 160 | 164.7 |
| T3-168 | neu | 162 | 165.8 |
| T3-170 | halo | 165 | 168.9 |
| T3-172 | AprilKnights | 170 | 173.2 |
| T3-171 | AprilKnights | 170 | 173.2 |
| T3-173 | AprilKnights | 170 | 173.2 |
| T3-174 | orderofthebluecorner | 196 | 195.5 |
| T3-195 | nVade | 201 | 197.0 |
| T3-185 | furry_irl | 206 | 201.7 |
| T3-175 | furry_irl | 206 | 201.7 |
| T3-176 | utaustin | 241 | 233.4 |
| T3-178 | dankmemes | 242 | 235.9 |
| T3-177 | dankmemes | 242 | 235.9 |
| T3-179 | anarcho_capitalism | 249 | 241.6 |
| T3-180 | korea | 255 | 246.1 |
| T3-181 | cubers | 259 | 254.7 |
| T3-183 | kanye | 267 | 261.3 |
| T3-182 | kanye | 267 | 261.3 |
| T3-184 | kanye | 267 | 261.3 |
| T3-186 | SwissNeutralityZone | 274 | 266.1 |
| T3-187 | haskell | 307 | 305.3 |
| T3-188 | ainbowroad | 332 | 334.5 |
| T3-189 | scp | 345 | 349.2 |
| T3-190 | PurplePixels | 367 | 373.5 |
| T3-191 | furry | 374 | 379.5 |
| T3-192 | paladins | 392 | 403.3 |
| T3-193 | france | 399 | 416.0 |
| split:T3-010+T3-194+T3-195 | anaheimducks | 409 | 424.5 |
| T3-196 | mindcrack | 421 | 434.9 |
| T3-197 | parahumans | 661 | 658.0 |

## The second pass (B1d)

pass 2 (B1d): met; chosen rooms read 108 of 108; rooms read in this pass 108; since its last new third-order theme 108 rooms and 148.1 average rooms, against 78 rooms and 72.1 average rooms (marker 1's empty run (72.1 average rooms, 78 rooms; floor 30 rooms))

| room | leg | new kinds | run, rooms | run, average rooms |
|---|---|---|---:|---:|
| morrowind | B1d-01 | - | 1 | 0.8 |
| Summit1G | B1d-01 | - | 2 | 1.2 |
| popheads | B1d-01 | - | 3 | 2.7 |
| homelab | B1d-01 | - | 4 | 3.2 |
| qotsa | B1d-01 | - | 5 | 3.6 |
| aeskwadraat | B1d-01 | - | 6 | 3.8 |
| falcons | B1d-01 | - | 7 | 5.3 |
| canucks | B1d-01 | - | 8 | 6.7 |
| cirkeltrek | B1d-01 | - | 9 | 7.8 |
| kurdistan | B1d-01 | - | 10 | 8.2 |
| theitalyplace | B1d-01 | - | 11 | 10.0 |
| PinkVomitMonster | B1d-01 | - | 12 | 10.5 |
| ubc | B1d-01 | - | 13 | 11.2 |
| bobross | B1d-01 | - | 14 | 11.3 |
| pcmasterrace | B1d-01 | - | 15 | 16.3 |
| mariokart | B1d-01 | - | 16 | 16.5 |
| rust | B1d-01 | - | 17 | 17.5 |
| gatech | B1d-01 | - | 18 | 18.5 |
| AprilKnights | B1d-01 | - | 19 | 19.3 |
| flashtv | B1d-01 | - | 20 | 21.1 |
| egypt | B1d-01 | - | 21 | 21.4 |
| totallynotrobots | B1d-02 | - | 22 | 23.1 |
| orderofthebluecorner | B1d-02 | - | 23 | 23.7 |
| GreenEmpire | B1d-02 | - | 24 | 23.8 |
| tenma | B1d-02 | - | 25 | 23.8 |
| nVade | B1d-02 | - | 26 | 24.3 |
| ontario | B1d-02 | - | 27 | 24.7 |
| furry_irl | B1d-02 | - | 28 | 26.2 |
| starryknights | B1d-02 | - | 29 | 26.7 |
| evedreddit | B1d-02 | - | 30 | 27.1 |
| mexico | B1d-02 | - | 31 | 29.3 |
| hellointernet | B1d-02 | - | 32 | 30.1 |
| oman | B1d-02 | - | 33 | 30.3 |
| placehfarts | B1d-02 | - | 34 | 30.4 |
| anime | B1d-02 | - | 35 | 31.7 |
| magictcg | B1d-02 | - | 36 | 34.0 |
| Redox | B1d-02 | - | 37 | 34.1 |
| utaustin | B1d-02 | - | 38 | 35.2 |
| dankmemes | B1d-02 | - | 39 | 37.7 |
| heyyea | B1d-02 | - | 40 | 38.1 |
| azores | B1d-02 | - | 41 | 38.1 |
| aoe2 | B1d-02 | - | 42 | 39.7 |
| anarcho_capitalism | B1d-02 | - | 43 | 41.3 |
| korea | B1d-02 | - | 44 | 42.4 |
| brasil | B1d-02 | - | 45 | 45.2 |
| Okami | B1d-03 | - | 46 | 45.8 |
| kanye | B1d-03 | - | 47 | 48.1 |
| glasgow | B1d-03 | - | 48 | 48.2 |
| stardewvalley | B1d-03 | - | 49 | 48.9 |
| danganronpa | B1d-03 | - | 50 | 50.2 |
| warthunder | B1d-03 | - | 51 | 51.3 |
| SwissNeutralityZone | B1d-03 | - | 52 | 51.9 |
| masseffect | B1d-03 | - | 53 | 53.7 |
| ibo | B1d-03 | - | 54 | 53.9 |
| finland | B1d-03 | - | 55 | 54.6 |
| Thegreatblackhole | B1d-03 | - | 56 | 55.0 |
| kpop | B1d-03 | - | 57 | 55.6 |
| lego | B1d-03 | - | 58 | 56.8 |
| wine | B1d-03 | - | 59 | 57.3 |
| duckgame | B1d-03 | - | 60 | 57.7 |
| cfb | B1d-03 | - | 61 | 60.7 |
| rotmg | B1d-03 | - | 62 | 62.3 |
| megaman | B1d-03 | - | 63 | 63.1 |
| ainbowroad | B1d-04 | - | 64 | 70.8 |
| dota2 | B1d-04 | - | 65 | 77.0 |
| ubreddit | B1d-04 | - | 66 | 77.4 |
| Fez | B1d-04 | - | 67 | 77.8 |
| azerbaijan | B1d-04 | - | 68 | 77.9 |
| scp | B1d-04 | - | 69 | 78.7 |
| wholesomememes | B1d-04 | - | 70 | 80.3 |
| placestart | B1d-04 | - | 71 | 82.3 |
| UNLincoln | B1d-04 | - | 72 | 82.3 |
| ukplace | B1d-04 | - | 73 | 83.1 |
| placehearts | B1d-05 | - | 74 | 85.3 |
| stardustcrusaders | B1d-05 | - | 75 | 86.9 |
| france | B1d-05 | - | 76 | 90.7 |
| cardinals | B1d-05 | - | 77 | 91.4 |
| FloydVsVoid | B1d-05 | - | 78 | 92.6 |
| ChronoTrigger | B1d-05 | - | 79 | 93.2 |
| philippines | B1d-05 | - | 80 | 96.6 |
| ireland | B1d-05 | - | 81 | 100.2 |
| Slovakia | B1d-05 | - | 82 | 100.8 |
| unitedkingdom | B1d-05 | - | 83 | 102.4 |
| hawks | B1d-05 | - | 84 | 103.8 |
| runescape | B1d-05 | - | 85 | 106.8 |
| theblackvoid | B1d-06 | - | 86 | 113.3 |
| detroitredwings | B1d-06 | - | 87 | 115.6 |
| loltyler1 | B1d-06 | - | 88 | 116.6 |
| CKCrusaders | B1d-06 | - | 89 | 117.1 |
| math | B1d-06 | - | 90 | 117.6 |
| parahumans | B1d-06 | - | 91 | 119.2 |
| PlaceNL | B1d-06 | - | 92 | 120.4 |
| vinesauce | B1d-06 | - | 93 | 121.1 |
| earthbound | B1d-06 | - | 94 | 121.9 |
| homestuck | B1d-06 | - | 95 | 123.4 |
| starcitizen | B1d-06 | - | 96 | 126.2 |
| prequelmemes | B1d-07 | - | 97 | 130.2 |
| heroesofthestorm | B1d-07 | - | 98 | 132.8 |
| rocketbeans | B1d-07 | - | 99 | 134.1 |
| ucf | B1d-07 | - | 100 | 134.9 |
| sakuragakuin | B1d-07 | - | 101 | 135.4 |
| israel | B1d-07 | - | 102 | 136.8 |
| reddevils | B1d-07 | - | 103 | 138.4 |
| lsu | B1d-07 | - | 104 | 139.4 |
| rainbowgrid | B1d-07 | - | 105 | 139.9 |
| thesilphroad | B1d-07 | - | 106 | 144.3 |
| DevonUK | B1d-07 | - | 107 | 144.5 |
| TheFarLeftSide | B1d-07 | - | 108 | 148.1 |
