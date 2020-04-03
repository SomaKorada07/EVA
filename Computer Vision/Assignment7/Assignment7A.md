# RECEPTIVE FIELD CALCULATION

## USING MAXIMUM RF (5) FROM A GROUP CONVOLUTION

| Layer No | Layer Name      | Kernel Size (k) | Stride (s) | j(in) | r(in) | j(out)=j(in)*s | Calculation r(out)=r(in)+(k-1)*j(in) |
| -------- | --------------- | --------------- | ---------- | ----- | ----- | -------------- | ------------------------------------ |
| 1        | Convolution     | 7x7             | 2          | 1     | 1     | 1*2=2          | 1+(7-1)*1=7                          |
| 2        | MaxPooling      | 3x3             | 2          | 2     | 7     | 2*2=4          | 7+(3-1)*2=11                         |
| 3        | Convolution     | 3x3             | 1          | 4     | 11    | 4*1=4          | 11+(3-1)*4=19                        |
| 4        | MaxPooling      | 3x3             | 2          | 4     | 19    | 4*2=8          | 19+(3-1)*4=27                        |
| 5        | Inception(3a)   | 5x5             | 1          | 8     | 27    | 8*1=8          | 27+(5-1)*8=59                        |
| 6        | Inception(3b)   | 5x5             | 1          | 8     | 59    | 8*1=8          | 59+(5-1)*8=91                        |
| 7        | MaxPooling      | 3x3             | 2          | 8     | 91    | 8*2=16         | 91+(3-1)*8=107                       |
| 8        | Inception(4a)   | 5x5             | 1          | 16    | 107   | 16*1=16        | 107+(5-1)*16=171                     |
| 9        | Inception(4b)   | 5x5             | 1          | 16    | 171   | 16*1=16        | 171+(5-1)*16=235                     |
| 10       | Inception(4c)   | 5x5             | 1          | 16    | 235   | 16*1=16        | 235+(5-1)*16=299                     |
| 11       | Inception(4d)   | 5x5             | 1          | 16    | 299   | 16*1=16        | 299+(5-1)*16=363                     |
| 12       | Inception(4e)   | 5x5             | 1          | 16    | 363   | 16*1=16        | 363+(5-1)*16=427                     |
| 13       | MaxPooling      | 3x3             | 2          | 16    | 427   | 16*2=32        | 427+(3-1)*16=459                     |
| 14       | Inception(5a)   | 5x5             | 1          | 32    | 459   | 32*1=32        | 459+(5-1)*32=587                     |
| 15       | Inception(5b)   | 5x5             | 1          | 32    | 587   | 32*1=32        | 587+(5-1)*32=715                     |
| 16       | Average Pooling | 7x7             | 1          | 32    | 715   | 32*1=32        | 715+(7-1)*32=907                     |



## USING RF OF 3X3 KERNEL FROM A GROUP CONVOLUTION

