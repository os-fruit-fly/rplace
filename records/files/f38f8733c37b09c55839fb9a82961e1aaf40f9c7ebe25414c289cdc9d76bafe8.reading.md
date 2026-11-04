# When to stop, stage B1

Written by `tools/saturation.py report` at 2026-10-11T06:40:07Z. The rule: `saturation.py` docstring; J, 2026-09-29.

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
| check-in: 60% of the words read before marker 3 | 408 | 423.8 | 0.996 | 24.24 | 60.1% |

Marker 1's empty run, from the last new kind (room 421, 434.9 average rooms) to marker 1: 72.1 average rooms and 78 rooms. It is the second pass's target, never fewer than 30 rooms.

## The draw

86 rooms drawn at random from the 131 unread at marker 2, 195182 words (the three rounds between the markers read 193932); 0 brought a new kind. With 95% confidence, 3 or more unread rooms carrying an unseen kind are ruled out.

What is left (0.0 average rooms) is no larger than the draw was (74.5): reading everything costs no more than the draw did.

## The rounds

| round | began at room | predicted next kind in | length (average rooms) | coverage | unseen | result |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 132 | 4.4 | 4.3 | 0.9835 | 26.27 | new |
| 2 | 155 | 5.2 | 5.4 | 0.9883 | 37.26 | new |
| 3 | 180 | 5.2 | 5.3 | 0.9882 | 43.51 | empty |
| 4 | 188 | 5.7 | 5.8 | 0.9894 | 38.69 | new |
| 5 | 217 | 7.0 | 6.8 | 0.9912 | 34.16 | empty |
| 6 | 228 | 7.4 | 7.2 | 0.9916 | 34.17 | empty |
| 7 | 236 | 7.9 | 7.6 | 0.9921 | 32.01 | new |
| 8 | 284 | 8.9 | 8.7 | 0.9932 | 31.89 | empty |
| 9 | 290 | 9.4 | 9.4 | 0.9936 | 29.93 | empty |
| 10 | 301 | 9.7 | 9.6 | 0.9938 | 36.84 | new |
| 11 | 319 | 11.4 | 11.3 (over 10) | 0.9947 | 24.42 | new |
| 12 | 342 | 12.3 | 12.5 (over 10) | 0.995 | 26.06 | new |
| 13 | 355 | 12.7 | 12.9 (over 10) | 0.9952 | 24.43 | new |
| 14 | 386 | 14.9 | 15.1 (over 10) | 0.9959 | 17.74 | new |
| 15 | 432 | 17.3 | 17.8 (over 10) | 0.9966 | 20.79 | empty |
| 16 | 459 | 20.9 | 21.1 (over 10) | 0.9972 | 15.09 | empty |
| 17 | 476 | 21.7 | 22.1 (over 10) | 0.9973 | 16.1 | empty |
| 18 | 499 | 22.7 | 23.1 (over 10) | 0.9974 | 18.58 | empty |
| 19 | 528 | 25.2 | 25 (over 10) | 0.9977 | 20.01 | empty |
| 20 | 548 | 26.1 | 25 (over 10) | 0.9978 | 20.01 | empty |

Resets (a new kind inside a round or the draw): 9.

## When each kind first came

