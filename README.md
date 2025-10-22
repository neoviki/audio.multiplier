# audio.multiplier

**Repeat an audio file a specific number of times.**  
This tool takes an input `.mp3` file and repeats it multiple times to generate a longer version.

---

## Install

```bash
./install.ubuntu.sh
```

This script installs all necessary dependencies.

---

## Usage

```bash
$ audio.multiplier <input_mp3_file> <repeat_count>
```

### Example

```bash
$ audio.multiplier sample.mp3 60
```

This will generate a new file:

```
sample_x60.mp3
```

The output will be `calm-track.mp3` repeated **60 times** back-to-back.

---

## What does “repeat count” mean?

- The second argument is the **number of times the audio will be repeated**.
- If your original audio is 1 minute and you pass `60`, the final output will be **60 minutes long** (1-minute mp3 × 60 repetitions).

