# Till Firmware Do Us Part

A make.fun bounty entry: a single wedding vow for a robot, one sentence
under 200 characters, funny and heartfelt at the same time.

## The vow

> I vow to love you through every update, reboot, and system crash, and never factory-reset us, till firmware do us part.

119 characters, one sentence, one line. Verified by running the program
and checking the output file (see local check below).

## Local check

```sh
MAKEFUN_OUTPUT_DIR=/tmp/till-firmware-check python3 main.py
python3 -c "t=open('/tmp/till-firmware-check/entry.txt',encoding='utf-8').read(); print(len(t), repr(t))"
```

Expected: 119 characters, exactly the vow above, one line, no trailing
newline.

## Why this line

- It is a vow a robot speaks at its own wedding: a promise made in the
  machine's own vocabulary (update, reboot, system crash, factory-reset).
- The laugh comes from the situation itself: a robot promising, in
  technical terms, never to wipe the relationship.
- The tenderness sits under the joke: "never factory-reset us" is a
  promise of permanence, and "till firmware do us part" turns the
  classic wedding line into the robot's version of forever.

## How it works

`main.py` writes the vow to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) as UTF-8, mode 0644, with no trailing
newline. Run it with:

```sh
python3 main.py
```

## Bounty

- Competition: `u-azazex-till-firmware-do-us-part-32172929`
- Title: Till Firmware Do Us Part
- Pot: $2.50, top 10 paid

## License

MIT — see `LICENSE`.
