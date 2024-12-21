# hash-cracker

If you are using Pipenv, do ```pipenv install && pipenv shell```

## Example 

900150983cd24fb0d6963f7d28e17f72 => "abc"

```bash
python main.py \
  --hashing-algorithm="md5" \
  --target-hash="900150983cd24fb0d6963f7d28e17f72" \
  --max-length=5 \
  -uld
```