| Layer No | Layer Name      | Kernel Size (k) | Stride (s) | j(in) | r(in) | j(out)=j(in)*s | Calculation r(out)=r(in)+(k-1)*j(in) |
| -------- | --------------- | --------------- | ---------- | ----- | ----- | -------------- | ------------------------------------ |
| 1        | Convolution     | 7x7             | 2          | 1     | 1     | 1*2=2          | 1+(7-1)*1=7                          |
| 2        | MaxPooling      | 3x3             | 2          | 2     | 7     | 2*2=4          | 7+(3-1)*2=11                         |
| 3        | Convolution     | 3x3             | 1          | 4     | 11    | 4*1=4          | 11+(3-1)*4=19                        |
| 4        | MaxPooling      | 3x3             | 2          | 4     | 19    | 4*2=8          | 19+(3-1)*4=27                        |
| 5        | Inception(3a)   | 3x3             | 1          | 8     | 27    | 8*1=8          | 27+(3-1)*8=43                        |
| 6        | Inception(3b)   | 3x3             | 1          | 8     | 43    | 8*1=8          | 43+(3-1)*8=59                        |
| 7        | MaxPooling      | 3x3             | 2          | 8     | 59    | 8*2=16         | 59+(3-1)*8=75                        |
| 8        | Inception(4a)   | 3x3             | 1          | 16    | 75    | 16*1=16        | 75+(3-1)*16=107                      |
| 9        | Inception(4b)   | 3x3             | 1          | 16    | 107   | 16*1=16        | 107+(3-1)*16=139                     |
| 10       | Inception(4c)   | 3x3             | 1          | 16    | 139   | 16*1=16        | 139+(3-1)*16=171                     |
| 11       | Inception(4d)   | 3x3             | 1          | 16    | 171   | 16*1=16        | 171+(3-1)*16=203                     |
| 12       | Inception(4e)   | 3x3             | 1          | 16    | 203   | 16*1=16        | 203+(3-1)*16=235                     |
| 13       | MaxPooling      | 3x3             | 2          | 16    | 235   | 16*2=32        | 235+(3-1)*16=267                     |
| 14       | Inception(5a)   | 3x3             | 1          | 32    | 267   | 32*1=32        | 267+(3-1)*32=331                     |
| 15       | Inception(5b)   | 3x3             | 1          | 32    | 331   | 32*1=32        | 331+(3-1)*32=395                     |
| 16       | Average Pooling | 7x7             | 1          | 32    | 395   | 32*1=32        | 395+(7-1)*32=587                     |



## USING RF OF 1X1 KERNEL FROM A GROUP CONVOLUTION

| Layer No | Layer Name      | Kernel Size (k) | Stride (s) | j(in) | r(in) | j(out)=j(in)*s | Calculation r(out)=r(in)+(k-1)*j(in) |
| -------- | --------------- | --------------- | ---------- | ----- | ----- | -------------- | ------------------------------------ |
| 1        | Convolution     | 7x7             | 2          | 1     | 1     | 1*2=2          | 1+(7-1)*1=7                          |
| 2        | MaxPooling      | 3x3             | 2          | 2     | 7     | 2*2=4          | 7+(3-1)*2=11                         |
| 3        | Convolution     | 3x3             | 1          | 4     | 11    | 4*1=4          | 11+(3-1)*4=19                        |
| 4        | MaxPooling      | 3x3             | 2          | 4     | 19    | 4*2=8          | 19+(3-1)*4=27                        |
| 5        | Inception(3a)   | 1x1             | 1          | 8     | 27    | 8*1=8          | 27+(1-1)*8=27                        |
| 6        | Inception(3b)   | 1x1             | 1          | 8     | 27    | 8*1=8          | 27+(1-1)*8=27                        |
| 7        | MaxPooling      | 3x3             | 2          | 8     | 27    | 8*2=16         | 27+(3-1)*8=43                        |
| 8        | Inception(4a)   | 1x1             | 1          | 16    | 43    | 16*1=16        | 43+(1-1)*16=43                       |
| 9        | Inception(4b)   | 1x1             | 1          | 16    | 43    | 16*1=16        | 43+(1-1)*16=43                       |
| 10       | Inception(4c)   | 1x1             | 1          | 16    | 43    | 16*1=16        | 43+(1-1)*16=43                       |
| 11       | Inception(4d)   | 1x1             | 1          | 16    | 43    | 16*1=16        | 43+(1-1)*16=43                       |
| 12       | Inception(4e)   | 1x1             | 1          | 16    | 43    | 16*1=16        | 43+(1-1)*16=43                       |
| 13       | MaxPooling      | 3x3             | 2          | 16    | 43    | 16*2=32        | 43+(3-1)*16=75                       |
| 14       | Inception(5a)   | 1x1             | 1          | 32    | 75    | 32*1=32        | 75+(1-1)*32=75                       |
| 15       | Inception(5b)   | 1x1             | 1          | 32    | 75    | 32*1=32        | 75+(1-1)*32=75                       |
| 16       | Average Pooling | 7x7             | 1          | 32    | 75    | 32*1=32        | 75+(7-1)*32=267                      |
