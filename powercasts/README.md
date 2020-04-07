
# PowerCasts User Guide v0.2

<br>

### 1. Parse OPML PocketCast exported feed

Run `opml_parser_2.py` with your downloaded OPML XML filename as argument to build a JSON with every full-text RSS feed and a text file `podcasts_opml.txt` with all episode URLs:


```python
! python opml_parser_2.py podcasts_opml.xml
```


```python
! ls -lh podcasts_opml.json podcasts_opml.txt
```

    -rw-r--r-- 1 dd dd 235M Feb 21 10:12 podcasts_opml.json
    -rw-r--r-- 1 dd dd 6.5M Feb 21 10:12 podcasts_opml.txt


<br>

#### 1.1. Review all episodes text file


```python
! head -n 5 podcasts_opml.txt
```

    https://mcdn.podbean.com/mf/web/25unw3/I_en_forstad_til_m_rket_REMIX.mp3
    https://mcdn.podbean.com/mf/web/ptjkia/Hestene_er_Stille_REMIX.mp3
    https://mcdn.podbean.com/mf/web/r8f7nx/Farfars_to_liv_REMIX.mp3
    https://mcdn.podbean.com/mf/web/yi2emh/21_Roser_afsnit_05_31_07.mp3
    https://mcdn.podbean.com/mf/web/6pc4f7/21_Roser_afsnit_04_26_46.mp3



```python
! cat podcasts_opml.txt | wc      # 76.589 episodes
```

      76589   76589 6794807


<br>

#### 1.2. Output newest episodes text file

Run `newest.py` to output the newest episodes from all feeds:


```python
! python newest.py podcasts_opml.json > newest.txt
```

<br>

#### 1.3. Output HTML links

Run `html_parser.py` with `urls.txt` and `output.htm` arguments:


```python
! ./html_parser.py newest.txt newest.htm
```

    Wrote file newest.htm


<br>

                                            February 21st by d@v1d.dk
