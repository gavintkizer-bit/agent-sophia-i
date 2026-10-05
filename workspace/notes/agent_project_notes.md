agent project - scratch notes (messy on purpose)

- laptop = macbook pro 13in 2016, 2 cores, 8gb ram. desktop app wont install. cant update macOS??
- claude code locally needs macOS 13+ ... mine is older. chrome also stops updating on old macOS -> use firefox or edge
- path A = no code. claude.ai projects + cowork in the browser. scheduled tasks run in cloud
- path B = THIS ONE. github repo + claude.ai/code cloud session + agent sdk agent. SET UP AND WORKING.
- path C = fix the mac. check About This Mac. maybe free up disk space then upgrade to monterey. opencore legacy patcher for ventura+ but unofficial, back up first
- want: organized, test workarounds, improve over time
- NEW GOAL (oct 2026): keep my laptop + life organized. step 1 = clean up Downloads (15 GB) without breaking ableton samples. macOS upgrade / desktop app = later, maybe never (2016 mac tops out at monterey)
- idea: keep a run log, write one thing to change after every run (doing this: logs/run_log.md)
- todo later: give the agent web search? a weekly scheduled run?

ANSWERED (don't ask these again):
- api key? NOT needed in claude.ai/code cloud sessions. old key was revoked. no separate billing for these runs
- does the cloud network allow api.anthropic.com? yes, agent.py --check says READY and runs work
- cheapest model? haiku (claude-haiku-4-5), the default. ~3-5 cents per notes run, ~33 cents for the downloads organizer

DOWNLOADS SO FAR (oct 5):
- organize.sh made: moves 609 of 1219 files into folders. haven't run it yet
- moving doesn't free space. space wins: ableton .alp packs 5.7 GB (delete once installed in ableton), installers .dmg/.pkg 2.4 GB, duplicate "(1)" copies 1.3 GB
- careful: moving .wav/.mp3/.asd out of downloads can break ableton projects that use them
