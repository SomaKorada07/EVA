###### NAME: SOMA KORADA

###### BATCH: S9

###### EMAIL ID: somakorada@gmail.com

# ASSIGNMENT 1B

## What are Channels and Kernels (according to EVA)?

**Channels** are similar kind of information or feature grouped or containerized together and given a name. For instance, all red color information will be grouped under red channel, all blue information will be grouped under blue channel, etc. We can divide an image into as many number of channels as we wish.

**Kernels** are the ones used to extract similar kind of information. Kernels are instrumental in deriving channel information. Kernels are also called as **Feature Extractors** or **Filters** or **3x3 matrix**.





## Why should we only (well mostly) use 3x3 Kernels?

3x3 kernels are mostly used because of equal division between left and right parts of the image. We could use 5x5, 7x7, etc but for **computational benefits**, 3x3 is preferred to the other odd sized kernels. 3x3 also leads to **less number of parameters** when compared to other odd sized kernels. Using 7x7 kernel once is equivalent to using 3x3 kernel 3 times (same receptive field of 7.) However, while using 7x7 kernel, the number of parameters are (7\*7) = 49. But on using 3x3 kernel 3 times, the number of parameters are 3 * (3\*3) = 27.

​	



## How many times do we need to perform 3x3 convolution operation to reach 1x1 from 199x199 (show calculations)

**99 times**

