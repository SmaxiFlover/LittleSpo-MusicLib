# DIARY OF LittleSpo - MusicLib

SmaxiFlover

------------------

### 2019-01-11

Using Centra-C (C<sub>3</sub>) as the root, we have the following table
, where $f$ is in the range [C<sub>2</sub>, C<sub>3</sub>]

| mul |    Key_Level    |  $f$   | $f_{12}$ |   $e$   |
|:---:|:---------------:|:------:|:--------:|:-------:|
|  2  |        I        | 261.63 |  261.63  |  0.00%  |
|  3  |        V        | 392.44 |  392.00  |  1.96%  |
|  5  |       III       | 327.03 |  329.63  | -13.69% |
|  7  | <sup>b</sup>VII | 457.84 |  466.16  | -31.17% |
| 11  |  <sup>b</sup>V  | 359.74 |  369.99  | -48.68% |
| 13  | <sup>b</sup>VI  | 425.14 |  415.30  | 40.53%  |
| 17  | <sub>b</sup>II  | 277.98 |  277.18  |  4.96%  |

| mul |   Key_Level    |  $f$   | $f_{12}$ |   $e$   |
|:---:|:--------------:|:------:|:--------:|:-------:|
| -2  |       I        | 261.63 |  261.63  |  0.00%  |
| -3  |       IV       | 348.83 |  349.23  | -1.96%  |
| -5  | <sup>b</sup>VI | 418.60 |  415.30  | 13.69%  |
| -7  |       II       | 299.00 |  293.66  | 31.17%  |
| -11 | <sup>b</sup>V  | 380.55 |  369.99  | 48.68%  |
| -13 |      III       | 322.00 |  329.63  | -40.53% |
| -17 |      VII       | 492.47 |  493.88  | -4.96%  |


### 2019-01-14

Add the function `PlayChord(nodes, file_name, length, loudness)` to the library.

### 2019-01-15

`step` Data for *Twelve-tone Equal Temperament* in *Just Inotation*.

| step | pure | maj  | min | dim  |  aug  |
|:----:|:----:|:----:|:---:|:----:|:-----:|
|  II  |      |  -7  | -15 |      |       |
| III  |      |  5   | 3/5 |      |       |
|  IV  |  -3  |      |     |      | -9/25 |
|  V   |  3   |      |     | 9/25 |       |
|  VI  |      | -3/5 | -5  |      |       |
| VII  |      |  15  |  7  |      |       |

| step | pure |  maj  |  min   | dim  |  aug  |
|:----:|:----:|:-----:|:------:|:----:|:-----:|
|  II  |      | -1.75 | -1.875 |      |       |
| III  |      | 1.25  |  1.2   |      |       |
|  IV  | -1.5 |       |        |      | -1.44 |
|  V   | 1.5  |       |        | 1.44 |       |
|  VI  |      | -1.2  | -1.25  |      |       |
| VII  |      | 1.875 |  1.75  |      |       |

As `expreiment2` shows in the `experiment.py`, pop
