# jarvispatrick
Jarvis-Patrick Clustering that uses a nearest neighbor approach to clustering objects

Example
------

```python
from chemfp.bitops import byte_tanimoto

ligands = [
            "00000000 00000000 00000017 2d6ca331 83a0c5cc 846e0c0120030000 00000000", 
            "00000000 00000000 0000001f bde88331 0385854a 9472040201010000 20000480", 
            "00000000 00000000 0000001b 2f6ce37d cbb0e5c8 aef7540520010029 a0000480",
            ... add more fingerprints ...
        ]

cluster_generator = JarvisPatrick(ligands, byte_tanimoto)
cluster = cluster_generator(9, 8)
```