1. 199x199 convolved using 3x3 matrix resulting in 197x197
2. 197x197 convolved using 3x3 matrix resulting in 195x195
3. 195x195 convolved using 3x3 matrix resulting in 193x193
4. 193x193 convolved using 3x3 matrix resulting in 191x191
5. 191x191 convolved using 3x3 matrix resulting in 189x189
6. 189x189 convolved using 3x3 matrix resulting in 187x187
7. 187x187 convolved using 3x3 matrix resulting in 185x185
8. 185x185 convolved using 3x3 matrix resulting in 183x183
9. 183x183 convolved using 3x3 matrix resulting in 181x181
10. 181x181 convolved using 3x3 matrix resulting in 179x179
11. 179x179 convolved using 3x3 matrix resulting in 177x177
12. 177x177 convolved using 3x3 matrix resulting in 175x175
13. 175x175 convolved using 3x3 matrix resulting in 173x173
14. 173x173 convolved using 3x3 matrix resulting in 171x171
15. 171x171 convolved using 3x3 matrix resulting in 169x169
16. 169x169 convolved using 3x3 matrix resulting in 167x167
17. 167x167 convolved using 3x3 matrix resulting in 165x165
18. 165x165 convolved using 3x3 matrix resulting in 163x163
19. 163x163 convolved using 3x3 matrix resulting in 161x161
20. 161x161 convolved using 3x3 matrix resulting in 159x159
21. 159x159 convolved using 3x3 matrix resulting in 157x157
22. 157x157 convolved using 3x3 matrix resulting in 155x155
23. 155x155 convolved using 3x3 matrix resulting in 153x153
24. 153x153 convolved using 3x3 matrix resulting in 151x151
25. 151x151 convolved using 3x3 matrix resulting in 149x149
26. 149x149 convolved using 3x3 matrix resulting in 147x147
27. 147x147 convolved using 3x3 matrix resulting in 145x145
28. 145x145 convolved using 3x3 matrix resulting in 143x143
29. 143x143 convolved using 3x3 matrix resulting in 141x141
30. 141x141 convolved using 3x3 matrix resulting in 139x139
31. 139x139 convolved using 3x3 matrix resulting in 137x137
32. 137x137 convolved using 3x3 matrix resulting in 135x135
33. 135x135 convolved using 3x3 matrix resulting in 133x133
34. 133x133 convolved using 3x3 matrix resulting in 131x131
35. 131x131 convolved using 3x3 matrix resulting in 129x129
36. 129x129 convolved using 3x3 matrix resulting in 127x127
37. 127x127 convolved using 3x3 matrix resulting in 125x125
38. 125x125 convolved using 3x3 matrix resulting in 123x123
39. 123x123 convolved using 3x3 matrix resulting in 121x121
40. 121x121 convolved using 3x3 matrix resulting in 119x119
41. 119x119 convolved using 3x3 matrix resulting in 117x117
42. 117x117 convolved using 3x3 matrix resulting in 115x115
43. 115x115 convolved using 3x3 matrix resulting in 113x113
44. 113x113 convolved using 3x3 matrix resulting in 111x111
45. 111x111 convolved using 3x3 matrix resulting in 109x109
46. 109x109 convolved using 3x3 matrix resulting in 107x107
47. 107x107 convolved using 3x3 matrix resulting in 105x105
48. 105x105 convolved using 3x3 matrix resulting in 103x103
49. 103x103 convolved using 3x3 matrix resulting in 101x101
50. 101x101 convolved using 3x3 matrix resulting in 99x99
51. 99x99 convolved using 3x3 matrix resulting in 97x97
52. 97x97 convolved using 3x3 matrix resulting in 95x95
53. 95x95 convolved using 3x3 matrix resulting in 93x93
54. 93x93 convolved using 3x3 matrix resulting in 91x91
55. 91x91 convolved using 3x3 matrix resulting in 89x89
56. 89x89 convolved using 3x3 matrix resulting in 87x87
57. 87x87 convolved using 3x3 matrix resulting in 85x85
58. 85x85 convolved using 3x3 matrix resulting in 83x83
59. 83x83 convolved using 3x3 matrix resulting in 81x81
60. 81x81 convolved using 3x3 matrix resulting in 79x79
61. 79x79 convolved using 3x3 matrix resulting in 77x77
62. 77x77 convolved using 3x3 matrix resulting in 75x75
63. 75x75 convolved using 3x3 matrix resulting in 73x73
64. 73x73 convolved using 3x3 matrix resulting in 71x71
65. 71x71 convolved using 3x3 matrix resulting in 69x69
66. 69x69 convolved using 3x3 matrix resulting in 67x67
67. 67x67 convolved using 3x3 matrix resulting in 65x65
68. 65x65 convolved using 3x3 matrix resulting in 63x63
69. 63x63 convolved using 3x3 matrix resulting in 61x61
70. 61x61 convolved using 3x3 matrix resulting in 59x59
71. 59x59 convolved using 3x3 matrix resulting in 57x57
72. 57x57 convolved using 3x3 matrix resulting in 55x55
73. 55x55 convolved using 3x3 matrix resulting in 53x53
74. 53x53 convolved using 3x3 matrix resulting in 51x51
75. 51x51 convolved using 3x3 matrix resulting in 49x49
76. 49x49 convolved using 3x3 matrix resulting in 47x47
77. 47x47 convolved using 3x3 matrix resulting in 45x45
78. 45x45 convolved using 3x3 matrix resulting in 43x43
79. 43x43 convolved using 3x3 matrix resulting in 41x41
80. 41x41 convolved using 3x3 matrix resulting in 39x39
81. 39x39 convolved using 3x3 matrix resulting in 37x37
82. 37x37 convolved using 3x3 matrix resulting in 35x35
83. 35x35 convolved using 3x3 matrix resulting in 33x33
84. 33x33 convolved using 3x3 matrix resulting in 31x31
85. 31x31 convolved using 3x3 matrix resulting in 29x29
86. 29x29 convolved using 3x3 matrix resulting in 27x27
87. 27x27 convolved using 3x3 matrix resulting in 25x25
88. 25x25 convolved using 3x3 matrix resulting in 23x23
89. 23x23 convolved using 3x3 matrix resulting in 21x21
90. 21x21 convolved using 3x3 matrix resulting in 19x19
91. 19x19 convolved using 3x3 matrix resulting in 17x17
92. 17x17 convolved using 3x3 matrix resulting in 15x15
93. 15x15 convolved using 3x3 matrix resulting in 13x13
94. 13x13 convolved using 3x3 matrix resulting in 11x11
95. 11x11 convolved using 3x3 matrix resulting in 9x9
96. 9x9 convolved using 3x3 matrix resulting in 7x7
97. 7x7 convolved using 3x3 matrix resulting in 5x5
98. 5x5 convolved using 3x3 matrix resulting in 3x3
99. 3x3 convolved using 3x3 matrix resulting in 1x1