| kind | room | rooms read | average rooms read |
|---|---|---:|---:|
| T3-005 | sixers | 1 | 1.0 |
| T3-002 | sixers | 1 | 1.0 |
| T3-009 | sixers | 1 | 1.0 |
| T3-011 | sixers | 1 | 1.0 |
| T3-018 | sixers | 1 | 1.0 |
| T3-008 | sixers | 1 | 1.0 |
| T3-013 | sixers | 1 | 1.0 |
| T3-016 | sixers | 1 | 1.0 |
| T3-007 | sixers | 1 | 1.0 |
| T3-006 | sixers | 1 | 1.0 |
| T3-019 | sixers | 1 | 1.0 |
| T3-012 | sixers | 1 | 1.0 |
| T3-010 | sixers | 1 | 1.0 |
| T3-003 | sixers | 1 | 1.0 |
| T3-017 | sixers | 1 | 1.0 |
| T3-014 | sixers | 1 | 1.0 |
| T3-001 | sixers | 1 | 1.0 |
| T3-004 | sixers | 1 | 1.0 |
| T3-015 | sixers | 1 | 1.0 |
| T3-028 | edmontonoilers | 2 | 2.1 |
| T3-025 | edmontonoilers | 2 | 2.1 |
| T3-021 | edmontonoilers | 2 | 2.1 |
| T3-029 | edmontonoilers | 2 | 2.1 |
| T3-023 | edmontonoilers | 2 | 2.1 |
| T3-026 | edmontonoilers | 2 | 2.1 |
| T3-022 | edmontonoilers | 2 | 2.1 |
| T3-024 | edmontonoilers | 2 | 2.1 |
| T3-020 | edmontonoilers | 2 | 2.1 |
| T3-030 | edmontonoilers | 2 | 2.1 |
| T3-027 | edmontonoilers | 2 | 2.1 |
| T3-037 | chess | 3 | 3.0 |
| T3-032 | chess | 3 | 3.0 |
| T3-031 | chess | 3 | 3.0 |
| T3-033 | chess | 3 | 3.0 |
| T3-035 | chess | 3 | 3.0 |
| T3-036 | chess | 3 | 3.0 |
| T3-034 | chess | 3 | 3.0 |
| T3-041 | lifeisstrange | 4 | 3.7 |
| T3-038 | lifeisstrange | 4 | 3.7 |
| T3-039 | lifeisstrange | 4 | 3.7 |
| T3-040 | lifeisstrange | 4 | 3.7 |
| T3-045 | worldpowers | 5 | 4.2 |
| T3-042 | worldpowers | 5 | 4.2 |
| T3-046 | worldpowers | 5 | 4.2 |
| T3-043 | worldpowers | 5 | 4.2 |
| T3-047 | worldpowers | 5 | 4.2 |
| T3-044 | worldpowers | 5 | 4.2 |
| T3-052 | leagueoflegends | 6 | 12.2 |
| T3-048 | leagueoflegends | 6 | 12.2 |
| T3-050 | leagueoflegends | 6 | 12.2 |
| T3-051 | leagueoflegends | 6 | 12.2 |
| T3-049 | leagueoflegends | 6 | 12.2 |
| T3-054 | leagueoflegends | 6 | 12.2 |
| T3-053 | leagueoflegends | 6 | 12.2 |
| T3-057 | rutgers | 7 | 13.7 |
| T3-058 | rutgers | 7 | 13.7 |
| T3-055 | rutgers | 7 | 13.7 |
| T3-059 | rutgers | 7 | 13.7 |
| T3-056 | rutgers | 7 | 13.7 |
| T3-061 | drugs | 8 | 14.9 |
| T3-062 | drugs | 8 | 14.9 |
| T3-064 | drugs | 8 | 14.9 |
| T3-060 | drugs | 8 | 14.9 |
| T3-063 | drugs | 8 | 14.9 |
| T3-067 | thailand | 9 | 16.1 |
| T3-068 | thailand | 9 | 16.1 |
| T3-065 | thailand | 9 | 16.1 |
| T3-066 | thailand | 9 | 16.1 |
| T3-073 | undertale | 10 | 17.9 |
| T3-069 | undertale | 10 | 17.9 |
| T3-071 | undertale | 10 | 17.9 |
| T3-072 | undertale | 10 | 17.9 |
| T3-070 | undertale | 10 | 17.9 |
| T3-075 | rpi | 11 | 18.7 |
| T3-074 | rpi | 11 | 18.7 |
| T3-076 | Mario | 12 | 18.9 |
| T3-077 | Mario | 12 | 18.9 |
| T3-080 | lithuania | 13 | 19.5 |
| T3-081 | lithuania | 13 | 19.5 |
| T3-078 | lithuania | 13 | 19.5 |
| T3-079 | lithuania | 13 | 19.5 |
| T3-082 | RelientK | 15 | 20.3 |
| T3-083 | faeria | 16 | 20.8 |
| T3-084 | faeria | 16 | 20.8 |
| T3-086 | bitcoin | 17 | 23.5 |
| T3-085 | bitcoin | 17 | 23.5 |
| T3-087 | criticalrole | 18 | 24.1 |
| T3-092 | criticalrole | 18 | 24.1 |
| T3-089 | criticalrole | 18 | 24.1 |
| T3-088 | criticalrole | 18 | 24.1 |
| T3-091 | criticalrole | 18 | 24.1 |
| T3-090 | criticalrole | 18 | 24.1 |
| T3-094 | seahawks | 19 | 25.1 |
| T3-093 | seahawks | 19 | 25.1 |
| T3-098 | minecraft | 20 | 26.7 |
| T3-095 | minecraft | 20 | 26.7 |
| T3-097 | minecraft | 20 | 26.7 |
| split:T3-023+T3-048+T3-095 | minecraft | 20 | 26.7 |
| T3-096 | minecraft | 20 | 26.7 |
| T3-099 | bretagne | 23 | 28.7 |
| T3-100 | mls | 24 | 31.1 |
| T3-101 | mls | 24 | 31.1 |
| T3-102 | nyjets | 25 | 32.1 |
| T3-104 | monalisaclan | 26 | 33.5 |
| T3-105 | monalisaclan | 26 | 33.5 |
| T3-103 | monalisaclan | 26 | 33.5 |
| T3-107 | samuraijack | 29 | 37.2 |
| T3-106 | samuraijack | 29 | 37.2 |
| T3-109 | archlinux | 30 | 39.0 |
| T3-108 | archlinux | 30 | 39.0 |
| T3-111 | pgang | 38 | 43.0 |
| T3-110 | pgang | 38 | 43.0 |
| T3-112 | warframe | 39 | 44.6 |
| T3-113 | norge | 41 | 47.3 |
| T3-114 | norge | 41 | 47.3 |
| T3-115 | radiohead | 43 | 49.8 |
| T3-116 | lakers | 44 | 51.5 |
| T3-117 | lakers | 44 | 51.5 |
| T3-118 | chelseafc | 46 | 53.7 |
| T3-119 | albania | 49 | 55.5 |
| T3-120 | albania | 49 | 55.5 |
| T3-121 | uoft | 50 | 56.7 |
| T3-122 | germany | 51 | 57.5 |
| T3-123 | placeportalpattern | 52 | 58.4 |
| T3-125 | southafrica | 54 | 59.5 |
| T3-124 | southafrica | 54 | 59.5 |
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
| T3-138 | kamenrider | 99 | 99.1 |
| T3-139 | homelab | 100 | 99.7 |
| T3-140 | japan | 105 | 101.6 |
| T3-142 | canucks | 111 | 110.0 |
| T3-141 | canucks | 111 | 110.0 |
| T3-143 | canucks | 111 | 110.0 |
| T3-144 | loliconsunite | 114 | 113.7 |
| T3-145 | theitalyplace | 118 | 118.4 |
| T3-146 | PinkVomitMonster | 119 | 118.9 |
| T3-147 | starlightstage | 120 | 119.6 |
| T3-148 | pcmasterrace | 134 | 136.0 |
| T3-159 | formula1 | 141 | 142.6 |
| T3-149 | formula1 | 141 | 142.6 |
| T3-160 | formula1 | 141 | 142.6 |
| T3-150 | formula1 | 141 | 142.6 |
| T3-157 | formula1 | 141 | 142.6 |
| T3-153 | formula1 | 141 | 142.6 |
| T3-154 | formula1 | 141 | 142.6 |
| T3-155 | formula1 | 141 | 142.6 |
| T3-161 | formula1 | 141 | 142.6 |
| split:T3-010+T3-149+T3-150+T3-151 | formula1 | 141 | 142.6 |
| T3-151 | formula1 | 141 | 142.6 |
| T3-156 | formula1 | 141 | 142.6 |
| T3-158 | formula1 | 141 | 142.6 |
| split:T3-014+T3-152+T3-153 | formula1 | 141 | 142.6 |
| T3-152 | formula1 | 141 | 142.6 |
| split:T3-009+T3-154+T3-155+T3-156+T3-157 | formula1 | 141 | 142.6 |
| T3-162 | greenlattice | 143 | 148.2 |
| T3-163 | greenlattice | 143 | 148.2 |
| T3-164 | traaaaaaannnnnnnnnns | 157 | 161.8 |
| T3-166 | greece | 158 | 162.9 |
| T3-165 | greece | 158 | 162.9 |
| T3-167 | dbz | 160 | 164.7 |
| T3-168 | neu | 162 | 165.8 |
| T3-169 | halo | 165 | 168.9 |
| T3-170 | halo | 165 | 168.9 |
| T3-173 | AprilKnights | 170 | 173.2 |
| T3-172 | AprilKnights | 170 | 173.2 |
| T3-171 | AprilKnights | 170 | 173.2 |
| T3-174 | orderofthebluecorner | 196 | 195.5 |
| T3-195 | nVade | 201 | 197.0 |
| T3-175 | furry_irl | 206 | 201.7 |
| T3-176 | utaustin | 241 | 233.4 |
| T3-178 | dankmemes | 242 | 235.9 |
| T3-177 | dankmemes | 242 | 235.9 |
| T3-179 | anarcho_capitalism | 249 | 241.6 |
| T3-180 | korea | 255 | 246.1 |
| T3-181 | cubers | 259 | 254.7 |
| T3-184 | kanye | 267 | 261.3 |
| T3-182 | kanye | 267 | 261.3 |
| T3-183 | kanye | 267 | 261.3 |
| T3-185 | warthunder | 273 | 265.4 |
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
