# Thanks for looking at my tool

![Docker Image Status](https://github.com/findarato/xander-casts/actions/workflows/deploy-image.yml/badge.svg?branch=release)

All docker builds and images are hosted by Moved over to github, and the builds are automated on a merge into the release branch.

I need to mention that [powercasts](https://github.com/taext/powercasts) is not something I wrote, and I do not take credit for it. I also used the code from [this](https://github.com/balloob/pychromecast/issues/330#issue-541432178) issue to make the queueing system work.  Their work is basically the whole player.py script

If you are running the Docker container it needs host networking for the Chromecast part to work.

## Environment Variables

- total_podcast_to_play
  - Defaults to 20
- chromecast_name
  - Defaults to Xander Room
  - His name starts with an X, big woop, wana fight about it?

## Design
This tool is designed to play a random episode from a selection of podcasts.  It is set up to play 20 podcasts, and this is currently not configurable

Also I am 100% open to pull requsts to make the python better, I am still super new at coding python and would love some pointers.

:TODO

- [x] Add support for setting amount of podcasts
- [ ] Add support for sending specific IP to the chromecast
- [x] Add cover image support
  - [x] Pull cover image from the podcast feed
  - [x] Pull the title from the podcast feed

