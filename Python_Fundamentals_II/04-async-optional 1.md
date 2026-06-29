# Assignment 4 — Do Slow Things at the Same Time (OPTIONAL)

**Topic:** async Python. **Optional.** Requires Python 3.8+.

## Task
When you have several slow tasks (like downloads), Python can do them at the
**same time** instead of one after another.

1. Write an `async` function `download(name, seconds)` that prints "start",
   waits using `await asyncio.sleep(seconds)` (pretending to download), prints
   "done", and returns a short string.
2. In `main()`, run **three** downloads of 2 seconds each at the same time using
   `asyncio.gather(...)`, and print how long it took in total.

## Example output
```
start file1
start file2
start file3
done file1
done file2
done file3
['file1 (2s)', 'file2 (2s)', 'file3 (2s)']
took 2.0s          <-- about 2 seconds, NOT 6, because they ran together
```

## Done when
- [ ] All three start before any finishes.
- [ ] Total time is about 2 seconds, not 6.

## One question to answer
In one sentence: why did it take ~2 seconds instead of ~6?
