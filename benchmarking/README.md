# Benchmarking & tear-downs

Reference motors we take apart to learn real geometry, windings, magnets, and bearings — then compare against our DIY builds (e.g. [3N4P](../builds/3n4p/)).

## How to add a motor

1. Create a folder: `benchmarking/<short-name>/`  
   Example: `benchmarking/drone-outrunner-2207/`
2. Copy photos into that folder’s `photos/`.
3. Fill in `README.md` using the template below (or copy [`_template/README.md`](_template/README.md)).

```
benchmarking/
├── README.md                 ← this index
├── _template/
│   └── README.md
└── <motor-name>/
    ├── README.md
    └── photos/
        ├── 01-outside.jpg
        ├── 02-rotor.jpg
        └── ...
```

## Motors

| Motor | Folder | Notes |
|-------|--------|--------|
| *(your tear-down)* | *add when photos land* | Past teardown — drop pics in a new folder |

---

## What to capture (checklist)

- [ ] Outside: labels, KV/size marks, shaft OD  
- [ ] End bell / bearing size (ID, OD, width if readable)  
- [ ] Rotor: magnet count, magnet shape/approx size, N–S pattern  
- [ ] Stator: slot count, tooth shape, stack height, wire gauge estimate  
- [ ] Winding: turns estimate if countable, star vs delta if visible  
- [ ] Air gap feel / any shims  
- [ ] Anything surprising vs our 3N4P print  

Drop photos anytime — we can fill the write-up from the images together.
